# Et si l’IA — electricite

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

# Électricité — protocole avant calcul

Prévision pédagogique de la demande française à 24 heures avec consommation passée et calendrier. RTE éCO2mix consolidé, snapshot 2023–2026. Conserver observations réalisées demi-horaires, moyenne horaire seulement si deux observations valides. Index UTC régulier ; calendrier en Europe/Paris. Les révisions sont inconnues à l'origine : évaluation rétrospective, pas validation opérationnelle.

Apprentissage fixe 2023–2024 ; test 2025–dernière donnée. Entrées disponibles 24 heures avant cible : consommations retardées de 24, 48 et 168 heures, moyenne des 24 observations de t−47 à t−24, heure/jour de semaine/mois cycliques. Régression Ridge alpha=10 après standardisation sur apprentissage ; forêt 80 arbres profondeur 12 feuille minimale 20 graine 42. Comparateurs : même heure veille/semaine précédente. RTE J−1 comparateur externe séparé, jamais variable. Pas de météo disponible dans le prototype. Aucun réglage après lecture des scores.

MAE en MW sur mêmes observations, par année et sur pointes définies par seuil 90e percentile de l'apprentissage. Modèles fixes sans réentraînement. Ne mesure pas facture, CO2 marginal ou effet d'un décalage de consommation.

