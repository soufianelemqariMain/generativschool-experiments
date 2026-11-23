# Faire entrer les trajets dans la tournée

Un petit calcul de planning ; il met en évidence la contrainte avant une éventuelle optimisation et une estimation des durées.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Écrire les visites et déplacements

L’ordre est déjà fixé ici. On ne prétend pas résoudre un problème de tournée.

## Construire une chronologie

Chaque déplacement décale la visite suivante. Les durées sont des hypothèses, pas des mesures routières.

## Comparer au temps disponible

Trois heures de soin ne tiennent pas en trois heures de travail lorsque les déplacements sont nécessaires.

## À essayer

Ajoutez une pause de dix minutes. Ne la cachez pas dans une durée de visite artificiellement raccourcie.

## Passage aux données réelles

Les durées peuvent être prédites à partir d’historiques ; l’optimisation doit respecter pauses, compétences, horaires et continuité des intervenants.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
