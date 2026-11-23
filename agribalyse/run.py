import json,hashlib,sys
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;raw=(P/'data/snapshot.json').read_bytes();rows=json.loads(raw)['results'];source=json.loads((P/'data/source.json').read_text());assert hashlib.sha256(raw).hexdigest()==source['sha256'];names=[r['Nom_du_Produit_en_Français'] for r in rows];cache=P/'data/embeddings.npz';fingerprint=hashlib.sha256(json.dumps(names,ensure_ascii=False).encode()).hexdigest()
if '--encode' in sys.argv:
 from sentence_transformers import SentenceTransformer
 import torch
 torch.set_num_threads(4)
 meta=json.loads((P/'data/model.json').read_text());model=SentenceTransformer(meta['id'],revision=meta['revision'],device='cpu');vectors=model.encode(names,batch_size=32,normalize_embeddings=True,show_progress_bar=True);np.savez_compressed(cache,vectors=vectors,fingerprint=fingerprint);(P/'data/model.json').write_text(json.dumps(meta,indent=2))
e=np.load(cache);assert str(e['fingerprint'])==fingerprint;v=e['vectors'];ids=[str(r['Code_AGB']) for r in rows];results=[]
def info(i):
 r=rows[i];return {'id':ids[i],'name':names[i],'climate_kgCO2e_kg':float(r['Changement_climatique']),'dqr':r['DQR'],'group':r["Sous-groupe_d'aliment"]}
for id in ['25081','25029','25413','11114','25457','25111']:
 i=ids.index(id);a=info(i);candidates=[j for j in range(len(rows)) if ids[j]!=id and rows[j]["Sous-groupe_d'aliment"]==a['group'] and float(rows[j]['Changement_climatique'])<a['climate_kgCO2e_kg']];score=v@v[i];rank=sorted(candidates,key=lambda j:-score[j]);low=sorted(candidates,key=lambda j:float(rows[j]['Changement_climatique']));alternatives=[]
 for j in rank[:3]:
  b=info(j);b['cosine']=float(score[j]);b['difference_percent']=100*(b['climate_kgCO2e_kg']/a['climate_kgCO2e_kg']-1);alternatives.append(b)
 results.append({'source':a,'candidates':len(candidates),'semantic':alternatives,'lowest_climate':[info(j) for j in low[:3]]})
(P/'results.json').write_text(json.dumps({'products':len(rows),'examples':results,'source':source,'status':'prototype calculé, pertinence non évaluée indépendamment'},ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False,indent=2))
