# Vérification de l'extension contexte

Le protocole est fixé avant les nouveaux scores. Aucun réglage de modèle après résultat. La période 2026 est distincte du test E10 2025 déjà consulté. Les stations sélectionnées ne sont pas représentatives de toute la France.

verify.py contrôle les empreintes des sources, l'unicité station/carburant/date, l'horizon de sept jours, la chronologie de l'apprentissage, le décalage macro minimal de quatorze jours et les métriques recalculées indépendamment. Il altère les déclarations et le contexte disponibles après janvier puis vérifie l'invariance des premières prévisions pour les trois IA.

Ces contrôles ne prouvent ni une disponibilité historique exacte des archives révisées, ni un lien causal entre tensions et carburants, ni une économie à la pompe. Pas d'intervalle de confiance ni de validation indépendante. Ce dossier conserve les contrôles exécutables et leurs conclusions ci-dessous.

Contrôles exécutés avec succès : métriques indépendantes et test d’invariance incluant les trois IA et les quatre carburants. Le tri des lignes de même date a été rendu stable après détection d’une dépendance de l’échantillonnage des arbres à l’ordre des lignes. Aucun réglage de modèle n’a été modifié. Le ZIP extrait passe également verify.py.

Deux exécutions complètes avec tri stable produisent un results.json identique octet par octet (cmp réussi). Aucun accès réseau ni appel payant pendant le calcul.

Vue post-crise, 22 octobre 2026 : contrôle exécuté de l’identité exacte entre les 6 247 lignes retenues et les prévisions originales filtrées par origine >= 2026-02-28. Les MAE des cinq méthodes et quatre carburants ont été recalculées indépendamment par somme des écarts absolus / effectif, concordance à 1e-12. Cibles du 8 mars au 27 septembre 2026. Aucun nouvel entraînement ni changement des prédictions.
