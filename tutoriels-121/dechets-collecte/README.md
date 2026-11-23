# Apprendre une vitesse, prévoir la saturation

Une droite ajustée sur trois mesures fictives de remplissage. Le dépassement de 100 % est tronqué pour l’affichage, pas pour prétendre à une mesure physique.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Mesurer à intervalles connus

Les heures sont comptées depuis le premier relevé ; le remplissage s’exprime en %.

## Apprendre le rythme moyen

La pente estime une progression en points de pourcentage par heure. Ce n’est pas une croissance relative de 10 %.

## Transformer le rythme en délai

Une pente positive donne un délai théorique. Un ramassage ou un dépôt exceptionnel casse ce scénario.

## À essayer

Remplacez le dernier relevé par 55. La droite et le délai changent : trois observations ne suffisent pas à stabiliser une tournée.

## Passage aux données réelles

Tester sur des séquences de capteurs, marquer les collectes et comparer au dernier rythme connu ; séparer estimation de remplissage et optimisation des tournées.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
