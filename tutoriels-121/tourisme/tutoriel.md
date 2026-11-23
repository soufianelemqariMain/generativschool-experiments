## Prévoir un afflux sans déplacer la surcharge

Un scénario de capacité. La fréquentation prévue est une entrée fictive ; elle n’est pas apprise ici.

### Afficher capacités et prévisions

Les unités sont des passages par créneau, pas des personnes uniques.

```python
sites = {"Plage": [120,150], "Sentier": [80,60], "Jardin": [100,70]}
print("Capacité / passages prévus :", sites)
```

Sortie exécutée :

```text
Capacité / passages prévus : {'Plage': [120, 150], 'Sentier': [80, 60], 'Jardin': [100, 70]}
```

### Mesurer les places restantes

On conserve les valeurs négatives pour rendre la surcharge visible.

```python
marges = {s:c-p for s,(c,p) in sites.items()}
print("Marges :", marges)
```

Sortie exécutée :

```text
Marges : {'Plage': -30, 'Sentier': 20, 'Jardin': 30}
```

### Redistribuer sans dépasser la capacité

On répartit les trente passages excédentaires seulement dans les marges positives ; c’est une règle de décision, pas un modèle appris.

```python
excedent = max(0,-marges["Plage"])
for s in ["Sentier","Jardin"]:
    transfert = min(excedent,max(0,marges[s]))
    sites[s][1] += transfert
    sites["Plage"][1] -= transfert
    excedent -= transfert
resultats = [(s,p) for s,(c,p) in sites.items()]
print("Après redistribution :", resultats)
```

Sortie exécutée :

```text
Après redistribution : [('Plage', 120), ('Sentier', 80), ('Jardin', 80)]
```

### À essayer

Réduisez la capacité du jardin. Le programme peut laisser un excédent : une recommandation ne crée pas de capacité.

### Passage aux données réelles

Il faudrait apprendre les passages sur des compteurs locaux puis observer l’effet des recommandations ; DATAtourisme décrit l’offre, pas cet historique.
