# Et si l’IA — eau

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

# Eau — protocole avant calcul

SISPEA eau potable 2024, OFB. Illustration d’une détection de profils atypiques, pas localisation de fuite. Variables : rendement P104.3 (%), pertes P106.3 (m³/km/j), abonnés VP.056, longueur VP.077 (km). Garder services distributeurs, quatre valeurs numériques, rendement 0–100, pertes >=0, abonnés et longueur >0. Exclure avis de vérification négatif s’ils sont identifiables et documenter les valeurs. Pas de noms de gestionnaires privés ou contacts publiés.

IsolationForest 200 arbres, contamination .05 (quota choisi, pas fréquence réelle des anomalies), random_state=42. StandardScaler et log1p pour pertes, abonnés, longueur. Refaire graine7, mesurer recouvrement des 5% les plus atypiques ; comparer au même nombre de plus faibles rendements. Pas de vérité terrain : ne pas produire précision/rappel ni parler de fraude ou mauvaise gestion. Statistiques globales et exemples anonymisés. Un grand service peut être atypique sans être défaillant. Données manquantes, déclaratives et performances historiques limitent la portée.


## Extrait de publication

`data/entrees.csv` contient uniquement les quatre variables numériques des 7 791 services retenus, dans l’ordre de la source. Aucun nom, adresse ni contact de service n’est distribué. `data/extraction.json` conserve les effectifs, les statuts et l’empreinte du ZIP source. Le calcul repart de cet extrait : le ZIP complet de SISPEA n’est pas nécessaire.
