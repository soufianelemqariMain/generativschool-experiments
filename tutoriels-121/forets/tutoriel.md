## Choisir un seuil sans cacher les alertes manquées

Un test de seuil sur six scores fictifs. Les scores sont fournis, pas appris ; on étudie la décision qui suit un modèle.

### Garder la vérité terrain pour le test

Chaque paire contient un score et la présence observée d’un événement. Il faudrait des événements indépendants pour un vrai test.

```python
cas = [(.1,0),(.2,0),(.4,1),(.55,0),(.7,1),(.9,1)]
print("Score / événement :",cas)
```

Sortie exécutée :

```text
Score / événement : [(0.1, 0), (0.2, 0), (0.4, 1), (0.55, 0), (0.7, 1), (0.9, 1)]
```

### Construire les quatre comptes

Un faux négatif est un événement manqué ; un faux positif est une alerte sans événement observé.

```python
def bilan(seuil):
    vp = sum(s>=seuil and y==1 for s,y in cas)
    fp = sum(s>=seuil and y==0 for s,y in cas)
    fn = sum(s<seuil and y==1 for s,y in cas)
    vn = sum(s<seuil and y==0 for s,y in cas)
    return vp,fp,fn,vn
print("VP, FP, FN, VN :",bilan(.5))
```

Sortie exécutée :

```text
VP, FP, FN, VN : (2, 1, 1, 2)
```

### Comparer deux politiques

Baisser le seuil récupère un événement dans cet exemple. Sur d’autres données cela peut aussi augmenter les fausses alertes.

```python
resultats = [("Manqués à 0,5",bilan(.5)[2]),("Manqués à 0,3",bilan(.3)[2])]
print("Seuil 0,5 :",bilan(.5),"; seuil 0,3 :",bilan(.3))
```

Sortie exécutée :

```text
Seuil 0,5 : (2, 1, 1, 2) ; seuil 0,3 : (3, 1, 0, 2)
```

### À essayer

Ajoutez (.35, 0) : la baisse de seuil a désormais un coût en fausses alertes. Choisir le seuil nécessite de discuter les deux erreurs.

### Passage aux données réelles

Apprendre les scores sur des images ou séries annotées, séparer lieux et dates de test et choisir le seuil sur validation, pas sur le test final.
