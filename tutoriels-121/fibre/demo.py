# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Rassembler incidents et lignes
territoires = {"A":(10,100),"B":(10,10000)}
print("Incidents / lignes :",territoires)

# Diviser par la population exposée
resultats = [(k,100*i/n) for k,(i,n) in territoires.items()]
print("Incidents pour 100 lignes :",resultats)

# Préciser ce qui reste inconnu
print("Rapport des fréquences :",resultats[0][1]/resultats[1][1])
print("Lignes distinctes touchées : non renseignées")
