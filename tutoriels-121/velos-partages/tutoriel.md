## Retrouver la demande que le stock cache

Une simulation de stock qui montre la censure des observations ; ce programme ne prédit pas encore la demande.

### Distinguer intentions et locations

Cinq personnes arrivent ; la station n’a que deux vélos. Dans une archive ordinaire, les intentions refusées peuvent manquer.

```python
stock = 2
intentions = [1,1,1,1,1]
print("Stock initial :", stock, "; personnes souhaitant partir :", len(intentions))
```

Sortie exécutée :

```text
Stock initial : 2 ; personnes souhaitant partir : 5
```

### Faire partir seulement les vélos présents

Le compteur des locations s’arrête quand le stock atteint zéro, pas quand la demande disparaît.

```python
locations = 0
refus = 0
for demande in intentions:
    if stock >= demande:
        stock -= demande
        locations += demande
    else:
        refus += demande
print("Locations observées :", locations, "; stock final :", stock)
```

Sortie exécutée :

```text
Locations observées : 2 ; stock final : 0
```

### Montrer la partie invisible

Dans ce scénario on connaît les intentions. Dans le réel, il faudrait des observations supplémentaires pour les estimer.

```python
resultats = [("Locations",locations),("Demandes refusées",refus)]
print("Demande totale simulée :", locations+refus)
print("Une archive de locations seule ne voit que", locations)
```

Sortie exécutée :

```text
Demande totale simulée : 5
Une archive de locations seule ne voit que 2
```

### À essayer

Rejouez avec un stock de 5. Une station mieux équipée peut enregistrer plus de locations sans que la demande ait changé.

### Passage aux données réelles

Marquer les intervalles station vide dans les archives GBFS, puis évaluer une estimation de demande censurée avec une source indépendante.
