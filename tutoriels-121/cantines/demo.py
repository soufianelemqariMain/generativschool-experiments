# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Observer les présences après le service
services = [(200,180),(180,171),(210,189),(190,180)]
print("Réservés / servis :", services)

# Estimer le taux pour demain
taux = sum(s for r,s in services)/sum(r for r,s in services)
print(f"Taux appris : {taux:.1%} ; attente : {200*taux:.1f} repas")

# Décider sous plusieurs présences possibles
scenarios = [180,190,200]
def cout(q, n):
    return max(q-n,0) + 4*max(n-q,0)
resultats = [(str(q)+" repas", sum(cout(q,n) for n in scenarios)/3) for q in scenarios]
print("Coûts moyens (unités conventionnelles) :", resultats)
print("Choix pour ces hypothèses :", min(resultats,key=lambda p:p[1])[0])
