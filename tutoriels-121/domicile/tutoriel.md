## Faire entrer les trajets dans la tournée

Un petit calcul de planning ; il met en évidence la contrainte avant une éventuelle optimisation et une estimation des durées.

### Écrire les visites et déplacements

L’ordre est déjà fixé ici. On ne prétend pas résoudre un problème de tournée.

```python
visites = [60,60,60]
trajets = [20,20]
print("Visites (min) :",visites,"; trajets (min) :",trajets)
```

Sortie exécutée :

```text
Visites (min) : [60, 60, 60] ; trajets (min) : [20, 20]
```

### Construire une chronologie

Chaque déplacement décale la visite suivante. Les durées sont des hypothèses, pas des mesures routières.

```python
minute = 0
resultats = []
for i,duree in enumerate(visites):
    resultats.append((f"Visite {i+1}",duree))
    print(f"Visite {i+1} : minute {minute} à {minute+duree}")
    minute += duree
    if i<len(trajets): minute += trajets[i]
```

Sortie exécutée :

```text
Visite 1 : minute 0 à 60
Visite 2 : minute 80 à 140
Visite 3 : minute 160 à 220
```

### Comparer au temps disponible

Trois heures de soin ne tiennent pas en trois heures de travail lorsque les déplacements sont nécessaires.

```python
disponible = 210
print("Temps nécessaire :",minute,"min")
print("Dépassement :",max(0,minute-disponible),"min")
```

Sortie exécutée :

```text
Temps nécessaire : 220 min
Dépassement : 10 min
```

### À essayer

Ajoutez une pause de dix minutes. Ne la cachez pas dans une durée de visite artificiellement raccourcie.

### Passage aux données réelles

Les durées peuvent être prédites à partir d’historiques ; l’optimisation doit respecter pauses, compétences, horaires et continuité des intervenants.
