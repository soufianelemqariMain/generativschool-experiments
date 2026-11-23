# Comparer une présence, pas inventer un accès

Une distance entre profils binaires fictifs. Ce voisinage prépare une typologie, il ne mesure pas la qualité de vie.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Encoder trois équipements

L’ordre des colonnes doit rester identique : école, pharmacie, bibliothèque.

## Compter les différences

La distance de Hamming compte les colonnes différentes. Ici les trois équipements ont le même poids, un choix discutable.

## Ouvrir la comparaison

Deux communes à distance un peuvent différer sur des équipements très différents. On garde les profils lisibles.

## À essayer

Donnez un poids de trois à la pharmacie : le voisinage change. Le choix des variables porte une vision des besoins.

## Passage aux données réelles

La BPE réelle fournit des présences d’équipements. Toute typologie doit être évaluée sans la présenter comme une mesure complète d’accessibilité.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
