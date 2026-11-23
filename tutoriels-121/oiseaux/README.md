# Voir deux fréquences dans un fragment sonore

Une transformée de Fourier directe sur un signal synthétique. Elle ne reconnaît aucune espèce.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Construire un son connu

128 échantillons à 128 Hz représentent une seconde. Les deux fréquences très basses servent uniquement à rendre l’exemple simple.

## Mesurer les composantes

Pour chaque fréquence on projette le signal sur un sinus et un cosinus. Un spectrogramme répéterait ce calcul sur des fenêtres successives.

## Retrouver ce que l’on a construit

Les deux pics retrouvent les composantes injectées, pas deux oiseaux.

## À essayer

Remplacez 20 par 24 dans le signal : le second pic doit suivre. Sur un vrai enregistrement, vent et moteurs produisent aussi des motifs.

## Passage aux données réelles

Un modèle d’espèces doit être entraîné sur des enregistrements annotés ; séparer sites et sessions de test, puis vérifier les candidats à l’écoute.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
