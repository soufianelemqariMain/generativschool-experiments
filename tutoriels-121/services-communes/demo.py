# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Encoder trois équipements
communes = {"A":(1,1,0),"B":(1,0,0),"C":(1,1,1),"D":(0,0,1)}
print("École, pharmacie, bibliothèque :", communes)

# Compter les différences
def distance(a,b):
    return sum(x!=y for x,y in zip(a,b))
resultats = [(k,distance(communes["A"],v)) for k,v in communes.items() if k!="A"]
print("Différences avec A :", resultats)

# Ouvrir la comparaison
proches = [k for k,d in resultats if d==min(v for k,v in resultats)]
print("Voisines de profil :", proches)
print("Horaires, distances et capacité d’accueil : inconnus")
