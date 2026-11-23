# Du texte du produit au lot concerné

Une recherche lexicale de référence, suivie d’une vérification exacte. Aucun encodeur sémantique n’est entraîné ici.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Séparer description et identifiants

Les mots orientent la recherche ; la référence et le lot servent ensuite à vérifier la fiche.

## Classer sans confondre proximité et preuve

Le score de Jaccard mesure la proportion de mots partagés. Il ne comprend pas que doudou et peluche peuvent être proches.

## Contrôler le lot

La meilleure fiche reste une candidate. Un lot différent ne permet pas d’appliquer automatiquement ses consignes au produit.

## À essayer

Remplacez peluche par doudou : voyez la limite du lexique. Un modèle sémantique devra améliorer ce cas sans faire perdre la référence exacte.

## Passage aux données réelles

Comparer recherche littérale et encodeur sur des requêtes annotées, avec des fiches distinctes dans le test. Les résultats réels RappelConso de l’article restent la preuve disponible.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
