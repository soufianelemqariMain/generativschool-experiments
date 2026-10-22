"""Extraction contrôlable des archives officielles : python extract.py /chemin/archives.
Les archives 2023.zip, 2024.zip, 2025.zip sont téléchargées séparément depuis sources.json.
"""
from pathlib import Path
import sys,zipfile,xml.etree.ElementTree as ET,hashlib,json,csv
R=Path(__file__).resolve().parent; raw=Path(sys.argv[1]);sources=json.loads((R/'data/station-sources.json').read_text())
def stations(year):
 p=raw/f'{year}.zip'
 assert hashlib.sha256(p.read_bytes()).hexdigest()==sources[str(year)]['sha256']
 with zipfile.ZipFile(p) as z:
  with z.open(next(n for n in z.namelist() if n.endswith('.xml'))) as f:
   for _,e in ET.iterparse(f,events=('end',)):
    if e.tag=='pdv':
     yield e
     e.clear()
ids=[]
for e in stations(2023):
 if any(p.get('nom') in ['Gazole','E10','SP95','SP98'] for p in e.findall('prix')):ids.append(e.get('id'))
selected=set(sorted(set(ids),key=lambda s:hashlib.sha256(s.encode()).hexdigest())[:120])
rows=[];meta={};invalid=0
for year in [2023,2024,2025,2026]:
 for e in stations(year):
  sid=e.get('id')
  if sid not in selected:continue
  if sid not in meta:meta[sid]={'ville':e.findtext('ville'),'code_postal':e.get('cp'),'type':e.get('pop')}
  for p in e.findall('prix'):
   if p.get('nom') not in ['Gazole','E10','SP95','SP98']:continue
   v=float(p.get('valeur'))
   # Some historical archives use millieuro integer values; modern ones use euro decimals.
   if v>100:v/=1000
   if not 0.5<=v<=4:invalid+=1;continue
   rows.append((sid,p.get('nom'),p.get('maj').replace('T',' '),v))
rows=sorted(set(rows))
p=R/'data/declarations.csv'
with p.open('w') as f:
 w=csv.writer(f);w.writerow(['station','fuel','date','prix']);w.writerows(rows)
(R/'data/stations.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
(R/'data/manifest.json').write_text(json.dumps({'declarations.csv':hashlib.sha256(p.read_bytes()).hexdigest(),'stations.json':hashlib.sha256((R/'data/stations.json').read_bytes()).hexdigest(),'eligible_2023':len(set(ids)),'selected':len(selected),'declarations':len(rows),'invalid_prices_excluded':invalid},indent=2))
print({'selected':len(selected),'declarations':len(rows),'sample':rows[:2],'invalid':invalid})
