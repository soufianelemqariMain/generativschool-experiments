# Croiser deux masques avant de compter

Un masque de végétation déjà fourni et une limite de cour fictive. Le code ne réalise pas de reconnaissance d’image.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Distinguer végétation et périmètre

Les matrices 4 × 4 sont alignées pixel par pixel. Un arbre hors cour ne doit pas gonfler la part végétalisée.

## Intersecter les deux masques

Un pixel est compté seulement si les deux valeurs valent un. Les deux produits doivent partager la même géométrie.

## Passer à une proportion

Un pixel sur quatre représente 25 % de cette grille. Cela ne mesure ni ombre, ni fraîcheur, ni usage réel.

## À essayer

Ajoutez de la végétation hors de la cour : le résultat doit rester identique. Déplacez ensuite le masque de cour pour voir le risque de désalignement.

## Passage aux données réelles

Un modèle de segmentation produirait le premier masque ; les limites de cour et la validation sur le terrain sont deux tâches distinctes.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
