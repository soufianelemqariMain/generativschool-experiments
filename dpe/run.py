import json,hashlib
from pathlib import Path
import pandas as pd,numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
P=Path(__file__).resolve().parent;raw=(P/'data/snapshot.json').read_bytes();source=json.loads((P/'data/source.json').read_text());assert hashlib.sha256(raw).hexdigest()==source['sha256'];d=pd.DataFrame(json.loads(raw)['results']);d['y']=pd.to_numeric(d.conso_5_usages_par_m2_ep,errors='coerce');d['surface_habitable_logement']=pd.to_numeric(d.surface_habitable_logement,errors='coerce');d=d[d.type_batiment.isin(['maison','appartement'])&d.y.between(.01,1500)&d.identifiant_ban.notna()];d=d.sort_values('date_etablissement_dpe');train=d[d.date_etablissement_dpe<'2025-01-01'];test=d[(d.date_etablissement_dpe>='2025-01-01')&~d.identifiant_ban.isin(train.identifiant_ban)].drop_duplicates('identifiant_ban',keep='last').copy();assert len(test)>100
cats=['type_batiment','periode_construction','type_energie_principale_chauffage','zone_climatique','classe_altitude','qualite_isolation_murs','qualite_isolation_menuiseries'];num=['surface_habitable_logement'];train=train.copy()
for x in [train,test]:x[cats]=x[cats].fillna('inconnu').astype(str)
model=make_pipeline(ColumnTransformer([('cats',OneHotEncoder(handle_unknown='ignore',sparse_output=False),cats),('num',SimpleImputer(strategy='median'),num)]),RandomForestRegressor(n_estimators=100,max_depth=10,min_samples_leaf=10,random_state=42,n_jobs=2));model.fit(train[cats+num],train.y);test['foret']=model.predict(test[cats+num]);med=train.groupby('type_batiment').y.median();test['mediane']=test.type_batiment.map(med);metrics={}
for name in ['foret','mediane']:metrics[name]={'mae':float(abs(test[name]-test.y).mean()),'par_type':{t:float(abs(g[name]-g.y).mean()) for t,g in test.groupby('type_batiment')}}
# Publish diagnostic characteristics and predictions, never street addresses.
out=test[['date_etablissement_dpe','type_batiment','y','foret','mediane']].copy();out.to_csv(P/'predictions.csv',index=False);result={'train_rows':len(train),'test_rows':len(test),'test_types':test.type_batiment.value_counts().to_dict(),'start':test.date_etablissement_dpe.min(),'end':test.date_etablissement_dpe.max(),'metrics':metrics,'unit':'kWh EP/m²/an','address_overlap':len(set(train.identifiant_ban)&set(test.identifiant_ban)),'source':source};(P/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
