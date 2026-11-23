# LOVAC — protocole avant calcul

Prévoir le nombre communal de logements privés vacants au millésime suivant à partir de deux millésimes passés et du parc privé connu. Pas de localisation de logements, pas d’explication causale de vacance. Source LOVAC 2020–2026 en géographie 2026 ; données secrétisées « s » traitées comme manquantes, jamais comme zéro.

Exemples apprentissage : cibles 2023, 2024, 2025. Cible test 2026. Variables : vacance totale à y−1 et y−2, différence, parc privé FF de y−2 (ne pas utiliser le stock contemporain). Régression Ridge alpha=10 après standardisation ; forêt 100 arbres, profondeur 10, feuille 20, graine 42. Comparateur : vacance inchangée. Résultats MAE en logements par commune et médiane erreur absolue, par région. Aucun réglage après résultats. Même panel complet pour tous. Archives révisées et changement géographique empêchent une validation opérationnelle historique. Les petites communes secrétisées sont sous-représentées.
