# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Décomposer le déplacement
trajets = {"Direct":[(8,1),(4,.5),(3,1)], "Ombragé":[(10,.2),(6,.3),(3,1)]}
print("Minutes / fraction au soleil :", trajets)

# Pondérer chaque durée
def exposition(troncons):
    return sum(minutes*soleil for minutes,soleil in troncons)
resultats = [(nom,exposition(t)) for nom,t in trajets.items()]
print("Minutes équivalentes au soleil :", resultats)

# Mettre durée et exposition côte à côte
for nom,t in trajets.items():
    print(nom,":",sum(m for m,s in t),"min de trajet ;",round(exposition(t),1),"min équivalentes au soleil")
