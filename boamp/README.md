# Et si l’IA — boamp

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

Les vecteurs sont fournis pour rejouer hors ligne. Pour les recalculer : installer requirements-encode.txt puis `python run.py --encode`. Les poids publics nécessitent Internet ; aucune API payante. La révision enregistrée est utilisée.

## Fichiers

- PROTOCOL.md : question, périmètre, comparateurs, choix avant calcul et corrections exploratoires éventuelles.
- data/ : données gelées et source, empreintes dans manifest.json.
- run.py : calcul de l’expérience.
- results.json : mesures et effectifs ; predictions.csv lorsqu’une cible est prévue.
- verify.py : contrôles de cohérence et de métriques sur les résultats.

## Droits et source

Données : licence indiquée dans data/source.json, attribution au producteur et date requises. Code : MIT. Les illustrations du site ne sont pas incluses dans ce dossier de données. Les modèles préentraînés éventuels sont identifiés dans data/model.json, licence Apache2.0. Recherche et code assistés par IA.

## Périmètre exact

# BOAMP — protocole avant classement

100 avis récents à la date du prélèvement, sans filtre de disponibilité. 24 requêtes, 12 cibles choisies pour diversité avant calcul. Une requête reprend l’objet, l’autre reformule un besoin. Panel éditorial non indépendant, non représentatif. Les avis peuvent être clos ou attribués : aucun résultat ne constitue une opportunité active vérifiée.

Indexer uniquement objet et descripteur_libelle, pas acheteur ni date. Comparer TF-IDF mots et caractères au même modèle multilingue MiniLM que RappelConso, révision gelée. Pas d’ajustement après résultats. Mesure de retrouvaille de cible au rang 1 et dans top 5, pas rappel exhaustif ni attribution de marchés. Le modèle aide à retrouver, pas à juger éligibilité, échéance, capacité ou chances de gain.

