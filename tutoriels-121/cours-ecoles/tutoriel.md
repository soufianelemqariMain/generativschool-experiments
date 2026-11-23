## Croiser deux masques avant de compter

Un masque de végétation déjà fourni et une limite de cour fictive. Le code ne réalise pas de reconnaissance d’image.

### Distinguer végétation et périmètre

Les matrices 4 × 4 sont alignées pixel par pixel. Un arbre hors cour ne doit pas gonfler la part végétalisée.

```python
vegetation = [[1,1,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,1]]
cour = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
print("Pixels dans la cour :",sum(map(sum,cour)))
```

Sortie exécutée :

```text
Pixels dans la cour : 4
```

### Intersecter les deux masques

Un pixel est compté seulement si les deux valeurs valent un. Les deux produits doivent partager la même géométrie.

```python
intersection = [[v*c for v,c in zip(vr,cr)] for vr,cr in zip(vegetation,cour)]
verts = sum(map(sum,intersection))
print("Pixels végétalisés dans la cour :",verts)
```

Sortie exécutée :

```text
Pixels végétalisés dans la cour : 1
```

### Passer à une proportion

Un pixel sur quatre représente 25 % de cette grille. Cela ne mesure ni ombre, ni fraîcheur, ni usage réel.

```python
total = sum(map(sum,cour))
part = 100*verts/total
resultats = [("Végétalisé",verts),("Autre surface",total-verts)]
print(f"Part végétalisée : {part:.1f} %")
```

Sortie exécutée :

```text
Part végétalisée : 25.0 %
```

### À essayer

Ajoutez de la végétation hors de la cour : le résultat doit rester identique. Déplacez ensuite le masque de cour pour voir le risque de désalignement.

### Passage aux données réelles

Un modèle de segmentation produirait le premier masque ; les limites de cour et la validation sur le terrain sont deux tâches distinctes.
