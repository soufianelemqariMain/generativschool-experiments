#!/usr/bin/env python3
"""Atelier pédagogique hors ligne. Données fictives, aucune mesure de terrain.
Usage: python3 demo.py --input demo-input.json --output demo-results.json
Python 3.10+ ; bibliothèque standard uniquement ; pas de service externe.
"""
import argparse,json,math,re,statistics,unicodedata
from pathlib import Path

def tokens(text):
 text=''.join(c for c in unicodedata.normalize('NFD',text.lower()) if unicodedata.category(c)!='Mn')
 return re.findall(r'[a-z]+',text)
def mean(v):return sum(v)/len(v)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def distance(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def compute(d):
 f=d['family'];out={'status':'DEMONSTRATION_SUR_DONNEES_FICTIVES','family':f,'unit':d['unit']}
 if f=='regression':
  train=[r for r in d['rows'] if r['split']=='apprentissage'];test=[r for r in d['rows'] if r['split']=='test']
  xs=[r['x'] for r in train];ys=[r['y'] for r in train];xm,ym=mean(xs),mean(ys)
  a=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs);b=ym-a*xm
  pred=[dict(r,prediction=a*r['x']+b,baseline=ym) for r in test]
  out.update(a=a,b=b,rows=d['rows'],predictions=pred,baseline_value=ym,mae=mean([abs(r['prediction']-r['y']) for r in pred]),baseline_mae=mean([abs(r['baseline']-r['y']) for r in pred]),train_count=len(train),test_count=len(test))
 elif f=='retrieval':
  docs=d['documents'];vocab=sorted(set(t for r in docs for t in tokens(r['text'])))
  idf={t:math.log((1+len(docs))/(1+sum(t in tokens(r['text']) for r in docs)))+1 for t in vocab}
  def vector(s):
   ts=tokens(s);v=[ts.count(t)*idf[t] for t in vocab];norm=math.sqrt(dot(v,v));return [x/norm for x in v] if norm else v
  q=vector(d['query']);scores=sorted([dict(r,score=dot(q,vector(r['text']))) for r in docs],key=lambda r:(-r['score'],r['id']))
  out.update(query=d['query'],ranked=scores,vocabulary=vocab,idf=idf,algorithm='TF-IDF lexical, pas un encodeur sémantique')
 elif f=='anomaly':
  train=d['reference'];mu=[mean([r[j] for r in train]) for j in range(2)];sd=[statistics.pstdev([r[j] for r in train]) or 1 for j in range(2)]
  scores=[{'id':r['id'],'values':r['values'],'score':math.sqrt(sum(((x-m)/s)**2 for x,m,s in zip(r['values'],mu,sd)))} for r in d['cases']]
  out.update(mean=mu,sd=sd,ranked=sorted(scores,key=lambda r:-r['score']),algorithm='Distance standardisée de référence, pas Isolation Forest')
 elif f=='cluster':
  pts=d['points'];centers=[pts[0][:],pts[-1][:]]
  for _ in range(20):
   labels=[min(range(2),key=lambda k:distance(p,centers[k])) for p in pts]
   new=[[mean([p[j] for p,l in zip(pts,labels) if l==k]) for j in range(2)] for k in range(2)]
   if new==centers:break
   centers=new
  out.update(points=pts,labels=labels,centers=centers,algorithm='K-means à deux groupes sur exemples fictifs')
 elif f=='classification':
  a=b=0.;train=d['train'];
  def sigmoid(z):return 1/(1+math.exp(-max(-40,min(40,z))))
  for _ in range(2500):
   errors=[sigmoid(a*r['x']+b)-r['y'] for r in train]
   a-=.12*mean([e*r['x'] for e,r in zip(errors,train)]);b-=.12*mean(errors)
  preds=[dict(r,score=sigmoid(a*r['x']+b)) for r in d['test']]
  out.update(a=a,b=b,predictions=preds,algorithm='Régression logistique pédagogique ; score non calibré pour un risque réel')
 elif f=='vision':
  labels=sorted(set(r['label'] for r in d['train']));centers={l:[mean([r['rgb'][j] for r in d['train'] if r['label']==l]) for j in range(3)] for l in labels}
  mask=[min(labels,key=lambda l:distance(rgb,centers[l])) for rgb in d['pixels']]
  selected=[m for m,inside in zip(mask,d['inside']) if inside];n=sum(m=='vegetation' for m in selected)
  out.update(width=d['width'],height=d['height'],pixels=d['pixels'],mask=mask,inside=d['inside'],vegetation_pixels=n,inside_pixels=len(selected),fraction=n/len(selected),centers=centers,algorithm='Classification couleur par centre de classe appris ; pas un modèle satellite')
 elif f=='audio':
  # A computed spectrogram of a constructed chirp, not a bird recording.
  sr=8000;n=128;frames=32;bins=48;signal=[math.sin(2*math.pi*(500*t/sr+1000*(t/sr)**2)) for t in range(n*frames)]
  grid=[]
  for frame in range(frames):
   window=[signal[frame*n+i]*(.5-.5*math.cos(2*math.pi*i/(n-1))) for i in range(n)]
   row=[]
   for k in range(bins):
    real=sum(v*math.cos(2*math.pi*k*i/n) for i,v in enumerate(window));imag=sum(-v*math.sin(2*math.pi*k*i/n) for i,v in enumerate(window))
    row.append(math.log1p(real*real+imag*imag))
   grid.append(row)
  out.update(spectrogram=grid,sample_rate=sr,window=n,duration=len(signal)/sr,algorithm='Transformée de Fourier ; aucune identification d’espèce')
 else:raise ValueError(f)
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input',default='demo-input.json');p.add_argument('--output',default='demo-results.json');args=p.parse_args()
 result=compute(json.loads(Path(args.input).read_text()));Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('Démonstration fictive calculée → '+args.output)
