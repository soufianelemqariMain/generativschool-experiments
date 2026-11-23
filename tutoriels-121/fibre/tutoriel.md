## Comparer des taux plutôt que des volumes bruts

Une normalisation de deux territoires fictifs. Elle prépare un indicateur, sans apprendre un risque individuel.

### Rassembler incidents et lignes

Les deux compteurs doivent couvrir la même période et le même périmètre.

```python
territoires = {"A":(10,100),"B":(10,10000)}
print("Incidents / lignes :",territoires)
```

Sortie exécutée :

```text
Incidents / lignes : {'A': (10, 100), 'B': (10, 10000)}
```

### Diviser par la population exposée

Dix incidents ne signifient pas la même fréquence lorsque cent ou dix mille lignes sont exposées.

```python
resultats = [(k,100*i/n) for k,(i,n) in territoires.items()]
print("Incidents pour 100 lignes :",resultats)
```

Sortie exécutée :

```text
Incidents pour 100 lignes : [('A', 10.0), ('B', 0.1)]
```

### Préciser ce qui reste inconnu

Si une même ligne a plusieurs incidents, ce taux n’est pas la proportion de lignes touchées.

```python
print("Rapport des fréquences :",resultats[0][1]/resultats[1][1])
print("Lignes distinctes touchées : non renseignées")
```

Sortie exécutée :

```text
Rapport des fréquences : 100.0
Lignes distinctes touchées : non renseignées
```

### À essayer

Ajoutez un territoire avec zéro ligne : le taux est indéfini, il ne faut ni diviser par zéro ni écrire 0 %.

### Passage aux données réelles

Un modèle de risque aurait besoin d’historiques d’incidents compatibles avec les données de couverture ; une carte de déploiement ne fournit pas cette cible.
