"""Passe mesurée, sans réglage ; sortie dans un répertoire neuf."""
import argparse, copy, hashlib, json, platform, resource, sys, time
from datetime import datetime, timezone
from pathlib import Path
import atlas
ROOT=Path(__file__).resolve().parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj): p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    a=argparse.ArgumentParser(); a.add_argument('--out',required=True); args=a.parse_args()
    out=Path(args.out); out.mkdir(exist_ok=False)
    wall=time.perf_counter(); cpu=time.process_time()
    freeze=json.loads((ROOT/'freeze.json').read_text())
    for name,digest in freeze['sha256'].items():
        if sha(ROOT/name)!=digest: raise ValueError('Fichier figé modifié : '+name)
    docs=atlas.load(ROOT/'corpus.json'); checks=[]
    for field,value in [('text_sha256','0'*64),('license','restricted')]:
        raw=json.loads((ROOT/'corpus.json').read_text()); raw['documents'][0][field]=value
        temp=out/'invalid.json'; save(temp,raw)
        try: atlas.load(temp)
        except ValueError: checks.append('rejet '+field)
        else: raise AssertionError('Entrée invalide acceptée')
        temp.unlink()
    results=[]
    for q in json.loads((ROOT/'questions.json').read_text()):
        t=time.perf_counter(); r=atlas.search(docs,q['query'],q['level']); elapsed=time.perf_counter()-t
        ids=[h['id'] for h in r['hits']]; expected=q['expected']
        rank=next((i for i,x in enumerate(ids,1) if x in expected),None)
        passed=(bool(ids) and ids[0] in expected) if expected else not ids
        for h in r['hits']:
            assert h['original_quote'] is False and 'quote' not in h
            assert q['level'] is None or h['evidence_level']==q['level']
        results.append(dict(case=q,result=r,passed=passed,first_relevant_rank=rank,recall_at_3=len(set(ids[:3])&set(expected))/len(expected) if expected else None,wall_seconds=elapsed))
    allcards=copy.deepcopy(results[0]['result']); allcards['query']='Catalogue des six cartes — pas une recherche'; allcards['status']='catalogue'
    allcards['hits']=[]
    for d in docs:
        h={k:d[k] for k in atlas.META}; h.update(original_quote=False,text_kind='reformulation_editoriale_fr'); allcards['hits'].append(h)
    page=atlas.render(allcards)
    for d in docs:
        for k in ('attribution','license','license_url','changes','url','text_sha256'):
            assert atlas.html.escape(d[k],quote=True) in page
    assert '<blockquote>' not in page and page.count('Reformulation éditoriale française')==6
    escaped=copy.deepcopy(allcards); escaped['hits'][0]['text']='<script>alert(1)</script>'
    assert '<script>' not in atlas.render(escaped)
    checks += ['attribution et licence 6/6 HTML et données','aucun blockquote ni champ quote','échappement HTML','filtres exacts','freeze vérifié']
    (out/'atlas.html').write_text(page,encoding='utf-8'); save(out/'cards.json',allcards)
    save(out/'queries.json',results); save(out/'controls.json',checks)
    usage=resource.getrusage(resource.RUSAGE_SELF)
    save(out/'execution.json',dict(utc=datetime.now(timezone.utc).isoformat(),python=sys.version,system=platform.system(),release=platform.release(),machine=platform.machine(),adapter=atlas.VERSION,engine=atlas.engine.VERSION,dependencies='Python standard library only',wall_seconds=time.perf_counter()-wall,cpu_seconds=time.process_time()-cpu,peak_rss_bytes=usage.ru_maxrss if sys.platform=='darwin' else usage.ru_maxrss*1024,passed=sum(r['passed'] for r in results),total=len(results),ai_executed=False,freeze_sha256=sha(ROOT/'freeze.json')))
    print(json.dumps({'passed':sum(r['passed'] for r in results),'total':len(results),'failed':[r['case']['id'] for r in results if not r['passed']]}))
if __name__=='__main__': main()
