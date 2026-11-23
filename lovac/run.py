import json,hashlib
from pathlib import Path
import pandas as pd,numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
P=Path(__file__).resolve().parent;d=pd.read_csv(P/'data/snapshot.csv',encoding='cp1252',sep=';',dtype=str);frames=[]
for y in [23,24,25,26]:
 f=pd.DataFrame({'commune':d.CODGEO_26,'region':d.REG,'year':2000+y,'y':pd.to_numeric(d[f'pp_vacant_{y}'],errors='coerce'),'lag1':pd.to_numeric(d[f'pp_vacant_{y-1}'],errors='coerce'),'lag2':pd.to_numeric(d[f'pp_vacant_{y-2}'],errors='coerce'),'stock':pd.to_numeric(d[f'ff_pp_total_{y-2}'],errors='coerce')});f['delta']=f.lag1-f.lag2;frames.append(f)
f=pd.concat(frames).dropna();train=f[f.year<2026];test=f[f.year==2026].copy();features=['lag1','lag2','stock','delta'];models={'ridge':make_pipeline(StandardScaler(),Ridge(alpha=10)),'foret':RandomForestRegressor(n_estimators=100,max_depth=10,min_samples_leaf=20,random_state=42,n_jobs=2)}
for name,m in models.items():m.fit(train[features],train.y);test[name]=np.maximum(0,m.predict(test[features]))
test['inchange']=test.lag1;metrics={}
for name in ['inchange','ridge','foret']:
 err=abs(test[name]-test.y);metrics[name]={'mae_logements':float(err.mean()),'mediane_erreur_logements':float(err.median()),'par_region':{str(k):float(abs(g[name]-g.y).mean()) for k,g in test.groupby('region')}}
test.to_csv(P/'predictions.csv',index=False);result={'train_rows':len(train),'test_communes':len(test),'total_communes_source':len(d),'year':2026,'metrics':metrics,'snapshot_sha256':hashlib.sha256((P/'data/snapshot.csv').read_bytes()).hexdigest()};(P/'results.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='metrics'},indent=2));print({k:round(v['mae_logements'],2) for k,v in metrics.items()})
