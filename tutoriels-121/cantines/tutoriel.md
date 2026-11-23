## Apprendre une présence, choisir une préparation

Un taux de présence estimé sur quatre services fictifs, puis une décision tenant compte du coût du manque.

### Observer les présences après le service

Une réservation est une entrée ; le nombre servi devient la cible seulement une fois la journée terminée.

```python
services = [(200,180),(180,171),(210,189),(190,180)]
print("Réservés / servis :", services)
```

Sortie exécutée :

```text
Réservés / servis : [(200, 180), (180, 171), (210, 189), (190, 180)]
```

### Estimer le taux pour demain

La somme des présences divisée par celle des réservations pondère correctement les journées. Demain, on connaît 200 réservations.

```python
taux = sum(s for r,s in services)/sum(r for r,s in services)
print(f"Taux appris : {taux:.1%} ; attente : {200*taux:.1f} repas")
```

Sortie exécutée :

```text
Taux appris : 92.3% ; attente : 184.6 repas
```

### Décider sous plusieurs présences possibles

On chiffre trois scénarios équiprobables. Le coût fictif d’un repas manquant vaut quatre fois celui d’un surplus. Ce choix relève de l’équipe, pas du modèle.

```python
scenarios = [180,190,200]
def cout(q, n):
    return max(q-n,0) + 4*max(n-q,0)
resultats = [(str(q)+" repas", sum(cout(q,n) for n in scenarios)/3) for q in scenarios]
print("Coûts moyens (unités conventionnelles) :", resultats)
print("Choix pour ces hypothèses :", min(resultats,key=lambda p:p[1])[0])
```

Sortie exécutée :

```text
Coûts moyens (unités conventionnelles) : [('180 repas', 40.0), ('190 repas', 16.666666666666668), ('200 repas', 10.0)]
Choix pour ces hypothèses : 200 repas
```

### À essayer

Passez le coefficient du manque de 4 à 1. La décision peut changer sans réentraîner le taux de présence.

### Passage aux données réelles

Il faut un historique quotidien local ; Ma cantine ne fournit pas à elle seule ces cibles. Tester hors période d’apprentissage et convenir des coûts avec les équipes.
