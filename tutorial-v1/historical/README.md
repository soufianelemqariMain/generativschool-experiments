# Compagnon technique — atlas documentaire réel

Prototype limité, non publié. Six reformulations françaises, deux publications. **15/20 attendus satisfaits ; cinq échecs conservés. Aucune IA exécutée.** Aucun résultat biologique nouveau, donnée individuelle, diagnostic ou protocole biologique.

Testé sur macOS (Darwin 25.2.0 arm64), Python 3.9.6 ; Python 3.9+ requis, bibliothèque standard uniquement. L’évaluation dépend du module Unix `resource` et de `RLIMIT_CPU` : Windows natif non pris en charge par cette commande ; Linux non testé. Aucune compatibilité Linux/Windows n’est revendiquée. Depuis ce dossier :

```sh
python3 evaluate.py --out nouvelle-passe
python3 atlas.py corpus.json 'suivi médian' --level clinique --html recherche.html
```

Le répertoire de sortie doit être neuf. Ouvrir `results/atlas.html` pour le catalogue statique des six cartes ; la recherche fonctionne par CLI. `results/cards.json` contient les mêmes cartes et métadonnées. Les cartes ne sont pas des citations originales : l'export n'emploie ni blockquote ni champ quote. Chaque carte conserve attribution, source, repère, licence et changements. Le SHA contrôle seulement le texte local.

`freeze.json` fige corpus, protocole, attendus et code avant mesure. `results/` conserve la passe initiale, `reproduction/` une reproduction sans ajustement. Les traces synthétiques antérieures restent dans le dossier parent `technical/` ; elles ne font pas partie de ce paquet. `lexical_legacy.py` est la copie inchangée de leur moteur ; utiliser uniquement l'adaptateur `atlas.py` pour ce corpus éditorial.

Voir `REPORT.md`, `PROTOCOL.md`, `SOURCES.md`, `questions.json` et `MANIFEST.json`. Pour contrôler les empreintes du paquet :

```sh
python3 -c 'import hashlib,json,pathlib; p=pathlib.Path("."); m=json.loads((p/"MANIFEST.json").read_text()); assert all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in m["sha256"].items()); print("Intégrité locale OK — aucune validation de source")'
```

## Conditions de consultation et notices

Code rendu consultable ; aucune licence de réutilisation du code n’est accordée pour le moment. Ce compagnon n’est pas présenté comme open source. La licence CC BY 4.0 des publications ne s’applique pas aux scripts. Aucun titulaire juridique du code n’est désigné ici et aucune attribution du code à Paperclip n’est faite.

Lire [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) avec les cartes : bibliographies, copyright, licence des publications et changements éditoriaux, notamment D06 « réserve de la rédaction ». Ces notices complètent les exports historiques sans les modifier.

## Version documentaire public-v2 — 16 octobre 2026

Première correction après revue indépendante : droits du code explicités, notices complétées, plateformes précisées. Aucun nouveau benchmark, réglage ou résultat biologique. Corpus, questions, algorithme, protocole, gel et résultats historiques sont inchangés. `REPORT.md` et `SOURCES.md` conservent leur état historique ; la prochaine étape de revue annoncée dans le rapport a depuis eu lieu. La revue a reproduit les résultats logiciels ; elle ne valide pas les données biologiques.

Les 15/20 attendus et les cinq échecs restent visibles. L’utilité pour les lecteurs et les gains éventuels d’une IA restent des hypothèses non testées. Le manifeste public couvre cette version documentaire ; `freeze.json` conserve le gel de l’expérience initiale. Aucune empreinte locale ne valide une source distante.

Compagnon préparé, non publié dans cette correction. L’intégration, les URL réciproques avec l’article et le traitement des réserves éditoriales relèvent du directeur. Les archives internes et documents de tâche ne sont pas inclus.
