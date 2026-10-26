# RappelConso — protocole avant calcul

26 octobre 2026. Prototype pédagogique, sans entraînement spécifique et sans service d'alerte réel.

Question : un encodeur multilingue préentraîné aide-t-il à retrouver une fiche connue à partir d'une description reformulée ? Comparaison sur le même corpus gelé, sans ajustement après lecture des scores.

Corpus : 1 000 fiches RappelConso les plus récentes à la date du prélèvement, tri date décroissante puis numéro de fiche ; préserver identifiants, version, référence officielle et champs produits. Dernière version de chaque numéro retenue. Ne pas indexer le motif sanitaire pour en déduire la sécurité d'un produit.

Modèle : sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2, Apache 2.0 ; encoder libellé produit, marque, catégorie, sous-catégorie, modèle/référence, conditionnement. Similarité cosinus. Révision exacte enregistrée au téléchargement. Pas d'API payante.

Comparateurs : TF-IDF caractères 3–5, TF-IDF mots 1–2. Apprentissage du vocabulaire sur le corpus documentaire, normal pour une recherche documentaire. Aucun GTIN fourni aux requêtes de reformulation ; lorsqu'il est connu, la recherche exacte reste préférable.

Évaluation : 24 requêtes éditoriales écrites à partir de fiches du corpus avant tout classement. Deux formulations par cible sur 12 cibles couvrant plusieurs catégories : description proche et description reformulée. Cible connue, pas annotation exhaustive de toutes les fiches pertinentes. Mesurer présence de la cible dans top 1/top 5 et MRR. Le nom exact de la métrique est taux de retrouvaille de la fiche cible, pas rappel exhaustif ni qualité d'une alerte. Aucun réglage après scores. Les cibles sont choisies pour diversité et lisibilité : panel construit non représentatif, pas utilisateurs réels, pas test indépendant.

Sauvegarder chaque rang et top 5, y compris échecs. Expliquer les limites : une fiche ressemblante ne prouve pas qu'un produit est concerné ; vérifier marque/référence, GTIN, lot, dates et consignes officielles. Absence de résultat ne signifie jamais absence de risque. Le corpus gelé n'est pas une liste d'alertes actuelles.

Contrôles : unicité des fiches, validité des identifiants cibles, hashes fichiers, scores recalculables depuis embeddings gelés, résultats déterministes CPU. Pas de données personnelles de lecteur collectées.
