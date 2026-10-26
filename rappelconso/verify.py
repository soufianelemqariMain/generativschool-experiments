import json, hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
r=json.loads((p/'results.json').read_text())
assert hashlib.sha256((p/'data/snapshot.json').read_bytes()).hexdigest()==r['source']['sha256']
q=json.loads((p/'queries.json').read_text())
assert len(q)==24 and len({x['target'] for x in q})==12
for method, expected in r['results'].items():
 d=[x for x in r['details'] if x['method']==method]
 assert len(d)==24
 assert sum(x['rank']==1 for x in d)==expected['top1']
 assert sum(x['rank']<=5 for x in d)==expected['top5']
 assert all(len(x['top5'])==5 and len({y['id'] for y in x['top5']})==5 for x in d)
 assert all((x['rank']==1)==(x['target']==x['top5'][0]['id']) for x in d)
print('OK — empreinte, 24 requêtes, 12 cibles, classements et métriques cohérents.')
