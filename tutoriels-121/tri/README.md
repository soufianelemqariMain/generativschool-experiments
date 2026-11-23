# Reconnaître l’objet ne décide pas de son avenir

Une table de décision après une reconnaissance supposée. Les règles de filière doivent être vérifiées localement.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Décrire l’état en plus de l’objet

Deux objets identiques peuvent avoir des parcours différents selon qu’ils fonctionnent ou sont réparables.

## Séparer les embranchements

La reconnaissance d’image fournirait une catégorie ; ces règles traitent l’état, qui ne se déduit pas toujours de la photo.

## Conserver le diagnostic manquant

Un objet non fonctionnel sans diagnostic doit rester dans une branche inconnue.

## À essayer

Ajoutez une photo sans information de fonctionnement : le programme ne peut pas conclure à une réparation possible.

## Passage aux données réelles

Un classifieur d’objets doit être testé sur des images distinctes ; la recommandation finale nécessite des règles de filière et des informations de diagnostic.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
