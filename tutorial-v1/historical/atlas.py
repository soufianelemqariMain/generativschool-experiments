"""Adaptateur éditorial 1.0 : réutilise le classement lexical 0.1.0 inchangé."""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlsplit
import lexical_legacy as engine
VERSION = '1.0.0'
META = ('id','source_id','title','text','disease','evidence_level','published_at','accessed_at','url','locator','attribution','license','license_url','changes','text_sha256')

def load(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    docs = data['documents']
    records = []
    for d in docs:
        if any(not isinstance(d.get(k), str) or not d[k].strip() for k in META):
            raise ValueError('Métadonnée éditoriale manquante')
        if d['license'] != 'CC-BY-4.0' or d['license_url'] != 'https://creativecommons.org/licenses/by/4.0/':
            raise ValueError('Licence non admise')
        if engine.digest(d['text']) != d['text_sha256']:
            raise ValueError('Intégrité locale du texte invalide, pas validation de source')
        records.append(dict(d, source_text=d['text'], source_sha256=d['text_sha256'], start=0, end=len(d['text']), synthetic=False, source_type='reformulation_editoriale'))
    engine.validate(records)
    return records

def search(records, query, level=None):
    result = engine.search(records, query, level, limit=6)
    lookup = {d['id']: d for d in records}
    result['adapter_version'] = VERSION
    result['integrity_scope'] = 'SHA local : intégrité des cartes uniquement ; aucune authentification de source'
    for hit in result['hits']:
        d = lookup[hit['id']]
        for k in ('quote','start','end','source_sha256'):
            del hit[k]
        hit.update({k: d[k] for k in META})
        hit['text_kind'] = 'reformulation_editoriale_fr'
        hit['original_quote'] = False
    return result

def render(result):
    e = lambda x: html.escape(str(x), quote=True)
    cards = []
    for h in result['hits']:
        cards.append('<article><h2>'+e(h['id']+' — '+h['title'])+'</h2><p><strong>Reformulation éditoriale française — pas une citation originale</strong></p><p>'+e(h['text'])+'</p><p>Attribution : '+e(h['attribution'])+' · Source : '+e(h['source_id'])+'</p><a href="'+e(h['url'])+'">Publication originale</a><p>Repère : '+e(h['locator'])+' · Niveau : '+e(h['evidence_level'])+'</p><p>Publication : '+e(h['published_at'])+' · Consultation : '+e(h['accessed_at'])+'</p><a href="'+e(h['license_url'])+'">'+e(h['license'])+'</a><p>Changements : '+e(h['changes'])+'</p><p>SHA-256 du texte local : '+e(h['text_sha256'])+'</p></article>')
    return '<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Atlas documentaire — prototype limité</title><style>body{max-width:850px;margin:2rem auto;padding:1rem;font:17px system-ui;line-height:1.6}article{border-top:1px solid #aaa}p{overflow-wrap:anywhere}</style><h1>Atlas documentaire — prototype limité</h1><p>Deux publications, six cartes. Recherche lexicale, aucune IA exécutée. Aucun avis médical ni résultat biologique nouveau.</p><p>Les empreintes contrôlent les fichiers locaux ; elles ne valident pas les sources.</p><p>'+e(result['query'])+' — '+e(result['status'])+'</p>'+''.join(cards)+'</html>'

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('corpus'); p.add_argument('query'); p.add_argument('--level', choices=engine.LEVELS); p.add_argument('--html')
    a=p.parse_args(); r=search(load(a.corpus),a.query,a.level)
    if a.html: Path(a.html).write_text(render(r),encoding='utf-8')
    print(json.dumps(r,ensure_ascii=False,indent=2))
