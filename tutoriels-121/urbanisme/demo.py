# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Identifier parcelle, zone et version
documents = [("2024","UA","hauteur maximale 9 metres"),("2026","UA","hauteur maximale 12 metres"),("2026","UB","hauteur maximale 6 metres")]
version, zone = "2026","UA"
print("Corpus :",documents)

# Fermer le corpus avant la recherche
corpus = [texte for v,z,texte in documents if v==version and z==zone]
print("Corpus applicable supposé :",corpus)

# Rendre le passage et sa provenance
passages = [texte for texte in corpus if "hauteur" in texte]
print("Passage :",passages[0] if passages else "aucun passage — réponse impossible")
print("Provenance : zone",zone,"; version",version,"; annexes non examinées")
resultats = [("Documents initiaux",len(documents)),("Après filtre",len(corpus)),("Passages",len(passages))]
