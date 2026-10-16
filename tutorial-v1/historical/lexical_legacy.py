"""Atlas documentaire local : sélection lexicale, aucune génération de réponse."""
import argparse
from datetime import date
import hashlib
import html
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit

VERSION = '0.1.0'
LEVELS = ('institutionnel', 'annonce', 'preclinique', 'clinique', 'revue')
STOP = set('le la les de des du un une et ou en au aux pour sur dans est il elle que qui quel quelle quels quelles a ce ces avec document documents'.split())

def tokens(text):
    text = ''.join(c for c in unicodedata.normalize('NFKD', text.lower()) if not unicodedata.combining(c))
    return set(re.findall(r'[a-z0-9]{2,}', text)) - STOP

def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def validate(records):
    if not isinstance(records, list):
        raise ValueError('Le corpus doit être une liste')
    ids = set()
    for r in records:
        for key in ('id', 'title', 'url', 'source_type', 'evidence_level', 'source_text', 'source_sha256'):
            if not isinstance(r.get(key), str) or not r[key].strip():
                raise ValueError('Champ manquant ou invalide : ' + key)
        if r['id'] in ids:
            raise ValueError('Identifiant dupliqué')
        ids.add(r['id'])
        if type(r.get('synthetic')) is not bool or r['evidence_level'] not in LEVELS:
            raise ValueError('Statut synthétique ou niveau invalide')
        url = urlsplit(r['url'])
        if url.scheme != 'https' or not url.hostname or url.username or url.password:
            raise ValueError('URL HTTPS publique attendue')
        for key in ('published_at', 'accessed_at'):
            value = r.get(key)
            if value is None and key == 'published_at':
                continue
            date.fromisoformat(value)
        if digest(r['source_text']) != r['source_sha256']:
            raise ValueError('Empreinte du texte incohérente')
        start, end = r.get('start'), r.get('end')
        if type(start) is not int or type(end) is not int or not 0 <= start < end <= len(r['source_text']):
            raise ValueError('Bornes de citation invalides')
    return records

def load(path):
    return validate(json.loads(Path(path).read_text(encoding='utf-8')))

def search(records, query, level=None, limit=5):
    validate(records)
    if level is not None and level not in LEVELS:
        raise ValueError('Niveau inconnu')
    if limit < 1:
        raise ValueError('Limite positive attendue')
    q = tokens(query)
    # Porte conservatrice, non-classificateur de sûreté : aucune conclusion médicale.
    blocked = q & {'efficacite', 'efficace', 'guerit', 'guerison', 'diagnostic', 'diagnostiquer', 'traiter', 'dose', 'sequence', 'vecteur'}
    hits = []
    if q and not blocked:
        for r in records:
            if level and r['evidence_level'] != level:
                continue
            quote = r['source_text'][r['start']:r['end']]
            overlap = q & tokens(quote)
            coverage = len(overlap) / len(q)
            if overlap and coverage >= 0.6:
                hits.append(dict(id=r['id'], title=r['title'], url=r['url'],
                    published_at=r['published_at'], accessed_at=r['accessed_at'],
                    source_type=r['source_type'], evidence_level=r['evidence_level'],
                    synthetic=r['synthetic'], quote=quote, start=r['start'], end=r['end'],
                    source_sha256=r['source_sha256'], lexical_coverage=round(coverage, 6)))
    hits.sort(key=lambda r: (-r['lexical_coverage'], r['id']))
    return {'engine': 'lexical-v' + VERSION, 'query': query, 'level_filter': level,
            'status': 'extraits_documentaires' if hits else 'abstention',
            'reason': 'Demande hors périmètre : aucune conclusion médicale ou conception biologique.' if blocked else
                      ('Correspondances lexicales ; elles ne constituent pas une réponse validée.' if hits else 'Aucun extrait suffisamment correspondant dans ce corpus.'),
            'hits': hits[:limit], 'ai_executed': False}

def render(result):
    esc = lambda value: html.escape(str(value), quote=True)
    cards = []
    for h in result['hits']:
        cards.append('<article><h2>' + esc(h['title']) + '</h2><p>' +
            ('SYNTHÉTIQUE — aucun fait biologique' if h['synthetic'] else 'Source importée — interprétation humaine requise') +
            '</p><blockquote>' + esc(h['quote']) + '</blockquote><p>Niveau : ' + esc(h['evidence_level']) +
            ' · Type : ' + esc(h['source_type']) + '</p><p>Publication : ' + esc(h['published_at']) +
            ' · Consultation : ' + esc(h['accessed_at']) + '</p><a href="' + esc(h['url']) + '">' + esc(h['url']) +
            '</a><p>Référence : ' + esc(h['id']) + ' · Caractères [' + str(h['start']) + ', ' + str(h['end']) +
            '[ · SHA-256 : ' + esc(h['source_sha256']) + '</p></article>')
    return '<!doctype html><html lang="fr"><meta charset="utf-8"><title>Atlas — export local</title><style>body{max-width:850px;margin:3rem auto;padding:1rem;font:18px system-ui;line-height:1.6}article{border-top:1px solid #aaa;margin-top:2rem}p,a{overflow-wrap:anywhere}</style><h1>Atlas de preuves — prototype local</h1><p>Recherche lexicale. IA non exécutée. Aucun avis médical.</p><p>Requête : ' + esc(result['query']) + '</p><p>' + esc(result['status']) + ' — ' + esc(result['reason']) + '</p>' + ''.join(cards) + '</html>'

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('corpus', type=Path)
    p.add_argument('query')
    p.add_argument('--level', choices=LEVELS)
    p.add_argument('--html', type=Path)
    args = p.parse_args()
    result = search(load(args.corpus), args.query, args.level)
    if args.html:
        args.html.write_text(render(result), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
