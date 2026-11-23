# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Exprimer deux intérêts
interets = {"creer","biologie"}
formations = {"Design":{"creer","dessiner"},"Biologie":{"biologie","experimenter"},"Paysage":{"creer","biologie","terrain"}}
print("Intérêts :", sorted(interets))

# Compter les points de contact
resultats = [(nom,len(interets & contenu)) for nom,contenu in formations.items()]
print("Points de contact :", resultats)

# Ajouter une question par chemin
for nom,contenu in formations.items():
    print(nom, "— à découvrir :", ", ".join(sorted(contenu-interets)))
