"""Normalisation pédagogique 1.1.0 ; aucun modèle exécuté."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'historical'))
import atlas
import lexical_legacy as legacy
VERSION = '1.1.0'
# Dictionnaire de développement explicite, pas un encodeur sémantique.
ALIASES = {'plaquettes': 'plaquettaire', 'corrigees': 'correction',
           'etude': 'publication'}
GRAMMAR = {'sont', 'elles', 'elle', 'il', 'ils'}

def normalize(text):
    return {ALIASES.get(t, t) for t in legacy.tokens(text) - GRAMMAR}

def search(records, query, level=None):
    if not isinstance(query, str) or not query.strip() or len(query) > 2000:
        raise ValueError('Requête attendue : 1 à 2000 caractères')
    if level is not None and level not in legacy.LEVELS:
        raise ValueError('Niveau inconnu')
    # La porte historique reste prioritaire.
    baseline = atlas.search(records, query, level)
    q = normalize(query)
    blocked = legacy.tokens(query) & {'efficacite','efficace','guerit','guerison','diagnostic','diagnostiquer','traiter','dose','sequence','vecteur'}
    hits = []
    if q and not blocked:
        for d in records:
            if level and d['evidence_level'] != level:
                continue
            overlap = q & normalize(d['text'])
            score = len(overlap) / len(q)
            if overlap and score >= .6:
                h = {k: d[k] for k in atlas.META}
                h.update(original_quote=False, text_kind='reformulation_editoriale_fr',
                         lexical_coverage=round(score, 6), matched_terms=sorted(overlap),
                         editorial_reservation=d['id']=='D06')
                hits.append(h)
    hits.sort(key=lambda h: (-h['lexical_coverage'], h['id']))
    baseline.update(engine='normalized-lexical-'+VERSION, hits=hits[:6],
                    status='extraits_documentaires' if hits else 'abstention',
                    normalized_query=sorted(q))
    if not blocked:
        baseline['reason'] = 'Correspondances lexicales normalisées ; pas une réponse validée.' if hits else 'Aucune carte suffisamment correspondante.'
    return baseline

def answer(result):
    # Assemblage déterministe : aucune phrase factuelle nouvelle.
    return dict(schema_version='1.0', status=result['status'], ai_executed=False,
                query=result['query'], reason=result['reason'],
                statements=[dict(text=h['text'], references=[h['id']],
                                 editorial_reservation=h['id']=='D06') for h in result['hits']],
                evidence=result['hits'], search=result)
