"""Interface CLI : requête -> ingestion -> classement -> réponse référencée."""
import argparse
import json
from pathlib import Path
import retrieval
ROOT = Path(__file__).resolve().parent

def run(query, level=None):
    records = retrieval.atlas.load(ROOT/'historical/corpus.json')
    return retrieval.answer(retrieval.search(records, query, level))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('query', nargs='?')
    p.add_argument('--level', choices=retrieval.legacy.LEVELS)
    p.add_argument('--html', type=Path)
    args = p.parse_args()
    query = args.query if args.query is not None else input('Question documentaire > ')
    try:
        result = run(query, args.level)
    except ValueError as exc:
        p.error(str(exc))
    if args.html:
        page = retrieval.atlas.render(result['search'])
        page = page.replace('</h1>', '</h1><p>D06 est une réserve de la rédaction, pas une observation de Porro. GNT0003 n’est pas documenté dans ce corpus.</p>', 1)
        args.html.write_text(page, encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
