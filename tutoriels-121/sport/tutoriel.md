## Respecter les contraintes avant les préférences

Un filtre sur trois activités fictives. Le rapprochement sémantique pourrait venir ensuite, dans la liste faisable.

### Séparer budget, horaire et envie

L’envie de plein air ne doit pas faire oublier une indisponibilité ou un coût trop élevé.

```python
activites = [("Course",0,18,True),("Tennis",25,18,True),("Natation",8,20,False)]
budget, heure_max = 10,19
print("Nom, euros, heure, dehors :",activites)
```

Sortie exécutée :

```text
Nom, euros, heure, dehors : [('Course', 0, 18, True), ('Tennis', 25, 18, True), ('Natation', 8, 20, False)]
```

### Appliquer les contraintes dures

Le budget est un prix par séance dans cet exemple ; il faut harmoniser abonnements et tarifs avant une comparaison réelle.

```python
possibles = [a for a in activites if a[1]<=budget and a[2]<=heure_max]
print("Faisables :",[a[0] for a in possibles])
```

Sortie exécutée :

```text
Faisables : ['Course']
```

### Classer ce qui reste

La préférence extérieur départage seulement les options encore possibles.

```python
resultats = [(a[0],int(a[3])) for a in sorted(possibles,key=lambda a:not a[3])]
print("Préférence plein air :",resultats)
```

Sortie exécutée :

```text
Préférence plein air : [('Course', 1)]
```

### À essayer

Passez heure_max à 21 et retirez la préférence extérieur : une autre option redevient possible.

### Passage aux données réelles

Une recherche sémantique peut traduire « bouger sans compétition » ; les tarifs, inscriptions et horaires exigent des données actualisées.
