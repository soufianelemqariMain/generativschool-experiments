# Et si l’IA — dpe

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

# DPE — protocole avant calcul

Prototype d’estimation d’une consommation conventionnelle du diagnostic, pas facture réelle ni effet causal de travaux. Échantillon de 10 000 lignes fourni par l’API ADEME, non représentatif. Types maison et appartement seulement ; cible énergie primaire en kWh EP/m²/an, positive <= 1500. Exclure immeubles et adresse BAN manquante. Le code d’adresse sert uniquement à tenir les bâtiments à l’écart entre ensembles.

Apprentissage : diagnostics établis avant 2025. Test : 2025 et après ; exclure les adresses BAN déjà vues dans apprentissage et ne garder qu’un diagnostic par adresse dans le test. Ce regroupement est imparfait (adresse n’est pas identifiant physique de bâtiment). Variables : surface du logement, type, période de construction, énergie principale de chauffage, climat, altitude, qualités d’isolation des murs et menuiseries. Pas de consommation partielle, coûts, étiquette ou déperditions calculées. Les qualités d’isolation supposent un diagnostic déjà disponible, ce n’est pas une estimation à partir d’une simple annonce immobilière.

Comparateur : médiane d’apprentissage par maison/appartement. Forêt 100 arbres, profondeur 10, feuille minimale 10, graine 42. Imputation médiane entraînement pour surface ; catégories manquantes explicites ; one-hot. MAE en kWh EP/m²/an, par type. Réformes et biais du parc diagnostiqué limitent la portée, aucune décision de rénovation automatique. Pas d’ajustement après résultats.

