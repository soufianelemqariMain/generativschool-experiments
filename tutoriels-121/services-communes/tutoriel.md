## Comparer une présence, pas inventer un accès

Une distance entre profils binaires fictifs. Ce voisinage prépare une typologie, il ne mesure pas la qualité de vie.

### Encoder trois équipements

L’ordre des colonnes doit rester identique : école, pharmacie, bibliothèque.

```python
communes = {"A":(1,1,0),"B":(1,0,0),"C":(1,1,1),"D":(0,0,1)}
print("École, pharmacie, bibliothèque :", communes)
```

Sortie exécutée :

```text
École, pharmacie, bibliothèque : {'A': (1, 1, 0), 'B': (1, 0, 0), 'C': (1, 1, 1), 'D': (0, 0, 1)}
```

### Compter les différences

La distance de Hamming compte les colonnes différentes. Ici les trois équipements ont le même poids, un choix discutable.

```python
def distance(a,b):
    return sum(x!=y for x,y in zip(a,b))
resultats = [(k,distance(communes["A"],v)) for k,v in communes.items() if k!="A"]
print("Différences avec A :", resultats)
```

Sortie exécutée :

```text
Différences avec A : [('B', 1), ('C', 1), ('D', 3)]
```

### Ouvrir la comparaison

Deux communes à distance un peuvent différer sur des équipements très différents. On garde les profils lisibles.

```python
proches = [k for k,d in resultats if d==min(v for k,v in resultats)]
print("Voisines de profil :", proches)
print("Horaires, distances et capacité d’accueil : inconnus")
```

Sortie exécutée :

```text
Voisines de profil : ['B', 'C']
Horaires, distances et capacité d’accueil : inconnus
```

### À essayer

Donnez un poids de trois à la pharmacie : le voisinage change. Le choix des variables porte une vision des besoins.

### Passage aux données réelles

La BPE réelle fournit des présences d’équipements. Toute typologie doit être évaluée sans la présenter comme une mesure complète d’accessibilité.
