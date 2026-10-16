# Annexe de validation — assistant documentaire Généthon

Cette annexe sépare les résultats logiciels du bénéfice d’usage envisagé. La version value-v2 est une réécriture éditoriale : aucune expérience, inférence ni mesure de performance n’a été exécutée à nouveau pour elle.

## Résultats conservés sur vingt questions connues

| Version | Attentes satisfaites | Échecs conservés |
|---|---:|---|
| Moteur historique | 15/20 | Q07, Q08, Q09, Q10, Q11 |
| Normalisation 1.1.0 | 17/20 | Q07, Q10, Q11 |

Q08 et Q09 passent grâce aux équivalences lexicales, avec une couverture de 0,666667. Pour observer la correction, ouvrez leur ligne dans `comparison.json` et comparez `baseline` à `improved`, notamment `passed`, `hits` et `matched_terms`. Les trois règles montrées à l’étape 6 sont déjà dans la version livrée : il n’est pas nécessaire de les ajouter une seconde fois.

Q07 échoue encore : « personnes suivies » n’est pas rapproché de « participants ». Q10 et Q11 montrent une limite différente. Une question mêlant « suivi médian » et « astronomie » fait remonter D01 avec 0,75 ; une question mêlant « publication 2017 », « modèle souris » et « diabète » fait remonter D04 avec 0,8. Un lien bibliographique correct peut donc accompagner une réponse hors sujet.

Le handoff technique conserve deux exécutions dans des environnements virtuels neufs, avec les mêmes verdicts et sorties de comparaison. Les questions étaient connues pendant le développement : le passage à 17/20 ne démontre pas une généralisation. Pour une prochaine expérience, écrire d’abord des questions nouvelles, les tenir à l’écart des réglages et mesurer aussi les faux positifs. Ajouter seulement « astronomie » et « diabète » à une liste noire ne suffirait pas à établir un progrès général.


## Provenance des contrôles

Les traces techniques sont conservées dans [runs/clean-1](https://github.com/soufianelemqariMain/generativschool-experiments/tree/main/tutorial-v1/runs/clean-1) et clean-2 du même projet. Environnements : CPython 3.9.6, macOS 26.2 arm64, deux venv neufs, pas deux machines vierges. Les commandes terminal, sorties JSON/HTML, filtres, intégrité et contrat ont été contrôlés. Aucun modèle IA exécuté. Windows natif n’est pas pris en charge par l’évaluation utilisant resource ; Linux n’est pas testé dans ces traces.

La reproduction rédactionnelle de tutorial-v1, le 16 octobre 2026 à 20:07 UTC, a vérifié les 46 empreintes techniques et retrouvé la comparaison complète. La revue indépendante du Lab Director à 20:11 UTC a retrouvé les mêmes résultats dans un nouveau venv. Cette revue portait sur tutorial-v1, pas sur la présente réécriture. Elle ne constituait pas une inspection visuelle du navigateur. Ces contrôles d’intégrité ne valident ni les publications ni une efficacité médicale.

La distribution publique diffère du paquet technique source par sa documentation et ses manifestes. Le compte rendu d’intégration conserve la comparaison de 45 fichiers techniques hors README et de 91 fichiers publics ; ces vérifications antérieures ne sont pas revendiquées comme répétées ici.

## Sources, réserves et droits

Les cartes sont des reformulations françaises, pas des citations originales. D01–D03 renvoient à Magnani ; D04–D05 à Porro. D06 est une réserve rédactionnelle, sans résultat expérimental attribuable à Porro ; GNT0003 n’est pas documenté dans ce paquet. La correction Magnani du 9 août 2022 et les limites de sa vérification historique restent dans les notices. Les champs de licence, attribution et modification sont conservés.

L’identification de Généthon reste minimale ; aucun résumé institutionnel, logo, partenariat ou permission de Généthon n’est ajouté. Les conditions des liens institutionnels restent à apprécier lors de l’intégration ; cette réécriture ne tranche aucun droit nouveau. Le code reste consultable sans licence de réutilisation accordée ; les licences des publications sont distinctes.

L’extension Qwen demeure proposée : le validateur a reçu des chaînes fabriquées, aucune inférence ni installation de la combinaison Transformers/PyTorch n’a été validée. L’estimation de mémoire concerne les paramètres seuls. Aucune mesure de temps gagné, de bénéfice scientifique ou d’usage chez Généthon n’est disponible.

## Lire le tutoriel et consulter les traces

[Lire le tutoriel](https://www.generativschool.com/genethon-atlas-documentaire-avant-ia.html) · [Compagnon et fichiers techniques](https://www.generativschool.com/genethon-atlas-documentaire-avant-ia-compagnon.html) · [Notices et droits](https://www.generativschool.com/genethon-atlas-documentaire-avant-ia-notices.html).

La revue ciblée de la réécriture value-v2, le 16 octobre 2026, est favorable à son intégration. Elle porte sur la lisibilité, la fidélité aux traces existantes et la conservation du parcours technique ; aucun benchmark ni modèle IA n’a été relancé. Elle ne démontre pas de bénéfice d’usage.
