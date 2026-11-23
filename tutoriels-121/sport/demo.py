# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Séparer budget, horaire et envie
activites = [("Course",0,18,True),("Tennis",25,18,True),("Natation",8,20,False)]
budget, heure_max = 10,19
print("Nom, euros, heure, dehors :",activites)

# Appliquer les contraintes dures
possibles = [a for a in activites if a[1]<=budget and a[2]<=heure_max]
print("Faisables :",[a[0] for a in possibles])

# Classer ce qui reste
resultats = [(a[0],int(a[3])) for a in sorted(possibles,key=lambda a:not a[3])]
print("Préférence plein air :",resultats)
