# Électricité — protocole avant calcul

Prévision pédagogique de la demande française à 24 heures avec consommation passée et calendrier. RTE éCO2mix consolidé, snapshot 2023–2026. Conserver observations réalisées demi-horaires, moyenne horaire seulement si deux observations valides. Index UTC régulier ; calendrier en Europe/Paris. Les révisions sont inconnues à l'origine : évaluation rétrospective, pas validation opérationnelle.

Apprentissage fixe 2023–2024 ; test 2025–dernière donnée. Entrées disponibles 24 heures avant cible : consommations retardées de 24, 48 et 168 heures, moyenne des 24 observations de t−47 à t−24, heure/jour de semaine/mois cycliques. Régression Ridge alpha=10 après standardisation sur apprentissage ; forêt 80 arbres profondeur 12 feuille minimale 20 graine 42. Comparateurs : même heure veille/semaine précédente. RTE J−1 comparateur externe séparé, jamais variable. Pas de météo disponible dans le prototype. Aucun réglage après lecture des scores.

MAE en MW sur mêmes observations, par année et sur pointes définies par seuil 90e percentile de l'apprentissage. Modèles fixes sans réentraînement. Ne mesure pas facture, CO2 marginal ou effet d'un décalage de consommation.
