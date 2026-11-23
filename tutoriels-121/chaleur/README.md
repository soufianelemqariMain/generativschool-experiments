# Additionner une exposition sur le trajet

Un indicateur fictif d’exposition au soleil ; aucune température ressentie n’est prédite par ce calcul.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Décomposer le déplacement

Chaque tronçon a une durée et une fraction au soleil. La zone d’attente compte aussi.

## Pondérer chaque durée

Cinq minutes à moitié à l’ombre comptent ici pour 2,5 minutes équivalentes au soleil. C’est un indicateur construit, pas une loi sanitaire.

## Mettre durée et exposition côte à côte

Le trajet moins exposé peut être plus long. L’arbitrage reste visible.

## À essayer

Passez l’attente finale de 3 à 10 minutes : un arrêt sans ombre peut devenir le point décisif.

## Passage aux données réelles

Une segmentation d’images peut estimer la couverture, mais heure, ombre réelle, météo et confort nécessitent des données et une validation supplémentaires.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
