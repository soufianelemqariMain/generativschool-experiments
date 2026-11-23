import json,hashlib
from pathlib import Path
import numpy as np,pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
P=Path(__file__).resolve().parent
raw=(P/'data/snapshot.json').read_bytes();source=json.loads((P/'data/source.json').read_text());assert hashlib.sha256(raw).hexdigest()==source['sha256']
d=pd.DataFrame(json.loads(raw));d=d[d.service=='National'].copy();d['route']=d.gare_depart+' → '+d.gare_arrivee;d['month']=pd.to_datetime(d.date);d['volume']=pd.to_numeric(d.nb_train_prevu)-pd.to_numeric(d.nb_annulation);d['y']=100*pd.to_numeric(d.nb_train_retard_arrivee)/d.volume;d=d[(d.volume>0)&d.y.between(0,100)].drop_duplicates(['route','month'])
frames=[]
for route,g in d.groupby('route'):
 g=g.set_index('month').reindex(pd.date_range(d.month.min(),d.month.max(),freq='MS'));g['route']=route
 for lag in [2,3,12]:g[f'lag{lag}']=g.y.shift(lag)
 g['mean6']=g.y.shift(2).rolling(6,min_periods=6).mean();g['sin']=np.sin(2*np.pi*g.index.month/12);g['cos']=np.cos(2*np.pi*g.index.month/12);g.index.name='month';frames.append(g.reset_index())
f=pd.concat(frames);features=['lag2','lag3','lag12','mean6','sin','cos'];f=f.dropna(subset=features+['y','volume']);train=f[f.month<'2025-01-01'];test=f[f.month>='2025-01-01'].copy();assert len(train)>500 and len(test)>100
model=make_pipeline(ColumnTransformer([('route',OneHotEncoder(handle_unknown='ignore',sparse_output=False),['route']),('numbers','passthrough',features)]),RandomForestRegressor(n_estimators=100,max_depth=8,min_samples_leaf=10,random_state=42,n_jobs=2));model.fit(train[['route']+features],train.y)
test['foret']=model.predict(test[['route']+features]);test['annee_precedente']=test.lag12;test['mois_moins_deux']=test.lag2
metrics={}
for name in ['foret','annee_precedente','mois_moins_deux']:
 err=abs(test[name]-test.y);metrics[name]={'mae_points':float(err.mean()),'mae_ponderee_trains':float(np.average(err,weights=test.volume)),'par_annee':{str(y):float(abs(g[name]-g.y).mean()) for y,g in test.groupby(test.month.dt.year)}}
cols=['month','route','y','volume','foret','annee_precedente','mois_moins_deux'];out=test[cols].copy();out['month']=out.month.dt.strftime('%Y-%m');out.to_csv(P/'predictions.csv',index=False)
result={'train_rows':len(train),'test_rows':len(test),'routes':test.route.nunique(),'start':out.month.min(),'end':out.month.max(),'metrics':metrics,'source':source,'unit':'points de pourcentage','features':features+['route']};(P/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
