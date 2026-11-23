# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Construire un son connu
from math import sin, cos, pi, hypot
fs, n = 128,128
signal = [sin(2*pi*8*i/fs)+.5*sin(2*pi*20*i/fs) for i in range(n)]
print("Durée :",n/fs,"s ; échantillons :",n)

# Mesurer les composantes
spectre = []
for k in range(n//2):
    re = sum(x*cos(2*pi*k*i/n) for i,x in enumerate(signal))
    im = -sum(x*sin(2*pi*k*i/n) for i,x in enumerate(signal))
    spectre.append((k*fs/n,2*hypot(re,im)/n))
print("Fréquences calculées :",len(spectre))

# Retrouver ce que l’on a construit
pics = sorted(spectre,key=lambda p:-p[1])[:2]
resultats = [(f"{f:g} Hz",round(a,3)) for f,a in pics]
print("Pics (Hz, amplitude) :",resultats)
