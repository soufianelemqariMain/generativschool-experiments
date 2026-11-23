## Faire apparaître les compétences à confirmer

Un rapprochement de compétences explicites. Il sert de référence transparente avant un encodeur de textes.

### Décrire ce qui a été fait

On part de compétences déclarées, sans attribuer automatiquement celles d’un métier voisin.

```python
acquis = {"planifier", "accueillir", "coordonner"}
metiers = {"logistique":{"planifier","coordonner","conduire"}, "accueil":{"accueillir","informer"}, "vente":{"negocier","informer"}}
print("Déclaré :", sorted(acquis))
```

Sortie exécutée :

```text
Déclaré : ['accueillir', 'coordonner', 'planifier']
```

### Chercher les recouvrements

L’intersection montre les éléments communs. Ce nombre n’est ni une aptitude globale ni une chance de recrutement.

```python
resultats = [(m,len(acquis & c)) for m,c in metiers.items()]
print("Compétences communes :", resultats)
```

Sortie exécutée :

```text
Compétences communes : [('logistique', 2), ('accueil', 1), ('vente', 0)]
```

### Nommer ce qui reste à vérifier

La différence d’ensembles ouvre des questions et des formations ; elle ne doit pas être réécrite comme expérience déjà acquise.

```python
cible = max(resultats,key=lambda p:p[1])[0]
print("Piste :", cible)
print("À confirmer ou acquérir :", sorted(metiers[cible]-acquis))
```

Sortie exécutée :

```text
Piste : logistique
À confirmer ou acquérir : ['conduire']
```

### À essayer

Ajoutez conduire uniquement si la personne confirme cette compétence. Voyez pourquoi la validation humaine appartient au parcours.

### Passage aux données réelles

Un encodeur pourrait reformuler les récits libres vers le ROME ; conserver les citations justifiant chaque compétence et ne pas confondre métier possible et offre disponible.
