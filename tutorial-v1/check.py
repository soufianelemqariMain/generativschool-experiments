"""Comparaison appariée, contrôles de contrat et intégration CLI, sans réseau."""
import argparse
import hashlib
import importlib.util
import json
import platform
import resource
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
import app
import model_adapter
import retrieval
ROOT = Path(__file__).resolve().parent

def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def main():
    resource.setrlimit(resource.RLIMIT_CPU, (60,60))
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    start = time.perf_counter()
    cpu = time.process_time()
    frozen = json.loads((ROOT/'historical/freeze.json').read_text())
    for name, digest in frozen['sha256'].items():
        assert hashlib.sha256((ROOT/'historical'/name).read_bytes()).hexdigest() == digest
    docs = retrieval.atlas.load(ROOT/'historical/corpus.json')
    rows = []
    for q in json.loads((ROOT/'historical/questions.json').read_text()):
        row = dict(case=q)
        for name, search in [('baseline',retrieval.atlas.search), ('improved',retrieval.search)]:
            r = search(docs, q['query'], q['level'])
            ids = [h['id'] for h in r['hits']]
            passed = bool(ids) and ids[0] in q['expected'] if q['expected'] else not ids
            row[name] = dict(passed=passed, result=r)
        rows.append(row)
    save(args.out/'comparison.json', rows)
    controls = []
    for field, value in [('text_sha256','0'*64), ('license','restricted')]:
        data = json.loads((ROOT/'historical/corpus.json').read_text())
        data['documents'][0][field] = value
        invalid = args.out/'invalid.json'
        save(invalid, data)
        try: retrieval.atlas.load(invalid)
        except ValueError: controls.append('rejet '+field)
        else: raise AssertionError(field)
        invalid.unlink()
    answer = app.run('suivi médian 7,6 ans')
    assert answer['statements'][0]['references'] == ['D01']
    assert model_adapter.validate_selection('{"references":["D01"]}',answer)[0]['text'] == docs[0]['text']
    for raw in ['{"references":["D99"]}', '{"references":["D01","D01"]}', '{"references":[],"text":"inventé"}', '{bad', '{"references":[1]}']:
        try: model_adapter.validate_selection(raw, answer)
        except (ValueError, TypeError): pass
        else: raise AssertionError(raw)
    controls.append('contrat modèle : référence valide, inconnue, doublon, texte inventé, JSON et type invalides')
    assert not model_adapter.validate_selection('{"references":[]}', app.run('astronomie Saturne'))
    for row in rows:
        for h in row['improved']['result']['hits']:
            assert h['original_quote'] is False
            assert row['case']['level'] is None or h['evidence_level']==row['case']['level']
    for query, label, expected in [('suivi médian 7,6 ans','sourced','extraits_documentaires'),('astronomie Saturne','abstention','abstention')]:
        command = [sys.executable,'-B',str(ROOT/'app.py'),query,'--html',str(args.out/(label+'.html'))]
        run = subprocess.run(command, capture_output=True, text=True, check=True, timeout=10)
        data = json.loads(run.stdout)
        assert data['status'] == expected
        save(args.out/(label+'.json'),data)
    interactive = subprocess.run([sys.executable,'-B',str(ROOT/'app.py')], input='astronomie Saturne\n', capture_output=True, text=True, check=True, timeout=10)
    (args.out/'interactive.txt').write_text(interactive.stdout, encoding='utf-8')
    invalid = subprocess.run([sys.executable,'-B',str(ROOT/'app.py'),''],capture_output=True,text=True,timeout=10)
    assert invalid.returncode == 2
    xss = app.run('<script>alert(1)</script>')
    assert '<script>' not in retrieval.atlas.render(xss['search'])
    controls += ['CLI argument et invite interactive','sortie HTML et échappement','requête vide rejetée','filtres exacts','empreintes historiques vérifiées']
    save(args.out/'controls.json',controls)
    usage = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    summary = dict(utc=datetime.now(timezone.utc).isoformat(), python=sys.version,
        platform=platform.platform(), machine=platform.machine(),
        baseline=sum(r['baseline']['passed'] for r in rows), improved=sum(r['improved']['passed'] for r in rows),
        total=len(rows), improved_failures=[r['case']['id'] for r in rows if not r['improved']['passed']],
        wall_seconds=time.perf_counter()-start, cpu_self_seconds=time.process_time()-cpu,
        cpu_children_seconds=children.ru_utime+children.ru_stime,
        peak_rss_bytes=usage.ru_maxrss if sys.platform=='darwin' else usage.ru_maxrss*1024,
        ai_executed=False, torch_available=importlib.util.find_spec('torch') is not None,
        transformers_available=importlib.util.find_spec('transformers') is not None)
    save(args.out/'execution.json',summary)
    print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__': main()
