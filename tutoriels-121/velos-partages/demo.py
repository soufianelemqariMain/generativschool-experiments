# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Distinguer intentions et locations
stock = 2
intentions = [1,1,1,1,1]
print("Stock initial :", stock, "; personnes souhaitant partir :", len(intentions))

# Faire partir seulement les vélos présents
locations = 0
refus = 0
for demande in intentions:
    if stock >= demande:
        stock -= demande
        locations += demande
    else:
        refus += demande
print("Locations observées :", locations, "; stock final :", stock)

# Montrer la partie invisible
resultats = [("Locations",locations),("Demandes refusées",refus)]
print("Demande totale simulée :", locations+refus)
print("Une archive de locations seule ne voit que", locations)
