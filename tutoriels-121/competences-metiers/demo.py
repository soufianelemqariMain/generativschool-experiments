# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Décrire ce qui a été fait
acquis = {"planifier", "accueillir", "coordonner"}
metiers = {"logistique":{"planifier","coordonner","conduire"}, "accueil":{"accueillir","informer"}, "vente":{"negocier","informer"}}
print("Déclaré :", sorted(acquis))

# Chercher les recouvrements
resultats = [(m,len(acquis & c)) for m,c in metiers.items()]
print("Compétences communes :", resultats)

# Nommer ce qui reste à vérifier
cible = max(resultats,key=lambda p:p[1])[0]
print("Piste :", cible)
print("À confirmer ou acquérir :", sorted(metiers[cible]-acquis))
