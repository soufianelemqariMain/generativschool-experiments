# Et si l’IA — dvf

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

# DVF — protocole avant calcul

Pour éviter de publier des adresses de transactions, utiliser les statistiques DVF déjà agrégées par département et mois. Question : peut-on anticiper la médiane mensuelle du prix des maisons au m² à partir de son historique ? Une médiane départementale n’est pas l’estimation d’une maison et varie avec le type de biens vendus.

Garder échelle département, nb_ventes_maison >= 30 et médiane positive. Réindexer les mois, variables décalées de 6, 7 et 12 mois (délai simplifié de publication). Une publication réelle se fait par livraison et peut prendre davantage de temps : rétrospective seulement. Pas de volume contemporain en entrée. Apprentissage jusqu’en 2024, test 2025–dernière période. Forêt 100 arbres profondeur 8 min feuille 10 graine 42, département one-hot, saison cyclique. Comparateurs prix à M−6 et M−12. MAE en €/m², par année et pondérée par ventes en évaluation seulement. Aucun réglage après test. Pas de conseil financier ni valeur individuelle.


## Extrait compact

`data/departements.csv` est l’extrait départemental utilisé. Le fichier source complet de statistiques est exclu du téléchargement ; son URL et son empreinte restent dans les métadonnées. Le calcul ne nécessite pas le fichier complet.
