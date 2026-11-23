## Prévoir sans emprunter les informations de demain

Une référence de persistance et son test chronologique sur des concentrations inventées de PM2,5.

### Ranger les concentrations dans le temps

Chaque ligne correspond à une journée. L’unité reste le µg/m³ pendant tout le calcul.

```python
jours = [12,14,13,18,25,20]
print("PM2,5 journaliers (µg/m³) :", jours)
```

Sortie exécutée :

```text
PM2,5 journaliers (µg/m³) : [12, 14, 13, 18, 25, 20]
```

### Émettre avant d’observer

Pour chaque jour du test, on reprend la veille. La valeur du jour visé ne rentre pas dans sa propre prévision.

```python
predictions = jours[:-1]
observations = jours[1:]
print("Prévu / observé :", list(zip(predictions, observations)))
```

Sortie exécutée :

```text
Prévu / observé : [(12, 14), (14, 13), (13, 18), (18, 25), (25, 20)]
```

### Mesurer ce qu’il faudra battre

L’erreur absolue moyenne décrit un écart de concentration, pas un risque sanitaire individuel.

```python
from statistics import mean
mae = mean(abs(p-y) for p,y in zip(predictions,observations))
resultats = [(f"J{i+2}", y) for i,y in enumerate(observations)]
print(f"Référence à battre : {mae:.2f} µg/m³")
```

Sortie exécutée :

```text
Référence à battre : 4.00 µg/m³
```

### À essayer

Ajoutez une pointe à 60. La référence réagit avec un jour de retard : repérez-le dans les couples plutôt que dans la seule moyenne.

### Passage aux données réelles

Ajouter des prévisions météo réellement disponibles à l’émission, puis comparer sur les mêmes jours. Des observations météo futures rendraient le test artificiellement facile.
