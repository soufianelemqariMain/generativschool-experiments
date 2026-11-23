# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Ranger les ventes
a = [1800,2000,2100,2200,8000]
b = [2000,2100,2200,2500,8000]
print("Ventes A :", a, "; ventes B :", b)

# Prendre le centre
from statistics import median
resultats = [("Mois A",median(a)),("Mois B",median(b))]
print("Médianes €/m² :", resultats)

# Interpréter le changement
variation = 100*(median(b)/median(a)-1)
print(f"Variation de médiane : {variation:.2f} %")
print("Variation du même logement : impossible à déduire de ces listes")
