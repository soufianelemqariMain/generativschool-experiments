# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Afficher capacités et prévisions
sites = {"Plage": [120,150], "Sentier": [80,60], "Jardin": [100,70]}
print("Capacité / passages prévus :", sites)

# Mesurer les places restantes
marges = {s:c-p for s,(c,p) in sites.items()}
print("Marges :", marges)

# Redistribuer sans dépasser la capacité
excedent = max(0,-marges["Plage"])
for s in ["Sentier","Jardin"]:
    transfert = min(excedent,max(0,marges[s]))
    sites[s][1] += transfert
    sites["Plage"][1] -= transfert
    excedent -= transfert
resultats = [(s,p) for s,(c,p) in sites.items()]
print("Après redistribution :", resultats)
