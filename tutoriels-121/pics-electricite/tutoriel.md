## Passer d’une courbe prévue à un créneau

Un apprentissage linéaire simplifié entre température et puissance, puis un calcul de coût séparé. Les nombres sont fictifs.

### Former des couples météo-réseau

La température doit être celle connue au moment de prévoir. Ici les quatre points sont artificiellement réguliers pour rendre la droite lisible.

```python
temperatures = [0, 5, 10, 15]
puissances = [70000, 65000, 60000, 55000]
print(list(zip(temperatures, puissances)))
```

Sortie exécutée :

```text
[(0, 70000), (5, 65000), (10, 60000), (15, 55000)]
```

### Ajuster la pente

La pente décrit combien de MW changent pour un degré dans ces exemples. Ce lien appris ne prouve pas une causalité isolée.

```python
from statistics import mean
mx, my = mean(temperatures), mean(puissances)
pente = sum((x-mx)*(y-my) for x,y in zip(temperatures,puissances))/sum((x-mx)**2 for x in temperatures)
interception = my-pente*mx
print(f"Puissance = {interception:.0f} + ({pente:.0f}) × température")
```

Sortie exécutée :

```text
Puissance = 70000 + (-1000) × température
```

### Distinguer prévision et facture

À 8 °C la droite donne une puissance nationale. Le coût de l’appareil dépend, lui, de ses kWh et du contrat.

```python
prediction = interception+pente*8
resultats = [("0 °C",70000),("5 °C",65000),("8 °C prévu",prediction),("15 °C",55000)]
print(f"Prévision illustrative : {prediction:.0f} MW")
print(f"Appareil 1 kW pendant 2 h à 0,15 €/kWh : {1*2*.15:.2f} €")
```

Sortie exécutée :

```text
Prévision illustrative : 62000 MW
Appareil 1 kW pendant 2 h à 0,15 €/kWh : 0.30 €
```

### À essayer

Ajoutez un point de grand froid qui s’écarte de la droite. Regardez comment la pente bouge ; une relation linéaire peut manquer certains régimes.

### Passage aux données réelles

Le modèle réseau réel nécessite calendrier, historiques et prévisions météo archivées ; réserver la fin de la chronologie. Une baisse nationale ne garantit pas un tarif domestique plus bas.
