# Retrouver une fiche RappelConso avec ses propres mots

Prototype éditorial Et si l’IA — Soufiane Lemqari, 26 octobre 2026.

Le programme compare TF-IDF mots, TF-IDF caractères et un encodeur multilingue préentraîné. Il classe les mêmes 1 000 fiches pour 24 descriptions de 12 produits. Le protocole est dans PROTOCOL.md et chaque classement dans results.json. Les requêtes ont été écrites avant le classement, mais ne sont ni représentatives ni indépendantes.

## Rejouer sans API

Python 3.12 utilisé, macOS ARM64. Dans ce dossier :

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
python verify.py
```

L’installation a besoin d’Internet ; le calcul utilise ensuite les vecteurs gelés fournis. Sous Windows, activer `.venv\Scripts\activate` (non testé ici).

## Recalculer les vecteurs

```sh
python -m pip install -r requirements-encode.txt
python run.py --encode
```

Télécharge des poids publics Hugging Face, sans service payant. La révision est enregistrée dans data/model.json. Le modèle est généraliste ; nous ne l’avons pas entraîné sur les rappels. Sa fenêtre est de 128 tokens : de longues fiches peuvent être tronquées. Pour changer les requêtes, il faut recalculer les vecteurs. `fetch.py` remplace le corpus par les 1 000 fiches les plus récentes : ce nouveau prélèvement ne reproduira plus le test d’octobre. Préserver l’archive originale.

## Résultat et interprétation

Sur 24 recherches, la cible arrive en premier 17 fois avec les mots, 18 avec les caractères et 12 avec le modèle sémantique. Le modèle généraliste ne gagne pas ce test. Une référence exacte compte énormément. Les scores de similarité ne sont pas des probabilités de danger.

## Données, licence, responsabilité

Source : DGCCRF et partenaires, RappelConso, via data.economie.gouv.fr. URLs, horodatage et SHA-256 dans data/source.json. Réutilisation sous Licence Ouverte 2.0 ; citer la source et la date. Les vecteurs dérivent des descriptions de produits. Modèle `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, Apache-2.0. Code de cette expérience : MIT, copyright 2026 Soufiane Lemqari (voir LICENSE).

Il s’agit d’une archive de recherche, pas d’une liste actuelle de rappels ni d’un service de sécurité. Vérifier les identifiants, les lots, les dates et les consignes sur la fiche officielle. Aucune absence de résultat ne prouve qu’un produit est sûr. Pas de données personnelles de lecteurs.
