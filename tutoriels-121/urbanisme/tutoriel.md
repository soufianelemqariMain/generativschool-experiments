## Choisir le bon texte avant de chercher la réponse

Un filtrage de versions et une recherche de passages fictifs. Aucun règlement réel ni droit à construire n’est déterminé.

### Identifier parcelle, zone et version

Les extraits sont inventés. Deux versions peuvent contenir des règles différentes pour la même zone.

```python
documents = [("2024","UA","hauteur maximale 9 metres"),("2026","UA","hauteur maximale 12 metres"),("2026","UB","hauteur maximale 6 metres")]
version, zone = "2026","UA"
print("Corpus :",documents)
```

Sortie exécutée :

```text
Corpus : [('2024', 'UA', 'hauteur maximale 9 metres'), ('2026', 'UA', 'hauteur maximale 12 metres'), ('2026', 'UB', 'hauteur maximale 6 metres')]
```

### Fermer le corpus avant la recherche

Filtrer après la génération laisserait déjà entrer une règle périmée dans la réponse.

```python
corpus = [texte for v,z,texte in documents if v==version and z==zone]
print("Corpus applicable supposé :",corpus)
```

Sortie exécutée :

```text
Corpus applicable supposé : ['hauteur maximale 12 metres']
```

### Rendre le passage et sa provenance

Une réponse augmentée par recherche doit garder sa source et signaler les annexes non consultées.

```python
passages = [texte for texte in corpus if "hauteur" in texte]
print("Passage :",passages[0] if passages else "aucun passage — réponse impossible")
print("Provenance : zone",zone,"; version",version,"; annexes non examinées")
resultats = [("Documents initiaux",len(documents)),("Après filtre",len(corpus)),("Passages",len(passages))]
```

Sortie exécutée :

```text
Passage : hauteur maximale 12 metres
Provenance : zone UA ; version 2026 ; annexes non examinées
```

### À essayer

Changez la zone à UB : le passage doit changer avant toute reformulation. Une zone absente doit produire aucune réponse, pas la première trouvée.

### Passage aux données réelles

Le modèle peut expliquer des passages, mais il faut vérifier document opposable, parcelle, annexes et mises à jour ; conserver un lien précis vers chaque source.
