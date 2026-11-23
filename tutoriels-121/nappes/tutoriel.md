## Passer de la profondeur au niveau, puis au décalage

Une conversion géométrique suivie d’une comparaison de pluie et niveau sur six jours fictifs. Ce n’est pas une preuve hydrologique.

### Lire ce que mesure le capteur

Le sol est à 100 m d’altitude. Une profondeur plus grande signifie ici une eau plus basse.

```python
sol = 100
profondeurs = [10,11,10,9,9,10]
niveaux = [sol-p for p in profondeurs]
print("Niveaux d’eau (m) :", niveaux)
```

Sortie exécutée :

```text
Niveaux d’eau (m) : [90, 89, 90, 91, 91, 90]
```

### Décaler la pluie avant de comparer

Un jour de pluie peut être associé à une réponse retardée. On ne rapproche que des indices compatibles, sans utiliser de pluie future.

```python
pluie = [0,20,10,0,0,5]
paires = list(zip(pluie[:-1],niveaux[1:]))
print("Pluie J / niveau J+1 :", paires)
```

Sortie exécutée :

```text
Pluie J / niveau J+1 : [(0, 89), (20, 90), (10, 91), (0, 91), (0, 90)]
```

### Préparer la cible sans surinterpréter

Le changement de niveau diffère du niveau absolu. Une régression pourrait apprendre une relation retardée sur beaucoup plus de données.

```python
variations = [b-a for a,b in zip(niveaux,niveaux[1:])]
resultats = [(f"J{i+1}",v) for i,v in enumerate(niveaux)]
print("Variations quotidiennes (m) :", variations)
print("Nombre de couples :",len(paires),"; insuffisant pour valider une réponse à la pluie")
```

Sortie exécutée :

```text
Variations quotidiennes (m) : [-1, 1, 1, 0, -1]
Nombre de couples : 5 ; insuffisant pour valider une réponse à la pluie
```

### À essayer

Changez la cote du sol à 120 : les altitudes changent, pas les variations. Ne mélangez pas les référentiels entre capteurs.

### Passage aux données réelles

Utiliser les chroniques ADES avec référentiel, qualité, dates et pluies disponibles ; tenir compte des pompages et réserver une période de test.
