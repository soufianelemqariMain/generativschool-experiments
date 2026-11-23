# Choisir un seuil sans cacher les alertes manquées

Un test de seuil sur six scores fictifs. Les scores sont fournis, pas appris ; on étudie la décision qui suit un modèle.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Garder la vérité terrain pour le test

Chaque paire contient un score et la présence observée d’un événement. Il faudrait des événements indépendants pour un vrai test.

## Construire les quatre comptes

Un faux négatif est un événement manqué ; un faux positif est une alerte sans événement observé.

## Comparer deux politiques

Baisser le seuil récupère un événement dans cet exemple. Sur d’autres données cela peut aussi augmenter les fausses alertes.

## À essayer

Ajoutez (.35, 0) : la baisse de seuil a désormais un coût en fausses alertes. Choisir le seuil nécessite de discuter les deux erreurs.

## Passage aux données réelles

Apprendre les scores sur des images ou séries annotées, séparer lieux et dates de test et choisir le seuil sur validation, pas sur le test final.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
