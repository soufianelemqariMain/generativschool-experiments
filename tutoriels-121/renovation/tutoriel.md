## Comparer des logements avant d’estimer

Une régression par trois voisins sur un minuscule jeu fictif. La cible est une consommation conventionnelle, pas la facture ni l’économie de travaux.

### Décrire des logements comparables

On fixe ici le type et la zone climatique ; seule la surface varie. Dans un vrai modèle, oublier l’isolation ou le chauffage serait une limite majeure.

```python
logements = [(45, 220), (55, 210), (65, 195), (90, 170), (110, 160)]
surface = 60
print("Surface m² ; consommation kWh EP/m²/an :", logements)
```

Sortie exécutée :

```text
Surface m² ; consommation kWh EP/m²/an : [(45, 220), (55, 210), (65, 195), (90, 170), (110, 160)]
```

### Retenir les trois plus proches

Le voisinage se définit dans l’espace des caractéristiques. Ici, la distance est simplement la différence de surface.

```python
voisins = sorted(logements, key=lambda p: abs(p[0]-surface))[:3]
print("Trois voisins du logement de 60 m² :", voisins)
```

Sortie exécutée :

```text
Trois voisins du logement de 60 m² : [(55, 210), (65, 195), (45, 220)]
```

### Produire une estimation et un repère

On moyenne les cibles des voisins ; la médiane globale sert de référence simple. Cette comparaison n’est pas un score de test.

```python
from statistics import mean, median
estimation = mean(y for x,y in voisins)
reference = median(y for x,y in logements)
resultats = [("Voisins", estimation), ("Médiane", reference)]
print(f"Estimation : {estimation:.1f} ; référence : {reference:.1f} kWh EP/m²/an")
```

Sortie exécutée :

```text
Estimation : 208.3 ; référence : 195.0 kWh EP/m²/an
```

### À essayer

Changez surface à 100 : observez les voisins retenus. Puis imaginez deux logements de même surface, l’un isolé, l’autre non : quelle variable manque ?

### Passage aux données réelles

Le dossier DPE réel reste lié dans l’article. Pour une nouvelle expérience, séparer les adresses entre apprentissage et test ; standardiser les variables sur le seul apprentissage.
