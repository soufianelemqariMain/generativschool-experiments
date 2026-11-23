## Un taux de retard a un dénominateur

Une agrégation de deux mois fictifs qui explique la cible d’un futur modèle de liaison.

### Compter les trains concernés

On ne mélange pas ici retards et annulations. Leur périmètre doit être documenté dans une vraie série.

```python
mois = [(100,10),(20,8)]
print("Trains circulés / retardés :", mois)
```

Sortie exécutée :

```text
Trains circulés / retardés : [(100, 10), (20, 8)]
```

### Calculer les taux mensuels

Chaque taux décrit une liaison sur un mois, pas la probabilité personnelle garantie d’un train réservé.

```python
taux = [100*r/n for n,r in mois]
resultats = [("Mois A",taux[0]),("Mois B",taux[1])]
print("Taux mensuels (%) :", taux)
```

Sortie exécutée :

```text
Taux mensuels (%) : [10.0, 40.0]
```

### Pondérer le bilan

La moyenne simple donnerait autant de poids au petit mois qu’au grand. Le taux global rapporte les retards à tous les trains circulés.

```python
global_pct = 100*sum(r for n,r in mois)/sum(n for n,r in mois)
print(f"Taux global : {global_pct:.1f} % ; moyenne simple : {sum(taux)/2:.1f} %")
```

Sortie exécutée :

```text
Taux global : 15.0 % ; moyenne simple : 25.0 %
```

### À essayer

Augmentez le nombre de trains du mois B à 200 en gardant son taux à 40 %. Observez ce qui arrive au taux global.

### Passage aux données réelles

La prévision réelle doit réserver des mois futurs et être comparée au même mois de l’année précédente. Le dossier TGV contient les essais déjà exécutés.
