## Reconnaître l’objet ne décide pas de son avenir

Une table de décision après une reconnaissance supposée. Les règles de filière doivent être vérifiées localement.

### Décrire l’état en plus de l’objet

Deux objets identiques peuvent avoir des parcours différents selon qu’ils fonctionnent ou sont réparables.

```python
objets = [("grille-pain",True,None),("grille-pain",False,True),("grille-pain",False,False)]
print("Objet / fonctionne / réparable :", objets)
```

Sortie exécutée :

```text
Objet / fonctionne / réparable : [('grille-pain', True, None), ('grille-pain', False, True), ('grille-pain', False, False)]
```

### Séparer les embranchements

La reconnaissance d’image fournirait une catégorie ; ces règles traitent l’état, qui ne se déduit pas toujours de la photo.

```python
def parcours(fonctionne,reparable):
    if fonctionne: return "réemploi à examiner"
    if reparable is None: return "diagnostic nécessaire"
    return "réparation à examiner" if reparable else "filière adaptée à vérifier"
print([parcours(f,r) for o,f,r in objets])
```

Sortie exécutée :

```text
['réemploi à examiner', 'réparation à examiner', 'filière adaptée à vérifier']
```

### Conserver le diagnostic manquant

Un objet non fonctionnel sans diagnostic doit rester dans une branche inconnue.

```python
print("Cas sans diagnostic :", parcours(False,None))
resultats = [(parcours(f,r),i+1) for i,(o,f,r) in enumerate(objets)]
```

Sortie exécutée :

```text
Cas sans diagnostic : diagnostic nécessaire
```

### À essayer

Ajoutez une photo sans information de fonctionnement : le programme ne peut pas conclure à une réparation possible.

### Passage aux données réelles

Un classifieur d’objets doit être testé sur des images distinctes ; la recommandation finale nécessite des règles de filière et des informations de diagnostic.
