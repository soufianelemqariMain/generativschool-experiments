# Comparer des taux plutôt que des volumes bruts

Une normalisation de deux territoires fictifs. Elle prépare un indicateur, sans apprendre un risque individuel.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Rassembler incidents et lignes

Les deux compteurs doivent couvrir la même période et le même périmètre.

## Diviser par la population exposée

Dix incidents ne signifient pas la même fréquence lorsque cent ou dix mille lignes sont exposées.

## Préciser ce qui reste inconnu

Si une même ligne a plusieurs incidents, ce taux n’est pas la proportion de lignes touchées.

## À essayer

Ajoutez un territoire avec zéro ligne : le taux est indéfini, il ne faut ni diviser par zéro ni écrire 0 %.

## Passage aux données réelles

Un modèle de risque aurait besoin d’historiques d’incidents compatibles avec les données de couverture ; une carte de déploiement ne fournit pas cette cible.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
