import json,hashlib
from pathlib import Path
import numpy as np,pandas as pd
p=Path(__file__).resolve().parent
for name,h in json.loads((p/'manifest.json').read_text()).items():assert hashlib.sha256((p/name).read_bytes()).hexdigest()==h,name
r=json.loads((p/'results.json').read_text());key=p.name
if (p/'predictions.csv').exists():
 d=pd.read_csv(p/'predictions.csv');assert len(d)>0 and d.y.notna().all()
 metric={'tgv':'mae_points','electricite':'mae_MW','dpe':'mae','lovac':'mae_logements','dvf':'mae_euros_m2'}[key]
 for method,m in r['metrics'].items():assert np.isclose(abs(d[method]-d.y).mean(),m[metric],rtol=1e-9),(method,'metric mismatch')
 if key=='tgv':assert d.y.between(0,100).all()
 if key=='dpe':assert r['address_overlap']==0
if key=='boamp':
 for method,m in r['results'].items():
  rows=[x for x in r['details'] if x['method']==method];assert len(rows)==24;assert sum(x['rank']==1 for x in rows)==m['top1']
if key=='agribalyse':
 for x in r['examples']:
  a=x['source']
  for b in x['semantic']:
   assert a['id']!=b['id'] and a['group']==b['group'] and b['climate_kgCO2e_kg']<a['climate_kgCO2e_kg']
   assert np.isclose(b['difference_percent'],100*(b['climate_kgCO2e_kg']/a['climate_kgCO2e_kg']-1))
if key=='bpe':assert sum(r['cluster_counts'].values())==r['communes'] and r['types']>1 and 0<=r['ari_graines']<=1
if key=='eau':
 d=pd.read_csv(p/'data/profils-anonymes.csv');assert len(d)==r['complete_distribution_services'];assert int(d.selected.sum())==r['selected_count'];assert d['P104.3'].between(0,100).all()
print('OK',key,': sources gelées et résultats cohérents')
