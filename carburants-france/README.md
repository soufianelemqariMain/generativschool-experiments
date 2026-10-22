# Carburants français et contexte international

Extension de l'expérience française : quatre carburants, comparaison de trois modèles d'IA et de deux règles simples sur les mêmes observations. Lire PROTOCOLE.md. Évaluation janvier–septembre 2026 ; données antérieures pour l'apprentissage. Les résultats de la première expérience 2025 étaient connus avant cette extension.

## Démarrer

[Lire l’article](https://www.generativschool.com/et-si-ia-anticipait-prix-carburant.html) · [Protocole](PROTOCOLE.md) · [Contrôles](VERIFICATION.md)

Pour récupérer le projet, utilisez **Code → Download ZIP** à la racine du dépôt, décompressez l’archive, puis ouvrez un terminal dans le dossier `carburants-france`. Avec Git :

```sh
git clone https://github.com/soufianelemqariMain/generativschool-experiments.git
cd generativschool-experiments/carburants-france
```

## Reproduire

Sur macOS ou Linux :

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
python crisis.py
python verify.py
```

Sur Windows, activez l’environnement avec `.venv\Scripts\activate.bat` dans l’invite de commandes. Cette plateforme n’a pas été vérifiée ici.

`results.json` contient la période complète, `crisis-results.json` la période utilisée dans l’article. Les erreurs sont exprimées en **euros par litre** dans les fichiers : multiplier par 100 pour obtenir des centimes par litre. Ce ne sont pas des économies mesurées.


Python 3.9.6 utilisé. Installer requirements.txt dans un environnement virtuel, puis `python run.py` et `python verify.py`. Après installation, aucun réseau, service payant ou clé n'est nécessaire. Les fichiers complets de contexte, déclarations extraites, résultats et empreintes sont inclus.

Pour contrôler l'extraction des stations, télécharger les archives de data/station-sources.json sous 2023.zip à 2026.zip puis lancer `python extract.py /chemin/archives`. L'archive 2026 évolue : la nouvelle version peut ne plus avoir la même empreinte. Les déclarations utilisées restent figées ici. Une modification de source doit créer une nouvelle version.

## Sources, droits et transformations

- Stations françaises : https://www.prix-carburants.gouv.fr/rubrique/opendata/ ; Licence ouverte https://www.etalab.gouv.fr/licence-ouverte-open-licence/ . Archives 2023–2026, téléchargées le 22 octobre 2026. Extraction par identifiant, carburant et date. Les trois valeurs hors [0,50 ; 4] €/l sont exclues. Le test s'arrête avant octobre.
- Brent mer du Nord : U.S. Energy Information Administration, https://www.eia.gov/dnav/pet/hist/RBRTED.htm ; réutilisation des données publiques EIA : https://www.eia.gov/about/copyrights_reuse.php . Prix en dollars/baril, transformé en euros/baril en divisant par USD pour un euro. Ce n'est pas une cotation de produit raffiné français.
- Change : Banque centrale européenne, taux de référence EUR/USD, https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html . Réutilisation avec attribution : https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html . Calculs dérivés et variations effectués par GenerativSchool ; pas de taux transactionnel garanti.
- Risque géopolitique : Dario Caldara et Matteo Iacoviello (2022), “Measuring Geopolitical Risk”, American Economic Review 112(4), 1194–1225 ; https://www.matteoiacoviello.com/gpr.htm . Données téléchargées le 22 octobre 2026, licence CC BY annoncée par les auteurs. Indice quotidien GPRD, moyenne mobile sept jours recalculée ici puis variation à 28 jours. Couverture de presse, pas corpus direct de déclarations ni preuve causale. Données révisables.

Les URL, dates et SHA-256 sont dans les deux fichiers sources JSON. Les observations macro sont décalées de 14 jours ; ce choix conservateur n'établit pas leur disponibilité historique exacte. Les derniers jours non cotés reprennent la dernière observation passée. Les déclarations de prix ne garantissent ni stock ni ouverture.

## Sources examinées mais non intégrées au modèle

L'indice AI-GPR a une méthodologie et une histoire de publication différentes : non utilisé pour éviter de mélanger un indicateur sémantique rétrospectif avec une disponibilité historique non documentée. Les déclarations directes de dirigeants, décisions OPEP, arrêts de raffinerie, fret, marges de produits raffinés et changements fiscaux ne disposent pas ici d'un corpus complet, daté et vérifié. Ils ne sont donc pas revendiqués comme variables du modèle. Le cadre français de formation des prix est documenté par https://www.ecologie.gouv.fr/politiques-publiques/prix-produits-petroliers . L'écart brut/pompe n'est pas une mesure de marge de raffinage.

Aucune économie conducteur, causalité géopolitique ou significativité statistique n'est établie. Évaluation assistée par IA et contrôles exécutables, sans revue scientifique indépendante.

## Vue utilisée dans l’article : depuis la crise en Iran
Après `python run.py`, exécuter `python crisis.py`. Ce script sans dépendance supplémentaire extrait les prévisions dont l’origine est au moins le 28 février 2026 et recalcule leurs métriques dans `crisis-results.json`. Il ne réentraîne pas les modèles. `results.json` conserve la période complète janvier–septembre. L’article et son exploration utilisent la vue post-crise : 6 247 prévisions, prix cibles du 8 mars au 27 septembre. Ce découpage a été choisi après lecture des résultats initiaux.
