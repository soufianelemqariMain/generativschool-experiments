# Rapport technique — tutorial-v1

Le parcours CLI et HTML est exécuté ; l’extension modèle est proposée, non exécutée. Tutoriel : README.md ; contrats et adaptateur : MODEL_EXTENSION.md et model_adapter.py. Matière destinée au rédacteur de GEN-15 et à la revue indépendante organisée par le Lab Director.

## Résultats réellement exécutés

- CPython 3.9.6, macOS 26.2 arm64 ; zéro dépendance tierce dans deux environnements virtuels neufs.
- Ancien moteur : 15/20 ; normalisation 1.1.0 : 17/20. Les sorties des deux passages sont identiques, comparaison complète vérifiée.
- Q08 et Q09 passent avec couverture 0,666667 ; Q07 reste en abstention ; Q10/D01 (0,75) et Q11/D04 (0,8) restent des faux positifs.
- Première passe : 0.581669 s murales ; 0.028815 s CPU principal ; 0.498135 s CPU enfants ; pic RSS du principal 22446080 octets. Ce pic n’est pas la mémoire agrégée des processus.
- Deuxième parcours, installation venv et commandes du README comprises : 1.084124 s murales, 1.042501 s CPU enfants. Détails conservés dans runs/install-transcript.json.
- Contrôles réellement exécutés : gel original, empreintes des textes, rejet licence invalide, filtres, contrats de sélection de références, CLI argumentée/interactive, export HTML et échappement, requête vide rejetée.
- Un premier lancement de check.py a échoué avant évaluation : le dossier parent runs/ manquait. Création des parents corrigée ; deux parcours réussis ensuite. Aucun résultat de benchmark n’a été supprimé ou réécrit pour masquer un échec.

Le budget CPU de 15 minutes n’a pas été approché. Ces mesures couvrent les processus testés, pas une mesure globale de la rédaction/navigation. Aucun modèle, achat, téléchargement de poids, API payante, site, DNS, email/X ou commit.

## Faits sourcés et hypothèses

Les références scientifiques, reformulations et corrections sont conservées dans historical/ ; D06 reste une réserve rédactionnelle et GNT0003 non documenté. La licence/version du modèle et les mesures GPU publiées sont sourcées dans MODEL_EXTENSION.md. Elles ne sont pas des mesures locales. L’estimation mémoire float32 est un calcul, non une exécution.

Le gain 17/20 est obtenu sur les questions connues pendant le développement. Ni généralisation, ni validation biologique, ni bénéfice utilisateur n’est démontré. Les faux positifs conservés interdisent de traiter une correspondance comme réponse médicale. L’utilité d’un modèle sélectionnant les références reste à établir ; son adaptateur n’a été testé que pour le contrat JSON avec données fabriquées.

## Intégrité et livraison

Les 22 fichiers du public-v2 original sont copiés sans changement dans historical/. Aucune modification des originaux, du site ou des autres répertoires de travail. MANIFEST.json inventorie les fichiers livrés hors lui-même, ZIP et empreintes externes ; le ZIP contient le manifeste. L’archive exclut environnements virtuels, caches et chemins locaux d’exécution. SHA-256 et contrôle CRC garantissent uniquement l’intégrité locale.

Le rédacteur peut reprendre les commandes et leur sortie réelle, l’architecture Mermaid, les contrats et le tableau de dépannage. Présenter 15/20 comme historique et 17/20 comme développement mesuré ; ne pas titrer « IA exécutée ». Suite : intégration rédactionnelle puis revue indépendante par le Lab Director, avant toute diffusion distinctement autorisée.
