# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Mesurer à intervalles connus
mesures = [(0,50),(1,60),(2,70)]
print("Heure / remplissage (%) :",mesures)

# Apprendre le rythme moyen
from statistics import mean
mx = mean(x for x,y in mesures)
my = mean(y for x,y in mesures)
pente = sum((x-mx)*(y-my) for x,y in mesures)/sum((x-mx)**2 for x,y in mesures)
base = my-pente*mx
print("Rythme appris :",pente,"points/h")

# Transformer le rythme en délai
saturation = (100-base)/pente if pente>0 else None
resultats = [(f"{h} h",min(100,base+pente*h)) for h in range(6)]
print("Saturation depuis le début :",saturation,"h")
print("Temps restant après le dernier relevé :",saturation-mesures[-1][0],"h")
