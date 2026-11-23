# Et si l’IA — bpe

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

# BPE — protocole avant regroupement

Regrouper des communes selon leurs profils de présence d’équipements en 2025. Utiliser le fichier INSEE d’évolution harmonisé 2015/2020/2025, géographie 2026 ; retenir COM et 2025, observation A, 0/1. Ne pas confondre cette sélection harmonisée d’équipements avec toute la BPE. Le nombre d’équipements et la population ne sont pas présents : aucun classement de sous-équipement ou de désertification justifié.

Matrice communes × types, conserver uniquement types renseignés pour au moins 95 % des communes ; exclure communes ayant une absence d’observation parmi ces types. KMeans 6 groupes n_init=10 random_state=42 ; refaire graine 7 sans ajuster. Distance euclidienne sur présence binaire, sans normalisation qui surpondérerait raretés. Mesurer stabilité ARI entre graines et silhouette sur échantillon 2000 graine42 ; comparaison aux 6 quantiles du simple nombre de types présents. Aucun score de qualité d'un service ni causalité.

La démonstration illustre un apprentissage non supervisé. Interpréter groupes par fréquences, pas par jugement politique. Ajouter ensuite population, distances et capacité avant toute décision publique. Publier centres et comptes, pas une liste de communes « oubliées ».

## Correction après inspection du premier essai
La règle de complétude ne conservait qu’un type et produisait deux profils distincts : essai dégénéré, résultats archivés et rejetés, pas une réussite. Le fichier est publié sous forme creuse. Nouvelle question : regrouper les types explicitement signalés présents, sans convertir les entrées absentes en preuves d’absence réelle. Encoder 1 uniquement si observation=1, 0 signifiant « pas de présence listée » ; retirer colonnes et lignes sans aucun 1. Aucun jugement de manque de service n’en découle. Les métriques du deuxième essai sont exploratoires après cette correction, non une validation indépendante.

