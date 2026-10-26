import urllib.request,urllib.parse,json,hashlib,datetime
from pathlib import Path
p=Path(__file__).resolve().parent/'data';p.mkdir(exist_ok=True); url='https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/rappelconso-v2-gtin-espaces/records?'+urllib.parse.urlencode({'limit':100,'order_by':'date_publication DESC, numero_fiche DESC'})
rows=[]
for offset in range(0,1000,100):
 d=json.load(urllib.request.urlopen(url+'&offset='+str(offset),timeout=30));rows+=d['results']
raw=json.dumps(rows,ensure_ascii=False,indent=2).encode();(p/'snapshot.json').write_bytes(raw)
(p/'source.json').write_text(json.dumps({'url':url,'offsets':list(range(0,1000,100)),'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(raw).hexdigest(),'license':'Licence Ouverte 2.0','publisher':'DGCCRF et partenaires via data.economie.gouv.fr','rows':len(rows)},indent=2))
print(f'{len(rows)} fiches enregistrées. Relancer --encode après toute modification du corpus.')
