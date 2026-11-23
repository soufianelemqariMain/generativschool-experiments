# Prévoir un afflux sans déplacer la surcharge

Un scénario de capacité. La fréquentation prévue est une entrée fictive ; elle n’est pas apprise ici.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Afficher capacités et prévisions

Les unités sont des passages par créneau, pas des personnes uniques.

## Mesurer les places restantes

On conserve les valeurs négatives pour rendre la surcharge visible.

## Redistribuer sans dépasser la capacité

On répartit les trente passages excédentaires seulement dans les marges positives ; c’est une règle de décision, pas un modèle appris.

## À essayer

Réduisez la capacité du jardin. Le programme peut laisser un excédent : une recommandation ne crée pas de capacité.

## Passage aux données réelles

Il faudrait apprendre les passages sur des compteurs locaux puis observer l’effet des recommandations ; DATAtourisme décrit l’offre, pas cet historique.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
