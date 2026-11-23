# Et si l’IA — agribalyse

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
Le recalcul lit la révision du modèle dans le dossier voisin rappelconso : conserver les dossiers du dépôt ensemble.

## Fichiers

- PROTOCOL.md : question, périmètre, comparateurs, choix avant calcul et corrections exploratoires éventuelles.
- data/ : données gelées et source, empreintes dans manifest.json.
- run.py : calcul de l’expérience.
- results.json : mesures et effectifs ; predictions.csv lorsqu’une cible est prévue.
- verify.py : contrôles de cohérence et de métriques sur les résultats.

## Droits et source

Données : licence indiquée dans data/source.json, attribution au producteur et date requises. Code : MIT. Les illustrations du site ne sont pas incluses dans ce dossier de données. Les modèles préentraînés éventuels sont identifiés dans data/model.json, licence Apache2.0. Recherche et code assistés par IA.

## Périmètre exact

# AGRIBALYSE — protocole avant classement

Prototype de suggestions : l’IA rapproche les noms d’aliments, puis un filtre déterministe conserve les produits du même sous-groupe ayant un indicateur changement climatique inférieur. Le modèle ne calcule pas l’ACV, ne déduit ni nutrition ni allergènes et ne garantit pas une substitution acceptable. Comparaison à un tri du même sous-groupe par seul impact climatique.

Six points de départ fixés avant calcul : lasagnes viande (25081), couscous mouton (25029), hamburger (25413), sauce bolognaise (11114), pizza viande (25457), chili con carne (25111). Encodeur multilingue MiniLM, noms français seulement, similarité cosinus. Exclure même Code_AGB, sélectionner trois plus proches parmi candidats impact strictement inférieur du même sous-groupe. Présenter impacts exacts en kg CO2e/kg de produit et DQR. Ne pas comparer 1 kg cru à 1 kg cuit comme portions équivalentes. Pas d’entraînement, de mesure d’économies réalisées ni de score de pertinence humain inventé.

Test de cohérence uniquement : identifiants distincts, sous-groupe identique, impact source strictement plus élevé, calcul de variation exact. Examen éditorial des 18 suggestions après génération ; refus possibles conservés. Cette expérience est un prototype calculé, pas une évaluation de qualité de substitution.

