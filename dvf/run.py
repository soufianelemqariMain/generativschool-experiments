import json,hashlib
from pathlib import Path
import pandas as pd,numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
P=Path(__file__).resolve().parent
extract=P/'data/departements.csv'
if not extract.exists():
 d=pd.read_csv(P/'data/snapshot.csv',dtype={'code_geo':str},low_memory=False);d=d[d.echelle_geo=='departement'];d[['code_geo','libelle_geo','annee_mois','nb_ventes_maison','med_prix_m2_maison']].to_csv(extract,index=False)
d=pd.read_csv(extract,dtype={'code_geo':str});d['month']=pd.to_datetime(d.annee_mois);d['y']=pd.to_numeric(d.med_prix_m2_maison,errors='coerce');d.loc[(d.nb_ventes_maison<30)|(d.y<=0),'y']=np.nan;frames=[]
for dept,g in d.groupby('code_geo'):
 g=g.drop_duplicates('month').set_index('month').reindex(pd.date_range(d.month.min(),d.month.max(),freq='MS'));g['dept']=dept
 for lag in [6,7,12]:g[f'lag{lag}']=g.y.shift(lag)
 g['sin']=np.sin(2*np.pi*g.index.month/12);g['cos']=np.cos(2*np.pi*g.index.month/12);g.index.name='month';frames.append(g.reset_index())
f=pd.concat(frames);features=['lag6','lag7','lag12','sin','cos'];f=f.dropna(subset=features+['y']);train=f[f.month<'2025-01-01'];test=f[f.month>='2025-01-01'].copy();model=make_pipeline(ColumnTransformer([('dept',OneHotEncoder(handle_unknown='ignore',sparse_output=False),['dept']),('num','passthrough',features)]),RandomForestRegressor(n_estimators=100,max_depth=8,min_samples_leaf=10,random_state=42,n_jobs=2));model.fit(train[['dept']+features],train.y);test['foret']=model.predict(test[['dept']+features]);test['six_mois']=test.lag6;test['douze_mois']=test.lag12;metrics={}
for name in ['foret','six_mois','douze_mois']:
 err=abs(test[name]-test.y);metrics[name]={'mae_euros_m2':float(err.mean()),'mae_ponderee_ventes':float(np.average(err,weights=test.nb_ventes_maison)),'par_annee':{str(y):float(abs(g[name]-g.y).mean()) for y,g in test.groupby(test.month.dt.year)}}
test[['month','dept','y','nb_ventes_maison','foret','six_mois','douze_mois']].to_csv(P/'predictions.csv',index=False);result={'train_rows':len(train),'test_rows':len(test),'departements':test.dept.nunique(),'start':str(test.month.min().date()),'end':str(test.month.max().date()),'metrics':metrics,'extract_sha256':hashlib.sha256(extract.read_bytes()).hexdigest()};(P/'results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
