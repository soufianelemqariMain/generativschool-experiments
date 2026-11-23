# Préparer la prévention routière — protocole avant résultats

Question : peut-on anticiper le nombre mensuel d’accidents corporels enregistrés dans un département, en utilisant uniquement des historiques publiés avant l’année prévue ? Ne pas en déduire le risque d’une personne, d’un trajet ni l’effet causal d’une action de prévention.

Source : BAAC / ONISR, catalogue data.gouv.fr 53698f4ca3a729239d2036df, licence ouverte. Un accident = un identifiant unique du fichier caractéristiques ; aucun fichier de victimes ni nom. Métropole, 96 départements. Agréger par année/mois/département ; conserver zéro pour un mois sans ligne dans un fichier annuel complet. Archives révisées : les dates de publication sont vérifiées au catalogue, pas une reconstitution historique de chaque version.

Disponibilité : pour une prévision de toute l’année 2025 produite en janvier 2025, les résultats 2023 sont disponibles, ceux de 2024 ne le sont pas. Utiliser des retards de 24, 36 et 48 mois pour chaque mois cible ; pas de retard de 12 mois. Entraîner jusqu’à 2023 inclus, tester janvier–décembre 2025 sans réentraînement. L’année 2024 n’est pas utilisée. Les années antérieures servent à construire les retards. Le modèle ne voit pas les variables météo, collisions ou victimes de l’année prévue.

Modèle figé : RandomForestRegressor, n_estimators=120, max_depth=8, min_samples_leaf=12, random_state=42, n_jobs=2. Entrées : département one-hot, sinus/cosinus du mois, nombres du même mois 2/3/4 ans avant et leur moyenne. Baselines : même mois deux ans avant ; moyenne de ces trois historiques. Même ensemble de lignes pour tous. Aucun ajustement après consultation des résultats.

Mesures : MAE en accidents par département-mois, MAE par trimestre et département, somme prévue et observée. Vérifier non-négativité, absence de doublons, séparation temporelle et invariance des entrées d’entraînement lorsque les nombres 2025 sont modifiés. Les années Covid sont conservées et signalées. Le nombre d’accidents enregistrés n’est ni un dénombrement exhaustif de tout incident, ni un taux rapporté au trafic.
