# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Lire ce que mesure le capteur
sol = 100
profondeurs = [10,11,10,9,9,10]
niveaux = [sol-p for p in profondeurs]
print("Niveaux d’eau (m) :", niveaux)

# Décaler la pluie avant de comparer
pluie = [0,20,10,0,0,5]
paires = list(zip(pluie[:-1],niveaux[1:]))
print("Pluie J / niveau J+1 :", paires)

# Préparer la cible sans surinterpréter
variations = [b-a for a,b in zip(niveaux,niveaux[1:])]
resultats = [(f"J{i+1}",v) for i,v in enumerate(niveaux)]
print("Variations quotidiennes (m) :", variations)
print("Nombre de couples :",len(paires),"; insuffisant pour valider une réponse à la pluie")
