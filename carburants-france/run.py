"""Comparaison contrôlée : station, pétrole/change, géopolitique. Hors réseau."""
from pathlib import Path
import json,hashlib,time,platform,zipfile
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestRegressor
R=Path(__file__).resolve().parent
BASE=['prix','d1','d2','d3','d4','age','sin','cos']
OIL=['brent_eur','brent_d7','brent_d28','usd_per_eur','fx_d7']
GEO=['gpr7','gpr_d28']
METHODS=['persistence','momentum','station_ai','oil_ai','context_ai']
def inputs():
 m=json.loads((R/'data/manifest.json').read_text())
 for n in ['declarations.csv','stations.json']:assert hashlib.sha256((R/'data'/n).read_bytes()).hexdigest()==m[n]
 for n,v in json.loads((R/'data/macro-sources.json').read_text()).items():assert hashlib.sha256((R/'data'/n).read_bytes()).hexdigest()==v['sha256']
 d=pd.read_csv(R/'data/declarations.csv',dtype={'station':str});d['date']=pd.to_datetime(d.date);return d

def macro():
 b=pd.read_excel(R/'data/brent.xls',sheet_name='Data 1',skiprows=2);b.columns=['date','brent'];b['date']=pd.to_datetime(b.date)
 with zipfile.ZipFile(R/'data/fx.zip') as z:f=pd.read_csv(z.open('eurofxref-hist.csv'),usecols=['Date','USD']).rename(columns={'Date':'date','USD':'usd_per_eur'})
 f['date']=pd.to_datetime(f.date)
 g=pd.read_excel(R/'data/gpr.xls')[['date','GPRD']].rename(columns={'GPRD':'gpr'});g['date']=pd.to_datetime(g.date)
 days=pd.DataFrame({'date':pd.date_range('2022-11-01','2026-09-30')})
 for x in [b,f,g]:days=pd.merge_asof(days,x.sort_values('date'),on='date',direction='backward')
 days['brent_eur']=days.brent/days.usd_per_eur
 days['brent_d7']=days.brent_eur.diff(7);days['brent_d28']=days.brent_eur.diff(28);days['fx_d7']=days.usd_per_eur.diff(7)
 days['gpr7']=days.gpr.rolling(7).mean();days['gpr_d28']=days.gpr7.diff(28)
 # Common 14-day information delay. Dates are observation dates, not certified release vintages.
 days['macro_observation']=days.date;days['available']=days.date+pd.Timedelta(days=14)
 return days[['available','macro_observation']+OIL+GEO].dropna()

def panel(d):
 parts=[];weeks=pd.date_range('2023-01-01 23:59:59','2026-09-27 23:59:59',freq='7D');coverage={}
 for (fuel,sid),g in d.groupby(['fuel','station']):
  g=g.sort_values(['date','prix']).drop_duplicates('date',keep='last')
  t=pd.merge_asof(pd.DataFrame({'origin':weeks}),g.rename(columns={'date':'declared'}),left_on='origin',right_on='declared',direction='backward')
  t['fuel']=fuel;t['station']=sid;t['age']=(t.origin-t.declared).dt.total_seconds()/86400
  c=coverage.setdefault(fuel,{'slots':0,'fresh':0});c['slots']+=len(t);c['fresh']+=int((t.age<=7).sum())
  t.loc[t.age>7,'prix']=np.nan
  for n in range(1,5):t[f'd{n}']=t.prix.shift(n-1)-t.prix.shift(n)
  t['sin']=np.sin(2*np.pi*t.origin.dt.dayofyear/365.25);t['cos']=np.cos(2*np.pi*t.origin.dt.dayofyear/365.25)
  t['actual']=t.prix.shift(-1);t['target']=t.origin+pd.Timedelta(days=7);t['change']=t.actual-t.prix
  parts.append(t.dropna(subset=BASE+['actual']))
 t=pd.concat(parts).sort_values(['origin','station','fuel']).reset_index(drop=True)
 return t,coverage

def enrich(t,m):return pd.merge_asof(t.sort_values('origin',kind='stable'),m.sort_values('available',kind='stable'),left_on='origin',right_on='available',direction='backward').dropna(subset=OIL+GEO)

def predict(t):
 rows=[]
 for fuel,allrows in t.groupby('fuel'):
  test=allrows[(allrows.target.dt.year==2026)&(allrows.target<='2026-09-30')]
  for month,g in test.groupby(test.target.dt.month):
   cutoff=g.origin.min();train=allrows[allrows.target<=cutoff];assert train.target.max()<=g.origin.min()
   forecasts={}
   for name,cols in [('station_ai',BASE),('oil_ai',BASE+OIL),('context_ai',BASE+OIL+GEO)]:
    model=RandomForestRegressor(n_estimators=80,max_depth=8,min_samples_leaf=20,random_state=42,n_jobs=1)
    forecasts[name]=model.fit(train[cols],train.change).predict(g[cols])+g.prix.to_numpy()
   for j,(_,r) in enumerate(g.iterrows()):
    row={'fuel':fuel,'station':r.station,'date':str(r.target.date()),'origin':str(r.origin.date()),'training_last_target':str(train.target.max().date()),'macro_observation':str(r.macro_observation.date()),'known':float(r.prix),'actual':float(r.actual),'persistence':float(r.prix),'momentum':float(r.prix+r.d1),'age_days':float(r.age),'brent_eur':float(r.brent_eur),'usd_per_eur':float(r.usd_per_eur),'gpr7':float(r.gpr7)}
    row.update({name:float(v[j]) for name,v in forecasts.items()});rows.append(row)
 return rows

def metrics(rows):
 out={'n':len(rows),'stations':len(set(r['station'] for r in rows))}
 for key in METHODS:
  err=np.array([abs(r[key]-r['actual']) for r in rows]);changed=[r for r in rows if abs(r['actual']-r['known'])>1e-9]
  by=[np.mean([abs(r[key]-r['actual']) for r in rows if r['station']==s]) for s in sorted(set(r['station'] for r in rows))]
  out[key]={'mae':float(err.mean()),'station_weighted_mae':float(np.mean(by)),'direction_accuracy':float(np.mean([np.sign(r[key]-r['known'])==np.sign(r['actual']-r['known']) for r in changed])),'changed_n':len(changed)}
 return out
if __name__=='__main__':
 start=time.perf_counter();t,coverage=panel(inputs());m=macro();joined=enrich(t,m);rows=predict(joined)
 result={'country':'France','period':'2026-01-01/2026-09-30','macro_delay_days':14,'coverage':coverage,'fuels':{},'predictions':rows}
 for fuel in ['Gazole','E10','SP95','SP98']:
  rr=[r for r in rows if r['fuel']==fuel];result['fuels'][fuel]={'metrics':metrics(rr),'quarters':{str(q):metrics([r for r in rr if (int(r['date'][5:7])-1)//3+1==q]) for q in [1,2,3]}}
 (R/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');m.to_csv(R/'data/macro-derived.csv',index=False)
 (R/'execution.json').write_text(json.dumps({'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'sklearn':sklearn.__version__,'seconds':round(time.perf_counter()-start,2),'command':'python run.py','paid_calls':0},indent=2))
 print(json.dumps(result['fuels'],ensure_ascii=False,indent=2))
