# Et si l’IA — lovac

Soufiane Lemqari — prototype pédagogique préparé le 26 octobre 2026. Les résultats ne constituent pas une validation indépendante ou un service opérationnel. Lire PROTOCOL.md avant interprétation.

## Rejouer

Python 3.12.14 utilisé sur macOS ARM64. Dans ce dossier :

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
python verify.py
```

Installation avec Internet, calcul sur données gelées ensuite. Sous Windows, activer `.venv\Scripts\activate` ; Windows non testé ici. Les résultats numériques peuvent varier légèrement selon plateforme. Aucune clé ni dépense de service requise.

## Fichiers

- PROTOCOL.md : question, périmètre, comparateurs, choix avant calcul et corrections exploratoires éventuelles.
- data/ : données gelées et source, empreintes dans manifest.json.
- run.py : calcul de l’expérience.
- results.json : mesures et effectifs ; predictions.csv lorsqu’une cible est prévue.
- verify.py : contrôles de cohérence et de métriques sur les résultats.

## Droits et source

Données : licence indiquée dans data/source.json, attribution au producteur et date requises. Code : MIT. Les illustrations du site ne sont pas incluses dans ce dossier de données. Les modèles préentraînés éventuels sont identifiés dans data/model.json, licence Apache2.0. Recherche et code assistés par IA.

## Périmètre exact

# LOVAC — protocole avant calcul

Prévoir le nombre communal de logements privés vacants au millésime suivant à partir de deux millésimes passés et du parc privé connu. Pas de localisation de logements, pas d’explication causale de vacance. Source LOVAC 2020–2026 en géographie 2026 ; données secrétisées « s » traitées comme manquantes, jamais comme zéro.

Exemples apprentissage : cibles 2023, 2024, 2025. Cible test 2026. Variables : vacance totale à y−1 et y−2, différence, parc privé FF de y−2 (ne pas utiliser le stock contemporain). Régression Ridge alpha=10 après standardisation ; forêt 100 arbres, profondeur 10, feuille 20, graine 42. Comparateur : vacance inchangée. Résultats MAE en logements par commune et médiane erreur absolue, par région. Aucun réglage après résultats. Même panel complet pour tous. Archives révisées et changement géographique empêchent une validation opérationnelle historique. Les petites communes secrétisées sont sous-représentées.

