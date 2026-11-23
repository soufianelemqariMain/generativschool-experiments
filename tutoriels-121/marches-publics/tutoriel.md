## Filtrer la date avant de classer les avis

Une recherche lexicale sur trois avis fictifs, avec une contrainte exacte de calendrier.

### Séparer objet et date

On fige la date d’examen pour que le résultat soit reproductible.

```python
from datetime import date
jour = date(2026,11,1)
avis = [("A","entretien espaces verts",date(2026,10,30)),("B","entretien parc",date(2026,12,1)),("C","mobilier bureau",date(2026,12,4))]
print("Date de recherche :", jour)
```

Sortie exécutée :

```text
Date de recherche : 2026-11-01
```

### Retirer les délais dépassés

Le meilleur texte du monde ne rend pas recevable une réponse après échéance.

```python
ouverts = [a for a in avis if a[2]>=jour]
print("Avis encore ouverts :", [a[0] for a in ouverts])
```

Sortie exécutée :

```text
Avis encore ouverts : ['B', 'C']
```

### Classer les candidats, puis lire les pièces

Le recouvrement des mots sert de référence. Les conditions de participation restent à examiner dans le dossier.

```python
mots = {"entretien","espaces","verts"}
resultats = sorted([(i,len(set(t.split()) & mots)) for i,t,d in ouverts],key=lambda p:-p[1])
print("Correspondances lexicales :", resultats)
print("Éligibilité de l’entreprise : non vérifiée")
```

Sortie exécutée :

```text
Correspondances lexicales : [('B', 1), ('C', 0)]
Éligibilité de l’entreprise : non vérifiée
```

### À essayer

Déplacez le jour de recherche après le 1er décembre. Le premier candidat doit sortir avant tout classement.

### Passage aux données réelles

Un modèle sémantique peut élargir le vocabulaire, puis être évalué contre cette référence sur des avis annotés. Le test BOAMP existant ne prouve pas une éligibilité.
