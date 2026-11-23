# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Séparer description et identifiants
fiches = [dict(id="A", texte="peluche gateau enfant", lot="L12"), dict(id="B", texte="gateau chocolat", lot="L98"), dict(id="C", texte="peluche ours", lot="L07")]
requete = set("peluche gateau".split())
print("Demande :", sorted(requete))

# Classer sans confondre proximité et preuve
def score(f):
    mots = set(f["texte"].split())
    return len(mots & requete)/len(mots | requete)
classement = sorted(fiches, key=score, reverse=True)
resultats = [(f["id"], round(score(f),3)) for f in classement]
print("Scores lexicaux :", resultats)

# Contrôler le lot
lot_detenu = "L13"
candidate = classement[0]
print("Fiche candidate :", candidate["id"])
print("Lot correspondant :", candidate["lot"] == lot_detenu)
