# Faire pousser un premier arbre de prix

Un arbre de régression à une seule question, appris sur six observations inventées. Il explique une brique possible de la forêt, pas une prévision Insee.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Lire six couples de mois

x est la variation déjà connue ; y la variation du mois suivant, en %. Les deux dernières lignes restent hors de l’apprentissage.

## Laisser les exemples choisir la question

Chaque seuil coupe le passé en deux groupes. La moyenne de chaque groupe devient une feuille. On choisit le seuil dont la somme des erreurs au carré est la plus faible.

## Suivre une branche puis refaire le ticket

Avec une variation connue de 4 %, on suit la branche droite. L’arbre estime 5 % ; la recomposition du panier reste une multiplication. Le test porte sur deux exemples distincts, trop peu pour conclure.

## À essayer

Ajoutez (3, 4) au passé, puis relancez : le seuil ou les feuilles changent-ils ? La question est apprise, elle n’est pas écrite à la main.

## Passage aux données réelles

Remplacer ces couples par des variations mensuelles publiées, avec leur date de disponibilité ; réserver plusieurs mois futurs et comparer à la variation inchangée. Une forêt agrégerait plusieurs arbres, pas les deux feuilles de celui-ci.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
