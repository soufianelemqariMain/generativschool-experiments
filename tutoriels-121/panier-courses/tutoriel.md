## Faire pousser un premier arbre de prix

Un arbre de régression à une seule question, appris sur six observations inventées. Il explique une brique possible de la forêt, pas une prévision Insee.

### Lire six couples de mois

x est la variation déjà connue ; y la variation du mois suivant, en %. Les deux dernières lignes restent hors de l’apprentissage.

```python
exemples = [(0, .5), (1, 1), (2, 1.5), (4, 4.5), (5, 5), (6, 5.5)]
test = [(1.5, 1.2), (5.5, 5.2)]
print("Passé connu → mois suivant (%) :", exemples)
```

Sortie exécutée :

```text
Passé connu → mois suivant (%) : [(0, 0.5), (1, 1), (2, 1.5), (4, 4.5), (5, 5), (6, 5.5)]
```

### Laisser les exemples choisir la question

Chaque seuil coupe le passé en deux groupes. La moyenne de chaque groupe devient une feuille. On choisit le seuil dont la somme des erreurs au carré est la plus faible.

```python
from statistics import mean
seuils = [(a[0]+b[0])/2 for a,b in zip(exemples, exemples[1:])]
def ajuster(seuil):
    gauche = [y for x,y in exemples if x <= seuil]
    droite = [y for x,y in exemples if x > seuil]
    bas, haut = mean(gauche), mean(droite)
    erreur = sum((y-(bas if x <= seuil else haut))**2 for x,y in exemples)
    return erreur, seuil, bas, haut
_, seuil, bas, haut = min(map(ajuster, seuils))
print(f"Question apprise : variation passée ≤ {seuil:g} % ?")
print(f"Oui : {bas:g} % ; non : {haut:g} %")
```

Sortie exécutée :

```text
Question apprise : variation passée ≤ 3 % ?
Oui : 1 % ; non : 5 %
```

### Suivre une branche puis refaire le ticket

Avec une variation connue de 4 %, on suit la branche droite. L’arbre estime 5 % ; la recomposition du panier reste une multiplication. Le test porte sur deux exemples distincts, trop peu pour conclure.

```python
def prevoir(x):
    return bas if x <= seuil else haut
prediction = prevoir(4)
ticket = 60*(1+prediction/100) + 40*1.01
mae = mean(abs(prevoir(x)-y) for x,y in test)
resultats = [("Frais : hausse prévue", prediction), ("Autres : hypothèse", 1)]
print(f"Panier : {ticket:.2f} € ; erreur sur deux cas : {mae:.2f} point de %")
```

Sortie exécutée :

```text
Panier : 103.40 € ; erreur sur deux cas : 0.20 point de %
```

### À essayer

Ajoutez (3, 4) au passé, puis relancez : le seuil ou les feuilles changent-ils ? La question est apprise, elle n’est pas écrite à la main.

### Passage aux données réelles

Remplacer ces couples par des variations mensuelles publiées, avec leur date de disponibilité ; réserver plusieurs mois futurs et comparer à la variation inchangée. Une forêt agrégerait plusieurs arbres, pas les deux feuilles de celui-ci.
