# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Décrire les livres par thèmes
livres = {"A":{"espace","aventure"},"B":{"espace","aventure","robot"},"C":{"jardin","societe"},"D":{"robot","societe"}}
interets = {"espace","aventure"}
print({k: sorted(v) for k,v in livres.items()})

# Trouver les voisins évidents
scores = {k:len(v & interets) for k,v in livres.items()}
resultats = sorted(scores.items(),key=lambda p:-p[1])
print("Voisins :",resultats)

# Composer un voisin et un détour
premier = resultats[0][0]
detour = min((k for k in livres if k!=premier),key=lambda k:len(livres[k]&livres[premier]))
print("Voisin :",premier,"; détour :",detour)
