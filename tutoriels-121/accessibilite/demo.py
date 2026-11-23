# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Conserver les valeurs inconnues
lieux = {"A":{"plain_pied":True,"porte_large":True},"B":{"plain_pied":True,"porte_large":None},"C":{"plain_pied":False,"porte_large":True}}
print(lieux)

# Calculer trois statuts distincts
def statut(c):
    if False in c.values(): return "contrainte identifiée"
    if None in c.values(): return "information manquante"
    return "critères renseignés compatibles"
for nom,c in lieux.items(): print(nom,statut(c))

# Produire une question utile
for nom,c in lieux.items():
    inconnus = [k for k,v in c.items() if v is None]
    if inconnus: print(nom,"— à confirmer :",inconnus)
resultats = [(nom,sum(v is True for v in c.values())) for nom,c in lieux.items()]
