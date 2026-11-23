# Comparer des logements avant d’estimer

Une régression par trois voisins sur un minuscule jeu fictif. La cible est une consommation conventionnelle, pas la facture ni l’économie de travaux.

## Exécuter

Python 3.10 ou plus, aucune dépendance ni clé.

```sh
python3 demo.py
```

Les entrées fictives sont définies au début du programme. Les sorties enregistrées figurent dans sorties.txt.

## Décrire des logements comparables

On fixe ici le type et la zone climatique ; seule la surface varie. Dans un vrai modèle, oublier l’isolation ou le chauffage serait une limite majeure.

## Retenir les trois plus proches

Le voisinage se définit dans l’espace des caractéristiques. Ici, la distance est simplement la différence de surface.

## Produire une estimation et un repère

On moyenne les cibles des voisins ; la médiane globale sert de référence simple. Cette comparaison n’est pas un score de test.

## À essayer

Changez surface à 100 : observez les voisins retenus. Puis imaginez deux logements de même surface, l’un isolé, l’autre non : quelle variable manque ?

## Passage aux données réelles

Le dossier DPE réel reste lié dans l’article. Pour une nouvelle expérience, séparer les adresses entre apprentissage et test ; standardiser les variables sur le seul apprentissage.

Le dessin SVG et les calques JSON partagent les valeurs calculées. Aucun résultat de terrain n’est établi par cette démonstration.
