## Additionner une exposition sur le trajet

Un indicateur fictif d’exposition au soleil ; aucune température ressentie n’est prédite par ce calcul.

### Décomposer le déplacement

Chaque tronçon a une durée et une fraction au soleil. La zone d’attente compte aussi.

```python
trajets = {"Direct":[(8,1),(4,.5),(3,1)], "Ombragé":[(10,.2),(6,.3),(3,1)]}
print("Minutes / fraction au soleil :", trajets)
```

Sortie exécutée :

```text
Minutes / fraction au soleil : {'Direct': [(8, 1), (4, 0.5), (3, 1)], 'Ombragé': [(10, 0.2), (6, 0.3), (3, 1)]}
```

### Pondérer chaque durée

Cinq minutes à moitié à l’ombre comptent ici pour 2,5 minutes équivalentes au soleil. C’est un indicateur construit, pas une loi sanitaire.

```python
def exposition(troncons):
    return sum(minutes*soleil for minutes,soleil in troncons)
resultats = [(nom,exposition(t)) for nom,t in trajets.items()]
print("Minutes équivalentes au soleil :", resultats)
```

Sortie exécutée :

```text
Minutes équivalentes au soleil : [('Direct', 13.0), ('Ombragé', 6.8)]
```

### Mettre durée et exposition côte à côte

Le trajet moins exposé peut être plus long. L’arbitrage reste visible.

```python
for nom,t in trajets.items():
    print(nom,":",sum(m for m,s in t),"min de trajet ;",round(exposition(t),1),"min équivalentes au soleil")
```

Sortie exécutée :

```text
Direct : 15 min de trajet ; 13.0 min équivalentes au soleil
Ombragé : 19 min de trajet ; 6.8 min équivalentes au soleil
```

### À essayer

Passez l’attente finale de 3 à 10 minutes : un arrêt sans ombre peut devenir le point décisif.

### Passage aux données réelles

Une segmentation d’images peut estimer la couverture, mais heure, ombre réelle, météo et confort nécessitent des données et une validation supplémentaires.
