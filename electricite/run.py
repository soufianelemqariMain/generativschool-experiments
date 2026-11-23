import json,hashlib
from pathlib import Path
import numpy as np,pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
P=Path(__file__).resolve().parent;raw=(P/'data/snapshot.json').read_bytes();source=json.loads((P/'data/source.json').read_text());assert hashlib.sha256(raw).hexdigest()==source['sha256']
d=pd.DataFrame(json.loads(raw));d['t']=pd.to_datetime(d.date_heure,utc=True);d=d.set_index('t').sort_index();d=d[~d.index.duplicated()];d=d[d.index.minute.isin([0,30])];d['consommation']=pd.to_numeric(d.consommation,errors='coerce');d['prevision_j1']=pd.to_numeric(d.prevision_j1,errors='coerce');counts=d.consommation.resample('h').count();f=d[['consommation','prevision_j1']].resample('h').mean();f.loc[counts<2,'consommation']=np.nan;f=f.rename(columns={'consommation':'y'});features=[]
for lag in [24,48,168]:k=f'lag{lag}';f[k]=f.y.shift(lag);features.append(k)
f['mean24']=f.y.shift(24).rolling(24,min_periods=24).mean();features.append('mean24');local=f.index.tz_convert('Europe/Paris')
for name,values,period in [('heure',local.hour,24),('jour',local.dayofweek,7),('mois',local.month,12)]:
 for trig,fn in [('sin',np.sin),('cos',np.cos)]:k=name+trig;f[k]=fn(2*np.pi*values/period);features.append(k)
f=f.dropna(subset=features+['y','prevision_j1']);train=f[f.index<'2025-01-01'];test=f[f.index>='2025-01-01'].copy();assert len(train)>10000
models={'ridge':make_pipeline(StandardScaler(),Ridge(alpha=10)),'foret':RandomForestRegressor(n_estimators=80,max_depth=12,min_samples_leaf=20,random_state=42,n_jobs=2)}
for name,model in models.items():model.fit(train[features],train.y);test[name]=model.predict(test[features])
test['veille']=test.lag24;test['semaine']=test.lag168;test['rte_j1']=test.prevision_j1;threshold=float(train.y.quantile(.9));metrics={}
for name in ['veille','semaine','ridge','foret','rte_j1']:
 err=abs(test[name]-test.y);metrics[name]={'mae_MW':float(err.mean()),'mae_pointes_MW':float(err[test.y>=threshold].mean()),'par_annee':{str(y):float(abs(g[name]-g.y).mean()) for y,g in test.groupby(test.index.year)}}
cols=['y','veille','semaine','ridge','foret','rte_j1'];test[cols].to_csv(P/'predictions.csv',index_label='heure_UTC');result={'train_rows':len(train),'test_rows':len(test),'start':str(test.index.min()),'end':str(test.index.max()),'peak_threshold_MW':threshold,'metrics':metrics,'source':source};(P/'results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
