# Passer d’une courbe prévue à un créneau

Un apprentissage linéaire simplifié entre température et puissance, puis un calcul de coût séparé. Les nombres sont fictifs.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Former des couples météo-réseau

La température doit être celle connue au moment de prévoir. Ici les quatre points sont artificiellement réguliers pour rendre la droite lisible.

## Ajuster la pente

La pente décrit combien de MW changent pour un degré dans ces exemples. Ce lien appris ne prouve pas une causalité isolée.

## Distinguer prévision et facture

À 8 °C la droite donne une puissance nationale. Le coût de l’appareil dépend, lui, de ses kWh et du contrat.

## À essayer

Ajoutez un point de grand froid qui s’écarte de la droite. Regardez comment la pente bouge ; une relation linéaire peut manquer certains régimes.

## Passage aux données réelles

Le modèle réseau réel nécessite calendrier, historiques et prévisions météo archivées ; réserver la fin de la chronologie. Une baisse nationale ne garantit pas un tarif domestique plus bas.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
