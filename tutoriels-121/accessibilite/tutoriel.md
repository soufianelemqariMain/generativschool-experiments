## Ne pas faire disparaître ce que l’on ignore

Un contrôle à trois états sur des informations fictives ; un champ absent n’est pas une preuve d’accessibilité.

### Conserver les valeurs inconnues

Le besoin illustratif porte sur une entrée de plain-pied et une porte assez large.

```python
lieux = {"A":{"plain_pied":True,"porte_large":True},"B":{"plain_pied":True,"porte_large":None},"C":{"plain_pied":False,"porte_large":True}}
print(lieux)
```

Sortie exécutée :

```text
{'A': {'plain_pied': True, 'porte_large': True}, 'B': {'plain_pied': True, 'porte_large': None}, 'C': {'plain_pied': False, 'porte_large': True}}
```

### Calculer trois statuts distincts

Le résultat dépend du besoin choisi ; il ne vaut pas pour tous les handicaps ni tous les usages.

```python
def statut(c):
    if False in c.values(): return "contrainte identifiée"
    if None in c.values(): return "information manquante"
    return "critères renseignés compatibles"
for nom,c in lieux.items(): print(nom,statut(c))
```

Sortie exécutée :

```text
A critères renseignés compatibles
B information manquante
C contrainte identifiée
```

### Produire une question utile

L’outil peut demander une confirmation ciblée au lieu de rendre un simple classement opaque.

```python
for nom,c in lieux.items():
    inconnus = [k for k,v in c.items() if v is None]
    if inconnus: print(nom,"— à confirmer :",inconnus)
resultats = [(nom,sum(v is True for v in c.values())) for nom,c in lieux.items()]
```

Sortie exécutée :

```text
B — à confirmer : ['porte_large']
```

### À essayer

Effacez une valeur True : le lieu doit passer en information manquante, pas rester recommandé sans réserve.

### Passage aux données réelles

Un modèle peut extraire des descriptions, mais il faut conserver provenance, date, besoin utilisateur et validation du renseignement.
