## Réserver une place à la découverte

Un classement lexical puis une sélection diversifiée sur quatre livres fictifs. Aucune préférence personnelle n’est apprise.

### Décrire les livres par thèmes

Les thèmes sont des étiquettes explicites ; les personnes n’ont pas à fournir un historique intime de lecture.

```python
livres = {"A":{"espace","aventure"},"B":{"espace","aventure","robot"},"C":{"jardin","societe"},"D":{"robot","societe"}}
interets = {"espace","aventure"}
print({k: sorted(v) for k,v in livres.items()})
```

Sortie exécutée :

```text
{'A': ['aventure', 'espace'], 'B': ['aventure', 'espace', 'robot'], 'C': ['jardin', 'societe'], 'D': ['robot', 'societe']}
```

### Trouver les voisins évidents

Le recouvrement favorise A et B, qui se ressemblent. Un score seul peut enfermer dans le même rayon.

```python
scores = {k:len(v & interets) for k,v in livres.items()}
resultats = sorted(scores.items(),key=lambda p:-p[1])
print("Voisins :",resultats)
```

Sortie exécutée :

```text
Voisins : [('A', 2), ('B', 2), ('C', 0), ('D', 0)]
```

### Composer un voisin et un détour

On choisit d’abord un voisin, puis le livre qui partage le moins de thèmes avec lui. C’est une politique éditoriale explicite.

```python
premier = resultats[0][0]
detour = min((k for k in livres if k!=premier),key=lambda k:len(livres[k]&livres[premier]))
print("Voisin :",premier,"; détour :",detour)
```

Sortie exécutée :

```text
Voisin : A ; détour : C
```

### À essayer

Changez les centres d’intérêt vers robot. Observez comment le voisin bouge et discutez si le détour reste pertinent.

### Passage aux données réelles

Un encodeur peut représenter les résumés au-delà des mots exacts. Évaluer aussi diversité et intérêt avec les lecteurs, pas seulement le clic.
