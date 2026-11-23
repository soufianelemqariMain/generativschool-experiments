# Préparer la prévention routière avec des historiques publics

Prototype pédagogique évalué : prévoir les volumes départementaux mensuels d'accidents corporels enregistrés, pas le risque d'un individu ni le prochain accident. Métropole uniquement.

## Rejouer sans réseau après installation

Python 3.12 recommandé.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
python verify.py
```

`data/monthly.csv` contient les effectifs mensuels agrégés : année, mois, département, accidents. Aucun nom, adresse ou fiche de victime. Le fichier annuel de 2024 est volontairement exclu : il n'était pas publié à l'origine simulée de la prévision (janvier 2025). Les entrées du test viennent au plus tard de 2023.

`PROTOCOL.md` détaille la question, les paramètres figés et les limites avant calcul. `results.json`, `predictions.csv` et `department-errors.csv` sont régénérés. `verify.py` recalcule les métriques et vérifie que changer les réponses futures ne change pas les variables d'entrée. De très petites différences d'arrondi peuvent survenir entre environnements.

## Reconstituer l'agrégat

`data/source.json` référence chaque CSV officiel, son empreinte et sa date de récupération. Téléchargez chaque fichier sous `2010.csv`, etc., dans un répertoire séparé, puis `python prepare.py /chemin/vers/les/csv`. Le script contrôle les empreintes et les identifiants uniques avant agrégation. Les anciennes modalités de département (010, 201, 202) deviennent 01, 2A et 2B.

Source : ONISR / BAAC, data.gouv.fr, Licence Ouverte. Les sources individuelles ne sont pas redistribuées dans ce dossier. Les extractions restent sous les conditions de la source ; le code de ce dossier est MIT. Données téléchargées le 23 novembre 2026. Archives révisées, pas une reconstruction parfaite des versions historiques. Pas d'évaluation de l'effet causal d'une politique de prévention.
