# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Lire six couples de mois
exemples = [(0, .5), (1, 1), (2, 1.5), (4, 4.5), (5, 5), (6, 5.5)]
test = [(1.5, 1.2), (5.5, 5.2)]
print("Passé connu → mois suivant (%) :", exemples)

# Laisser les exemples choisir la question
from statistics import mean
seuils = [(a[0]+b[0])/2 for a,b in zip(exemples, exemples[1:])]
def ajuster(seuil):
    gauche = [y for x,y in exemples if x <= seuil]
    droite = [y for x,y in exemples if x > seuil]
    bas, haut = mean(gauche), mean(droite)
    erreur = sum((y-(bas if x <= seuil else haut))**2 for x,y in exemples)
    return erreur, seuil, bas, haut
_, seuil, bas, haut = min(map(ajuster, seuils))
print(f"Question apprise : variation passée ≤ {seuil:g} % ?")
print(f"Oui : {bas:g} % ; non : {haut:g} %")

# Suivre une branche puis refaire le ticket
def prevoir(x):
    return bas if x <= seuil else haut
prediction = prevoir(4)
ticket = 60*(1+prediction/100) + 40*1.01
mae = mean(abs(prevoir(x)-y) for x,y in test)
resultats = [("Frais : hausse prévue", prediction), ("Autres : hypothèse", 1)]
print(f"Panier : {ticket:.2f} € ; erreur sur deux cas : {mae:.2f} point de %")
