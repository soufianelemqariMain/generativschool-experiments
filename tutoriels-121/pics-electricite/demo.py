# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Former des couples météo-réseau
temperatures = [0, 5, 10, 15]
puissances = [70000, 65000, 60000, 55000]
print(list(zip(temperatures, puissances)))

# Ajuster la pente
from statistics import mean
mx, my = mean(temperatures), mean(puissances)
pente = sum((x-mx)*(y-my) for x,y in zip(temperatures,puissances))/sum((x-mx)**2 for x in temperatures)
interception = my-pente*mx
print(f"Puissance = {interception:.0f} + ({pente:.0f}) × température")

# Distinguer prévision et facture
prediction = interception+pente*8
resultats = [("0 °C",70000),("5 °C",65000),("8 °C prévu",prediction),("15 °C",55000)]
print(f"Prévision illustrative : {prediction:.0f} MW")
print(f"Appareil 1 kW pendant 2 h à 0,15 €/kWh : {1*2*.15:.2f} €")
