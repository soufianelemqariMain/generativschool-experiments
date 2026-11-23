## Garder les inconnues dans un dossier d’aide

Un contrôle de critères fictifs à trois états. Il complète une recherche de textes mais n’est pas une décision administrative.

### Décrire les critères connus

None signifie qu’une information manque. On ne transforme pas ce manque en oui.

```python
criteres = {"porteur":True,"territoire":True,"calendrier":None}
print(criteres)
```

Sortie exécutée :

```text
{'porteur': True, 'territoire': True, 'calendrier': None}
```

### Appliquer une logique à trois états

Un non suffit à bloquer ; en son absence, une inconnue impose une vérification.

```python
def statut(c):
    if False in c.values(): return "critère bloquant"
    if None in c.values(): return "à compléter"
    return "critères examinés satisfaits"
print("Dossier :", statut(criteres))
```

Sortie exécutée :

```text
Dossier : à compléter
```

### Rendre la question suivante explicite

L’outil doit citer ce qui manque et la source à lire, au lieu de produire une assurance générale.

```python
manquants = [k for k,v in criteres.items() if v is None]
resultats = [(k,1 if v is True else 0) for k,v in criteres.items()]
print("À documenter :", manquants)
print("Décision finale : consulter le règlement et l’organisme")
```

Sortie exécutée :

```text
À documenter : ['calendrier']
Décision finale : consulter le règlement et l’organisme
```

### À essayer

Passez territoire à False. Le blocage doit être visible même si les autres critères sont favorables.

### Passage aux données réelles

Un modèle peut extraire les critères et passages pertinents ; les comparer au règlement à jour et conserver chaque citation avant de calculer ce statut.
