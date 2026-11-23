# AGRIBALYSE — protocole avant classement

Prototype de suggestions : l’IA rapproche les noms d’aliments, puis un filtre déterministe conserve les produits du même sous-groupe ayant un indicateur changement climatique inférieur. Le modèle ne calcule pas l’ACV, ne déduit ni nutrition ni allergènes et ne garantit pas une substitution acceptable. Comparaison à un tri du même sous-groupe par seul impact climatique.

Six points de départ fixés avant calcul : lasagnes viande (25081), couscous mouton (25029), hamburger (25413), sauce bolognaise (11114), pizza viande (25457), chili con carne (25111). Encodeur multilingue MiniLM, noms français seulement, similarité cosinus. Exclure même Code_AGB, sélectionner trois plus proches parmi candidats impact strictement inférieur du même sous-groupe. Présenter impacts exacts en kg CO2e/kg de produit et DQR. Ne pas comparer 1 kg cru à 1 kg cuit comme portions équivalentes. Pas d’entraînement, de mesure d’économies réalisées ni de score de pertinence humain inventé.

Test de cohérence uniquement : identifiants distincts, sous-groupe identique, impact source strictement plus élevé, calcul de variation exact. Examen éditorial des 18 suggestions après génération ; refus possibles conservés. Cette expérience est un prototype calculé, pas une évaluation de qualité de substitution.
