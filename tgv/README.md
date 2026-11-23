# Et si l’IA — tgv

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

Données et base dérivée : ODbL (attribution SNCF/AQST, partage sous ODbL). Code uniquement : MIT. Les illustrations du site ne sont pas incluses dans ce dossier de données. Les modèles préentraînés éventuels sont identifiés dans data/model.json, licence Apache2.0. Recherche et code assistés par IA.

## Périmètre exact

# TGV — protocole avant évaluation

Question : un modèle entraîné sur les historiques de régularité aide-t-il à anticiper la proportion de trains en retard à l’arrivée d’une liaison, mois par mois ? Pas la prédiction d’un train individuel.

Source : SNCF/AQST, régularité mensuelle par liaison, ODbL. Cible : 100 × trains en retard à l’arrivée / (trains prévus − annulations). Le seuil officiel dépend de la durée du trajet. Lignes nationales seulement. Retirer valeurs impossibles et doublons liaison/mois ; réindexer les mois pour que décalage signifie bien mois calendaire.

Modèle figé : RandomForestRegressor, 100 arbres, max_depth=8, min_samples_leaf=10, random_state=42, n_jobs=2. Variables : taux retardés de 2, 3 et 12 mois, moyenne des mois 2 à 7, mois cyclique, liaison encodée. Pas de causes, volumes ou retards du mois à prévoir. Délai de deux mois supposé ; archives révisées sans preuve de disponibilité historique.

Apprentissage jusqu’à décembre 2024, test de janvier 2025 à la dernière période disponible. Modèle fixe sans réentraînement. Comparateurs : même mois année précédente et dernier mois utilisable (M−2). Même panel complet pour tous. MAE en points de pourcentage, pondération égale par liaison/mois puis par nombre de trains réalisés ; ce dernier poids sert seulement à l’évaluation. Résultats par année. Pas de réglage après scores. Pas d’économie ou de fiabilité individuelle démontrée.

