# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Ranger les concentrations dans le temps
jours = [12,14,13,18,25,20]
print("PM2,5 journaliers (µg/m³) :", jours)

# Émettre avant d’observer
predictions = jours[:-1]
observations = jours[1:]
print("Prévu / observé :", list(zip(predictions, observations)))

# Mesurer ce qu’il faudra battre
from statistics import mean
mae = mean(abs(p-y) for p,y in zip(predictions,observations))
resultats = [(f"J{i+2}", y) for i,y in enumerate(observations)]
print(f"Référence à battre : {mae:.2f} µg/m³")
