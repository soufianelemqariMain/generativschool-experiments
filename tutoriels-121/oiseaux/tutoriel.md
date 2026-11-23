## Voir deux fréquences dans un fragment sonore

Une transformée de Fourier directe sur un signal synthétique. Elle ne reconnaît aucune espèce.

### Construire un son connu

128 échantillons à 128 Hz représentent une seconde. Les deux fréquences très basses servent uniquement à rendre l’exemple simple.

```python
from math import sin, cos, pi, hypot
fs, n = 128,128
signal = [sin(2*pi*8*i/fs)+.5*sin(2*pi*20*i/fs) for i in range(n)]
print("Durée :",n/fs,"s ; échantillons :",n)
```

Sortie exécutée :

```text
Durée : 1.0 s ; échantillons : 128
```

### Mesurer les composantes

Pour chaque fréquence on projette le signal sur un sinus et un cosinus. Un spectrogramme répéterait ce calcul sur des fenêtres successives.

```python
spectre = []
for k in range(n//2):
    re = sum(x*cos(2*pi*k*i/n) for i,x in enumerate(signal))
    im = -sum(x*sin(2*pi*k*i/n) for i,x in enumerate(signal))
    spectre.append((k*fs/n,2*hypot(re,im)/n))
print("Fréquences calculées :",len(spectre))
```

Sortie exécutée :

```text
Fréquences calculées : 64
```

### Retrouver ce que l’on a construit

Les deux pics retrouvent les composantes injectées, pas deux oiseaux.

```python
pics = sorted(spectre,key=lambda p:-p[1])[:2]
resultats = [(f"{f:g} Hz",round(a,3)) for f,a in pics]
print("Pics (Hz, amplitude) :",resultats)
```

Sortie exécutée :

```text
Pics (Hz, amplitude) : [('8 Hz', 1.0), ('20 Hz', 0.5)]
```

### À essayer

Remplacez 20 par 24 dans le signal : le second pic doit suivre. Sur un vrai enregistrement, vent et moteurs produisent aussi des motifs.

### Passage aux données réelles

Un modèle d’espèces doit être entraîné sur des enregistrements annotés ; séparer sites et sessions de test, puis vérifier les candidats à l’écoute.
