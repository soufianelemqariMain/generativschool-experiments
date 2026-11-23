## Apprendre une vitesse, prévoir la saturation

Une droite ajustée sur trois mesures fictives de remplissage. Le dépassement de 100 % est tronqué pour l’affichage, pas pour prétendre à une mesure physique.

### Mesurer à intervalles connus

Les heures sont comptées depuis le premier relevé ; le remplissage s’exprime en %.

```python
mesures = [(0,50),(1,60),(2,70)]
print("Heure / remplissage (%) :",mesures)
```

Sortie exécutée :

```text
Heure / remplissage (%) : [(0, 50), (1, 60), (2, 70)]
```

### Apprendre le rythme moyen

La pente estime une progression en points de pourcentage par heure. Ce n’est pas une croissance relative de 10 %.

```python
from statistics import mean
mx = mean(x for x,y in mesures)
my = mean(y for x,y in mesures)
pente = sum((x-mx)*(y-my) for x,y in mesures)/sum((x-mx)**2 for x,y in mesures)
base = my-pente*mx
print("Rythme appris :",pente,"points/h")
```

Sortie exécutée :

```text
Rythme appris : 10.0 points/h
```

### Transformer le rythme en délai

Une pente positive donne un délai théorique. Un ramassage ou un dépôt exceptionnel casse ce scénario.

```python
saturation = (100-base)/pente if pente>0 else None
resultats = [(f"{h} h",min(100,base+pente*h)) for h in range(6)]
print("Saturation depuis le début :",saturation,"h")
print("Temps restant après le dernier relevé :",saturation-mesures[-1][0],"h")
```

Sortie exécutée :

```text
Saturation depuis le début : 5.0 h
Temps restant après le dernier relevé : 3.0 h
```

### À essayer

Remplacez le dernier relevé par 55. La droite et le délai changent : trois observations ne suffisent pas à stabiliser une tournée.

### Passage aux données réelles

Tester sur des séquences de capteurs, marquer les collectes et comparer au dernier rythme connu ; séparer estimation de remplissage et optimisation des tournées.
