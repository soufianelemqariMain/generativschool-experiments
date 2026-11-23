# TGV — protocole avant évaluation

Question : un modèle entraîné sur les historiques de régularité aide-t-il à anticiper la proportion de trains en retard à l’arrivée d’une liaison, mois par mois ? Pas la prédiction d’un train individuel.

Source : SNCF/AQST, régularité mensuelle par liaison, ODbL. Cible : 100 × trains en retard à l’arrivée / (trains prévus − annulations). Le seuil officiel dépend de la durée du trajet. Lignes nationales seulement. Retirer valeurs impossibles et doublons liaison/mois ; réindexer les mois pour que décalage signifie bien mois calendaire.

Modèle figé : RandomForestRegressor, 100 arbres, max_depth=8, min_samples_leaf=10, random_state=42, n_jobs=2. Variables : taux retardés de 2, 3 et 12 mois, moyenne des mois 2 à 7, mois cyclique, liaison encodée. Pas de causes, volumes ou retards du mois à prévoir. Délai de deux mois supposé ; archives révisées sans preuve de disponibilité historique.

Apprentissage jusqu’à décembre 2024, test de janvier 2025 à la dernière période disponible. Modèle fixe sans réentraînement. Comparateurs : même mois année précédente et dernier mois utilisable (M−2). Même panel complet pour tous. MAE en points de pourcentage, pondération égale par liaison/mois puis par nombre de trains réalisés ; ce dernier poids sert seulement à l’évaluation. Résultats par année. Pas de réglage après scores. Pas d’économie ou de fiabilité individuelle démontrée.
