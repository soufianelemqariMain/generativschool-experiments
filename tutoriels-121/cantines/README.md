# Apprendre une présence, choisir une préparation

Un taux de présence estimé sur quatre services fictifs, puis une décision tenant compte du coût du manque.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Observer les présences après le service

Une réservation est une entrée ; le nombre servi devient la cible seulement une fois la journée terminée.

## Estimer le taux pour demain

La somme des présences divisée par celle des réservations pondère correctement les journées. Demain, on connaît 200 réservations.

## Décider sous plusieurs présences possibles

On chiffre trois scénarios équiprobables. Le coût fictif d’un repas manquant vaut quatre fois celui d’un surplus. Ce choix relève de l’équipe, pas du modèle.

## À essayer

Passez le coefficient du manque de 4 à 1. La décision peut changer sans réentraîner le taux de présence.

## Passage aux données réelles

Il faut un historique quotidien local ; Ma cantine ne fournit pas à elle seule ces cibles. Tester hors période d’apprentissage et convenir des coûts avec les équipes.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
