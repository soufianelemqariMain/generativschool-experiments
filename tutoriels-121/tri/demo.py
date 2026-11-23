# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Décrire l’état en plus de l’objet
objets = [("grille-pain",True,None),("grille-pain",False,True),("grille-pain",False,False)]
print("Objet / fonctionne / réparable :", objets)

# Séparer les embranchements
def parcours(fonctionne,reparable):
    if fonctionne: return "réemploi à examiner"
    if reparable is None: return "diagnostic nécessaire"
    return "réparation à examiner" if reparable else "filière adaptée à vérifier"
print([parcours(f,r) for o,f,r in objets])

# Conserver le diagnostic manquant
print("Cas sans diagnostic :", parcours(False,None))
resultats = [(parcours(f,r),i+1) for i,(o,f,r) in enumerate(objets)]
