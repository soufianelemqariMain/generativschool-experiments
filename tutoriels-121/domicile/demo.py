# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Écrire les visites et déplacements
visites = [60,60,60]
trajets = [20,20]
print("Visites (min) :",visites,"; trajets (min) :",trajets)

# Construire une chronologie
minute = 0
resultats = []
for i,duree in enumerate(visites):
    resultats.append((f"Visite {i+1}",duree))
    print(f"Visite {i+1} : minute {minute} à {minute+duree}")
    minute += duree
    if i<len(trajets): minute += trajets[i]

# Comparer au temps disponible
disponible = 210
print("Temps nécessaire :",minute,"min")
print("Dépassement :",max(0,minute-disponible),"min")
