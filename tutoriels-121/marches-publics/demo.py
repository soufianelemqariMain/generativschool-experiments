# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Séparer objet et date
from datetime import date
jour = date(2026,11,1)
avis = [("A","entretien espaces verts",date(2026,10,30)),("B","entretien parc",date(2026,12,1)),("C","mobilier bureau",date(2026,12,4))]
print("Date de recherche :", jour)

# Retirer les délais dépassés
ouverts = [a for a in avis if a[2]>=jour]
print("Avis encore ouverts :", [a[0] for a in ouverts])

# Classer les candidats, puis lire les pièces
mots = {"entretien","espaces","verts"}
resultats = sorted([(i,len(set(t.split()) & mots)) for i,t,d in ouverts],key=lambda p:-p[1])
print("Correspondances lexicales :", resultats)
print("Éligibilité de l’entreprise : non vérifiée")
