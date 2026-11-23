# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Écrire le besoin en heures
besoin = (8,18)
creches = [("A",7,19,0),("B",9,18,2),("C",7,18,1)]
print("Besoin :",besoin,"; ouverture, fermeture, places :",creches)

# Vérifier toute la plage
compatibles = [(nom,places) for nom,debut,fin,places in creches if debut<=besoin[0] and fin>=besoin[1]]
print("Horaires compatibles :",compatibles)

# Distinguer compatibilité et admission
resultats = [(nom,n) for nom,n in compatibles]
print("Disponibilités positives à confirmer :",[nom for nom,n in compatibles if n>0])
