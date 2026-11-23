## Repérer un écart, ouvrir une vérification

Un score d’écart à un historique fictif ; une alerte n’est pas une fuite diagnostiquée.

### Fixer une référence

Comparer le même service évite ici de confondre taille du réseau et anomalie. Les rendements sont en %.

```python
historique = [79,80,81,80,79,81]
nouveau = 65
print("Historique de rendement (%) :", historique)
```

Sortie exécutée :

```text
Historique de rendement (%) : [79, 80, 81, 80, 79, 81]
```

### Standardiser l’écart

On mesure la distance à la moyenne en nombre d’écarts-types. Une dispersion nulle exigerait un traitement séparé.

```python
from statistics import mean, pstdev
centre, dispersion = mean(historique), pstdev(historique)
z = (nouveau-centre)/dispersion
print(f"Centre : {centre:.1f} % ; écart standardisé : {z:.2f}")
```

Sortie exécutée :

```text
Centre : 80.0 % ; écart standardisé : -18.37
```

### Envoyer une alerte à vérifier

Le seuil de trois écarts-types est choisi pour l’exemple. Vérifier la déclaration et l’exploitation précède l’inspection physique.

```python
alerte = abs(z)>3
resultats = [("Habituel",centre),("Nouvelle déclaration",nouveau)]
print("Dossier à vérifier :", alerte)
print("Cause connue : non ; contrôler déclaration, exploitation, puis réseau")
```

Sortie exécutée :

```text
Dossier à vérifier : True
Cause connue : non ; contrôler déclaration, exploitation, puis réseau
```

### À essayer

Ajoutez une ancienne année à 60 %. La référence change : une anomalie durable ne doit pas devenir normale par simple oubli du contexte.

### Passage aux données réelles

Un détecteur multivarié réel devrait intégrer volumes, longueur et qualité des déclarations ; seules des inspections annotées permettraient d’évaluer une détection de fuites.
