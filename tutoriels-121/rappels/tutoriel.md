## Du texte du produit au lot concerné

Une recherche lexicale de référence, suivie d’une vérification exacte. Aucun encodeur sémantique n’est entraîné ici.

### Séparer description et identifiants

Les mots orientent la recherche ; la référence et le lot servent ensuite à vérifier la fiche.

```python
fiches = [dict(id="A", texte="peluche gateau enfant", lot="L12"), dict(id="B", texte="gateau chocolat", lot="L98"), dict(id="C", texte="peluche ours", lot="L07")]
requete = set("peluche gateau".split())
print("Demande :", sorted(requete))
```

Sortie exécutée :

```text
Demande : ['gateau', 'peluche']
```

### Classer sans confondre proximité et preuve

Le score de Jaccard mesure la proportion de mots partagés. Il ne comprend pas que doudou et peluche peuvent être proches.

```python
def score(f):
    mots = set(f["texte"].split())
    return len(mots & requete)/len(mots | requete)
classement = sorted(fiches, key=score, reverse=True)
resultats = [(f["id"], round(score(f),3)) for f in classement]
print("Scores lexicaux :", resultats)
```

Sortie exécutée :

```text
Scores lexicaux : [('A', 0.667), ('B', 0.333), ('C', 0.333)]
```

### Contrôler le lot

La meilleure fiche reste une candidate. Un lot différent ne permet pas d’appliquer automatiquement ses consignes au produit.

```python
lot_detenu = "L13"
candidate = classement[0]
print("Fiche candidate :", candidate["id"])
print("Lot correspondant :", candidate["lot"] == lot_detenu)
```

Sortie exécutée :

```text
Fiche candidate : A
Lot correspondant : False
```

### À essayer

Remplacez peluche par doudou : voyez la limite du lexique. Un modèle sémantique devra améliorer ce cas sans faire perdre la référence exacte.

### Passage aux données réelles

Comparer recherche littérale et encodeur sur des requêtes annotées, avec des fiches distinctes dans le test. Les résultats réels RappelConso de l’article restent la preuve disponible.
