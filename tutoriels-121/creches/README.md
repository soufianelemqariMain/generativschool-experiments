# Une place disponible doit couvrir le bon horaire

Un filtrage de compatibilité sur des créneaux fictifs. Il clarifie la cible d’un futur système de recherche.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Écrire le besoin en heures

Les intervalles restent dans la même journée pour ce petit exemple.

## Vérifier toute la plage

Une ouverture après le début du besoin rend le créneau incomplet, même si deux places sont annoncées.

## Distinguer compatibilité et admission

Le filtre garde une place théorique, pas une attribution certaine ni une donnée temps réel.

## À essayer

Décalez le besoin à 9 h. Une nouvelle structure devient compatible sans que son nombre de places change.

## Passage aux données réelles

Un modèle pourrait rapprocher une demande libre des contraintes ; les disponibilités et critères d’admission doivent venir des organismes concernés.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
