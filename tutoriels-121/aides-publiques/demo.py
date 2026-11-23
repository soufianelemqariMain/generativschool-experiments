# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Décrire les critères connus
criteres = {"porteur":True,"territoire":True,"calendrier":None}
print(criteres)

# Appliquer une logique à trois états
def statut(c):
    if False in c.values(): return "critère bloquant"
    if None in c.values(): return "à compléter"
    return "critères examinés satisfaits"
print("Dossier :", statut(criteres))

# Rendre la question suivante explicite
manquants = [k for k,v in criteres.items() if v is None]
resultats = [(k,1 if v is True else 0) for k,v in criteres.items()]
print("À documenter :", manquants)
print("Décision finale : consulter le règlement et l’organisme")
