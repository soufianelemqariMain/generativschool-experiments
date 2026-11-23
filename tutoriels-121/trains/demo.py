# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Compter les trains concernés
mois = [(100,10),(20,8)]
print("Trains circulés / retardés :", mois)

# Calculer les taux mensuels
taux = [100*r/n for n,r in mois]
resultats = [("Mois A",taux[0]),("Mois B",taux[1])]
print("Taux mensuels (%) :", taux)

# Pondérer le bilan
global_pct = 100*sum(r for n,r in mois)/sum(n for n,r in mois)
print(f"Taux global : {global_pct:.1f} % ; moyenne simple : {sum(taux)/2:.1f} %")
