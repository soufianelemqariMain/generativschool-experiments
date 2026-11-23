## Une place disponible doit couvrir le bon horaire

Un filtrage de compatibilité sur des créneaux fictifs. Il clarifie la cible d’un futur système de recherche.

### Écrire le besoin en heures

Les intervalles restent dans la même journée pour ce petit exemple.

```python
besoin = (8,18)
creches = [("A",7,19,0),("B",9,18,2),("C",7,18,1)]
print("Besoin :",besoin,"; ouverture, fermeture, places :",creches)
```

Sortie exécutée :

```text
Besoin : (8, 18) ; ouverture, fermeture, places : [('A', 7, 19, 0), ('B', 9, 18, 2), ('C', 7, 18, 1)]
```

### Vérifier toute la plage

Une ouverture après le début du besoin rend le créneau incomplet, même si deux places sont annoncées.

```python
compatibles = [(nom,places) for nom,debut,fin,places in creches if debut<=besoin[0] and fin>=besoin[1]]
print("Horaires compatibles :",compatibles)
```

Sortie exécutée :

```text
Horaires compatibles : [('A', 0), ('C', 1)]
```

### Distinguer compatibilité et admission

Le filtre garde une place théorique, pas une attribution certaine ni une donnée temps réel.

```python
resultats = [(nom,n) for nom,n in compatibles]
print("Disponibilités positives à confirmer :",[nom for nom,n in compatibles if n>0])
```

Sortie exécutée :

```text
Disponibilités positives à confirmer : ['C']
```

### À essayer

Décalez le besoin à 9 h. Une nouvelle structure devient compatible sans que son nombre de places change.

### Passage aux données réelles

Un modèle pourrait rapprocher une demande libre des contraintes ; les disponibilités et critères d’admission doivent venir des organismes concernés.
