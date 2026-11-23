# -*- coding: utf-8 -*-
# Entrées pédagogiques fictives. Python 3.10+, bibliothèque standard.
# Garder la vérité terrain pour le test
cas = [(.1,0),(.2,0),(.4,1),(.55,0),(.7,1),(.9,1)]
print("Score / événement :",cas)

# Construire les quatre comptes
def bilan(seuil):
    vp = sum(s>=seuil and y==1 for s,y in cas)
    fp = sum(s>=seuil and y==0 for s,y in cas)
    fn = sum(s<seuil and y==1 for s,y in cas)
    vn = sum(s<seuil and y==0 for s,y in cas)
    return vp,fp,fn,vn
print("VP, FP, FN, VN :",bilan(.5))

# Comparer deux politiques
resultats = [("Manqués à 0,5",bilan(.5)[2]),("Manqués à 0,3",bilan(.3)[2])]
print("Seuil 0,5 :",bilan(.5),"; seuil 0,3 :",bilan(.3))
