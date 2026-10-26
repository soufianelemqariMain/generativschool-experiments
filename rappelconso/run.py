"""Run frozen retrieval comparison. First run downloads public model weights; replay is offline."""
import json,hashlib,time,sys,importlib.metadata
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
P=Path(__file__).resolve().parent
raw=(P/'data/snapshot.json').read_bytes();source=json.loads((P/'data/source.json').read_text());assert hashlib.sha256(raw).hexdigest()==source['sha256']
rows=json.loads(raw);latest={}
for r in rows:
 key=r['numero_fiche'];v=str(r.get('numero_version') or '0')
 if key not in latest or int(v)>int(latest[key].get('numero_version') or 0):latest[key]=r
rows=list(latest.values());ids=[r['numero_fiche'] for r in rows]
fields=['libelle','marque_produit','categorie_produit','sous_categorie_produit','modeles_ou_references','conditionnements']
docs=['. '.join(str(r.get(k) or '').replace('¤',', ') for k in fields) for r in rows]
queries=json.loads((P/'queries.json').read_text());assert all(q['target'] in ids for q in queries)
texts=[q['query'] for q in queries];scores={}
for name,analyzer,ngram in [('mots','word',(1,2)),('caracteres','char_wb',(3,5))]:
 v=TfidfVectorizer(analyzer=analyzer,ngram_range=ngram,strip_accents='unicode');matrix=v.fit_transform(docs);scores[name]=(v.transform(texts)@matrix.T).toarray()
cache=P/'data/embeddings.npz';fingerprint=hashlib.sha256(json.dumps([docs,texts],ensure_ascii=False).encode()).hexdigest()
if '--encode' in sys.argv:
 from sentence_transformers import SentenceTransformer
 from huggingface_hub import model_info
 import torch
 torch.set_num_threads(4)
 model_id='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2';revision=json.loads((P/'data/model.json').read_text())['revision'] if (P/'data/model.json').exists() else model_info(model_id).sha;model=SentenceTransformer(model_id,revision=revision,device='cpu')
 start=time.time();a=model.encode(docs,batch_size=32,normalize_embeddings=True,show_progress_bar=True);b=model.encode(texts,normalize_embeddings=True)
 np.savez_compressed(cache,documents=a,queries=b,fingerprint=fingerprint)
 (P/'data/model.json').write_text(json.dumps({'id':model_id,'revision':revision,'license':'Apache-2.0','dimensions':a.shape[1],'seconds':time.time()-start,'max_sequence_length':model.max_seq_length,'fingerprint':fingerprint},indent=2))
e=np.load(cache);assert str(e['fingerprint'])==fingerprint;scores['semantique']=e['queries']@e['documents'].T
results={};details=[]
for name,score in scores.items():
 ranks=[]
 for q,line in zip(queries,score):
  order=np.argsort(-line,kind='stable');rank=int(np.where(order==ids.index(q['target']))[0][0])+1;ranks.append(rank)
  details.append({**q,'method':name,'rank':rank,'top5':[{'id':ids[int(i)],'label':rows[int(i)]['libelle'],'url':rows[int(i)]['lien_vers_la_fiche_rappel'],'score':float(line[i])} for i in order[:5]]})
 results[name]={'top1':sum(x==1 for x in ranks),'top5':sum(x<=5 for x in ranks),'total':len(ranks),'mrr':float(np.mean([1/x for x in ranks])),'by_form':{f:{'top1':sum(rank==1 for q,rank in zip(queries,ranks) if q['form']==f),'top5':sum(rank<=5 for q,rank in zip(queries,ranks) if q['form']==f),'total':sum(q['form']==f for q in queries)} for f in ['proche','reformulee']}}
output={'corpus_size':len(rows),'raw_rows':len(json.loads(raw)),'source':source,'results':results,'details':details,'versions':{k:importlib.metadata.version(k) for k in ['numpy','scikit-learn']}}
(P/'results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2));print(json.dumps(results,indent=2))
