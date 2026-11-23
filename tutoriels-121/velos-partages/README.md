# Retrouver la demande que le stock cache

Une simulation de stock qui montre la censure des observations ; ce programme ne prédit pas encore la demande.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Distinguer intentions et locations

Cinq personnes arrivent ; la station n’a que deux vélos. Dans une archive ordinaire, les intentions refusées peuvent manquer.

## Faire partir seulement les vélos présents

Le compteur des locations s’arrête quand le stock atteint zéro, pas quand la demande disparaît.

## Montrer la partie invisible

Dans ce scénario on connaît les intentions. Dans le réel, il faudrait des observations supplémentaires pour les estimer.

## À essayer

Rejouez avec un stock de 5. Une station mieux équipée peut enregistrer plus de locations sans que la demande ait changé.

## Passage aux données réelles

Marquer les intervalles station vide dans les archives GBFS, puis évaluer une estimation de demande censurée avec une source indépendante.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
