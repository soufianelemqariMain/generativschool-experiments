# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Distinguer végétation et périmètre
vegetation = [[1,1,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,1]]
cour = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
print("Pixels dans la cour :",sum(map(sum,cour)))

# Intersecter les deux masques
intersection = [[v*c for v,c in zip(vr,cr)] for vr,cr in zip(vegetation,cour)]
verts = sum(map(sum,intersection))
print("Pixels végétalisés dans la cour :",verts)

# Passer à une proportion
total = sum(map(sum,cour))
part = 100*verts/total
resultats = [("Végétalisé",verts),("Autre surface",total-verts)]
print(f"Part végétalisée : {part:.1f} %")
