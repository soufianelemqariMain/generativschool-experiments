# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Décrire des logements comparables
logements = [(45, 220), (55, 210), (65, 195), (90, 170), (110, 160)]
surface = 60
print("Surface m² ; consommation kWh EP/m²/an :", logements)

# Retenir les trois plus proches
voisins = sorted(logements, key=lambda p: abs(p[0]-surface))[:3]
print("Trois voisins du logement de 60 m² :", voisins)

# Produire une estimation et un repère
from statistics import mean, median
estimation = mean(y for x,y in voisins)
reference = median(y for x,y in logements)
resultats = [("Voisins", estimation), ("Médiane", reference)]
print(f"Estimation : {estimation:.1f} ; référence : {reference:.1f} kWh EP/m²/an")
