# Passer de la profondeur au niveau, puis au décalage

Une conversion géométrique suivie d’une comparaison de pluie et niveau sur six jours fictifs. Ce n’est pas une preuve hydrologique.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Lire ce que mesure le capteur

Le sol est à 100 m d’altitude. Une profondeur plus grande signifie ici une eau plus basse.

## Décaler la pluie avant de comparer

Un jour de pluie peut être associé à une réponse retardée. On ne rapproche que des indices compatibles, sans utiliser de pluie future.

## Préparer la cible sans surinterpréter

Le changement de niveau diffère du niveau absolu. Une régression pourrait apprendre une relation retardée sur beaucoup plus de données.

## À essayer

Changez la cote du sol à 120 : les altitudes changent, pas les variations. Ne mélangez pas les référentiels entre capteurs.

## Passage aux données réelles

Utiliser les chroniques ADES avec référentiel, qualité, dates et pluies disponibles ; tenir compte des pompages et réserver une période de test.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
