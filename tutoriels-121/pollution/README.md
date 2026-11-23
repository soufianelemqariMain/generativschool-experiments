# Prévoir sans emprunter les informations de demain

Une référence de persistance et son test chronologique sur des concentrations inventées de PM2,5.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Ranger les concentrations dans le temps

Chaque ligne correspond à une journée. L’unité reste le µg/m³ pendant tout le calcul.

## Émettre avant d’observer

Pour chaque jour du test, on reprend la veille. La valeur du jour visé ne rentre pas dans sa propre prévision.

## Mesurer ce qu’il faudra battre

L’erreur absolue moyenne décrit un écart de concentration, pas un risque sanitaire individuel.

## À essayer

Ajoutez une pointe à 60. La référence réagit avec un jour de retard : repérez-le dans les couples plutôt que dans la seule moyenne.

## Passage aux données réelles

Ajouter des prévisions météo réellement disponibles à l’émission, puis comparer sur les mêmes jours. Des observations météo futures rendraient le test artificiellement facile.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
