## Voir une médiane bouger sans hausse générale

Une comparaison de distributions fictives ; cette préparation explique la cible avant toute forêt de prévision.

### Ranger les ventes

Chaque valeur est un prix au m². Les cinq ventes de chaque mois ne sont pas les mêmes biens.

```python
a = [1800,2000,2100,2200,8000]
b = [2000,2100,2200,2500,8000]
print("Ventes A :", a, "; ventes B :", b)
```

Sortie exécutée :

```text
Ventes A : [1800, 2000, 2100, 2200, 8000] ; ventes B : [2000, 2100, 2200, 2500, 8000]
```

### Prendre le centre

La médiane résiste à une valeur extrême mais reste sensible à la composition des ventes.

```python
from statistics import median
resultats = [("Mois A",median(a)),("Mois B",median(b))]
print("Médianes €/m² :", resultats)
```

Sortie exécutée :

```text
Médianes €/m² : [('Mois A', 2100), ('Mois B', 2200)]
```

### Interpréter le changement

Cette variation agrégée ne mesure pas le prix du même logement d’un mois à l’autre.

```python
variation = 100*(median(b)/median(a)-1)
print(f"Variation de médiane : {variation:.2f} %")
print("Variation du même logement : impossible à déduire de ces listes")
```

Sortie exécutée :

```text
Variation de médiane : 4.76 %
Variation du même logement : impossible à déduire de ces listes
```

### À essayer

Remplacez 8 000 par 80 000 : la médiane ne change pas. Retirez plutôt une petite vente : la composition compte.

### Passage aux données réelles

Pour apprendre une tendance sur DVF, documenter les dates de publication, les types de biens et le nombre minimal de ventes ; utiliser une séparation chronologique.
