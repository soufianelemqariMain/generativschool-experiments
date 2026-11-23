# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Fixer une référence
historique = [79,80,81,80,79,81]
nouveau = 65
print("Historique de rendement (%) :", historique)

# Standardiser l’écart
from statistics import mean, pstdev
centre, dispersion = mean(historique), pstdev(historique)
z = (nouveau-centre)/dispersion
print(f"Centre : {centre:.1f} % ; écart standardisé : {z:.2f}")

# Envoyer une alerte à vérifier
alerte = abs(z)>3
resultats = [("Habituel",centre),("Nouvelle déclaration",nouveau)]
print("Dossier à vérifier :", alerte)
print("Cause connue : non ; contrôler déclaration, exploitation, puis réseau")
