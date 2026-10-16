# Extension proposée, non exécutée

L’adaptateur `model_adapter.py` permet de brancher un modèle local déjà présent. Son rôle proposé est de sélectionner des identifiants parmi les cartes retrouvées, pas d’inventer une synthèse biomédicale. Il ne peut pas récupérer une carte manquée par la recherche initiale. L’intérêt de cette sélection reste une hypothèse ; elle peut aussi retirer une bonne référence.

## Configuration vérifiée aux sources officielles le 16 octobre 2026

Candidat : [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct), révision [7ae557604adf67be50417f59c2c2f167def9a775](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/commit/7ae557604adf67be50417f59c2c2f167def9a775). La fiche officielle indique 0,49 milliard de paramètres, BF16, licence Apache-2.0 et compatibilité Qwen2 à partir de Transformers 4.37.0. Les poids du [dépôt officiel](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/tree/7ae557604adf67be50417f59c2c2f167def9a775) occupent environ 988 MB, hors tokenizer. Aucun fichier de poids téléchargé.

Le [benchmark officiel Qwen2.5](https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html) rapporte pour 0.5B BF16 une mémoire GPU de 0,97 GB avec entrée de 1 token et génération de 2048 tokens, et 1,23 GB avec entrée de 6144 tokens. Environnement : A100 80 GB, CUDA 12.1, PyTorch 2.3.1, Transformers 4.46.0, Flash Attention 2.5.8. Ces chiffres ne décrivent pas ce Mac. Notre option CPU float32 demanderait environ 1,96 GB pour les paramètres seuls (estimation 0,49 milliard × 4 octets), plus cache, activations et bibliothèque. Ce n’est pas une mesure ni une garantie de mémoire suffisante.

Configuration proposée de l’adaptateur : CPU float32, contexte limité à 2048 tokens, 128 nouveaux tokens au maximum, `do_sample=False`, `trust_remote_code=False`, `local_files_only=True`. Versions candidates : Transformers 4.46.0 et PyTorch 2.3.1 ; elles reprennent des versions documentées, mais leur combinaison CPU/macOS n’est pas testée ici. Il ne s’agit donc pas d’un environnement verrouillé et validé pour l’extension. Le parcours principal, lui, ne dépend d’aucune de ces bibliothèques.

## Contrat testé sans modèle

Entrée : `make_request(answer)` produit deux messages ; la question et les cartes avec leurs identifiants sont des données JSON. Sortie attendue : un objet JSON strict `{"references":["D01"]}` ou `{"references":[]}`. Le validateur refuse clés supplémentaires, identifiants absents des résultats, répétitions, mauvais types et JSON invalide. Il reconstruit le texte et les références depuis les cartes locales, jamais depuis du texte généré. Les tests du validateur sont exécutés dans `check.py` avec des chaînes fabriquées ; cela n’est pas une inférence IA.

Pour une future exécution, préparer séparément un environnement compatible et un snapshot complet de la révision ci-dessus, avec licence et inventaire SHA-256. Le chemin local est explicite ; l’adaptateur ne télécharge pas et ne vérifie pas à lui seul l’identité du snapshot. Exemple d’intégration **non exécuté** :

```python
from app import run
from model_adapter import select_local
answer = run('suivi médian 7,6 ans')
selected = select_local(answer, '/chemin/vers/snapshot-verifie')
print(selected)
```

Une erreur de parsing ou de référence doit être traitée comme une abstention de l’extension, avec conservation de l’erreur dans la trace. Ne pas transformer silencieusement une sortie invalide en texte utilisateur. La vérification d’identifiants empêche les références inventées, pas une sélection hors sujet. Une future validation doit mesurer pertinence, abstentions, ressources, durée et régressions sur questions tenues à l’écart. Aucun gain du modèle n’est revendiqué.

La disponibilité a été contrôlée dans l’environnement virtuel propre : Torch et Transformers absents. Aucun parcours d’inférence utilisable n’y est donc disponible ; aucun téléchargement massif n’a été tenté. Cela ne constitue pas un inventaire global de tous les caches ou logiciels de la machine.
