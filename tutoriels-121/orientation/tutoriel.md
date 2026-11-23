## Ouvrir plusieurs chemins au lieu d’un classement unique

Une comparaison de programmes fictifs par centres d’intérêt. Ce score n’est pas une probabilité d’admission.

### Exprimer deux intérêts

On ne transforme ni les intérêts ni une note en destin scolaire.

```python
interets = {"creer","biologie"}
formations = {"Design":{"creer","dessiner"},"Biologie":{"biologie","experimenter"},"Paysage":{"creer","biologie","terrain"}}
print("Intérêts :", sorted(interets))
```

Sortie exécutée :

```text
Intérêts : ['biologie', 'creer']
```

### Compter les points de contact

Le recouvrement ouvre des pistes ; il ignore ici prérequis, coût et distance.

```python
resultats = [(nom,len(interets & contenu)) for nom,contenu in formations.items()]
print("Points de contact :", resultats)
```

Sortie exécutée :

```text
Points de contact : [('Design', 1), ('Biologie', 1), ('Paysage', 2)]
```

### Ajouter une question par chemin

On laisse les différences visibles, plutôt que de supprimer les formations moins bien classées.

```python
for nom,contenu in formations.items():
    print(nom, "— à découvrir :", ", ".join(sorted(contenu-interets)))
```

Sortie exécutée :

```text
Design — à découvrir : dessiner
Biologie — à découvrir : experimenter
Paysage — à découvrir : terrain
```

### À essayer

Ajoutez terrain aux intérêts. Demandez ensuite ce qu’un score ne peut pas savoir : contraintes de mobilité, envie réelle, prérequis.

### Passage aux données réelles

Une recherche sémantique sur des descriptions de formation pourrait aider à explorer ; les décisions et données d’admission doivent rester séparées.
