# Rapport de la passe réelle — 16 octobre 2026

Résultat exécuté : 15/20 attendus satisfaits, cinq échecs. Six cartes / deux publications ; petite évaluation de développement conçue avec connaissance du corpus et de l’algorithme, ni validation indépendante ni validation scientifique. Une passe de consolidation et une reproduction technique sans réglage.

| Groupe | Attendus satisfaits |
|---|---:|
| Recherche directe | 6/6 |
| Paraphrases | 0/3 |
| Hors corpus | 1/3 |
| Filtres | 4/4 |
| Abstention | 4/4 |

Sur 11 cas avec carte attendue, 8 premiers résultats pertinents, rappel à 3 moyen 8/11. Sur 9 abstentions attendues, 7 obtenues. Lien, attribution, licence, changements et niveau concordent avec les cartes importées pour toutes les sorties ; ce contrôle de métadonnées ne valide pas les affirmations biologiques. Les contrôles HTML couvrent les six cartes. Aucun modèle de langage ou encodeur, BM25, entraînement ou calcul externe exécuté. Le moteur est une couverture lexicale de mots, seuil hérité 0,60.

| Cas | Attendu | Obtenu | Verdict |
|---|---|---|---|
| Q01 | D01 | D01 | conforme |
| Q02 | D02 | D02 | conforme |
| Q03 | D03 | D03 | conforme |
| Q04 | D04 | D04 | conforme |
| Q05 | D05 | D05 | conforme |
| Q06 | D06 | D06 | conforme |
| Q07 | D01 | abstention | échec |
| Q08 | D02 | abstention | échec |
| Q09 | D04 | abstention | échec |
| Q10 | abstention | D01 | échec |
| Q11 | abstention | D04 | échec |
| Q12 | abstention | abstention | conforme |
| Q13 | abstention | abstention | conforme |
| Q14 | D04 | D04 | conforme |
| Q15 | D01 | D01 | conforme |
| Q16 | abstention | abstention | conforme |
| Q17 | abstention | abstention | conforme |
| Q18 | abstention | abstention | conforme |
| Q19 | abstention | abstention | conforme |
| Q20 | abstention | abstention | conforme |

Q07–Q09 : la couverture lexicale ne retrouve pas les trois paraphrases. Q10 (« suivi médian de 7,6 ans en astronomie ») retourne D01 ; Q11 (« publication 2017 modèle souris diabète ») retourne D04. Le partage de mots franchit le seuil sans compréhension du sujet. Aucune correction postérieure à la mesure. Les gardes lexicales ne détectent pas toutes les intentions et ne démontrent aucune sûreté médicale générale.

## Ressources réellement mesurées

Python 3.9.6 (default, May 22 2026, 11:13:45) 
[Clang 21.0.0 (clang-2100.1.1.101)], Darwin 25.2.0 arm64. Adaptateur 1.0.0, moteur 0.1.0. Bibliothèque standard uniquement. Passe initiale : 0.006077584 s murales, 0.005735000 s CPU, pic RSS 22298624 octets. Reproduction : 0.004946125 s murales, 0.004818000 s CPU, pic RSS 22511616 octets.

Mesures internes couvrant lecture, contrôles, recherche et exports, hors démarrage Python, recherche documentaire et rédaction. RSS : pic du processus entier. Les deux commandes ont terminé en moins d’une seconde chacune selon l’outil terminal ; limite CPU dure 60 s par processus, budget demandé 900 s non approché. Aucun benchmark statistique de latence, énergie ou coût total. Aucun achat, API payante, téléchargement de poids ou installation. Les mesures isolées ne permettent pas de comparer des machines.

## Reproductibilité et limites

Les deux fichiers queries.json sont égaux après retrait du seul champ wall_seconds ; classement, texte, score, filtres et verdicts identiques. Corpus identique octet pour octet à l’entrée research/corpus.json ; hash ec265866c8ea14a1d3030d8650da4c690c14fe12cb7d9bd83de2c0423753fcb4. Gel enregistré avant exécution dans freeze.json. Les hashes ne sont ni une signature externe ni une preuve de véracité des sources.

Vérification documentaire et correction S08 détaillées dans SOURCES.md. Deux sources ne démontrent aucune performance générale. Une utilité pour des lecteurs et un éventuel gain par encodeur restent des hypothèses non testées. Comparaison ouverte non exécutée : aucun poids chargé, périmètre maintenu sans téléchargement/installation. Les textes français incluent des limites éditoriales et ne doivent pas être présentés comme des citations originales.

Le paquet ne contient que code, cartes attribuées, protocole et traces sélectionnées. Pas de dossier research complet, de texte institutionnel restreint, de ressource privée, de données individuelles ou de méthode biologique. Le site et la recherche ne sont pas modifiés. Aucun commit, push ou lancement public. Prochaine étape : revue indépendante et décision éditoriale du directeur ; publication uniquement selon autorisation du fondateur.
