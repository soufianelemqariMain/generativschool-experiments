"""Optional extraction from downloaded official CSV files; no victims data."""
import argparse,hashlib,json
from pathlib import Path
import pandas as pd
P=Path(__file__).parent
parser=argparse.ArgumentParser();parser.add_argument('source_directory',type=Path);args=parser.parse_args()
source=json.loads((P/'data/source.json').read_text());out=[];audit=[]
deps=[f'{n:02}' for n in range(1,96) if n!=20]+['2A','2B']
for meta in sorted(source['resources'],key=lambda r:r['year']):
 y=meta['year'];raw=(args.source_directory/f'{y}.csv').read_bytes();assert hashlib.sha256(raw).hexdigest()==meta['sha256']
 import io
 try:text=raw.decode('utf-8-sig')
 except UnicodeDecodeError:text=raw.decode('latin1')
 d=pd.read_csv(io.StringIO(text),sep=None,engine='python',dtype=str)
 ident='Num_Acc' if 'Num_Acc' in d else 'Accident_Id';assert not d[ident].duplicated().any()
 def dep(v):
  v=v.strip().upper()
  if y<=2018:
   if v=='201':return '2A'
   if v=='202':return '2B'
   if len(v)==3 and v.endswith('0'):return v[:2]
   return v
  return v.zfill(2)
 d['department']=d.dep.map(dep);d['month']=pd.to_numeric(d.mois);assert d.month.between(1,12).all()
 d=d[d.department.isin(deps)]
 counts=d.groupby(['department','month']).size()
 for code in deps:
  for m in range(1,13):out.append({'year':y,'month':m,'department':code,'accidents':int(counts.get((code,m),0))})
 audit.append({'year':y,'metropolitan_rows':len(d),'departments':d.department.nunique()})
pd.DataFrame(out).to_csv(P/'data/monthly.csv',index=False)
(P/'data/extraction-audit.json').write_text(json.dumps(audit,indent=2))
print(audit)
