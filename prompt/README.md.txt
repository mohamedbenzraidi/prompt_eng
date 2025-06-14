TP : Ingénierie de prompt appliquée à la génération de code avec l'IA
Partie 1 : Solution d'IA Générative choisie
1. Solution choisie
Claude Sonnet 4 (Anthropic)
2. Définition brève de la solution
Claude Sonnet 4 est un modèle d'IA générative développé par Anthropic, spécialisé dans la compréhension et la génération de code. Il excelle dans l'analyse contextuelle et la production de code robuste avec une approche conversationnelle naturelle.
3. Avantages perçus pour le développement de code

Compréhension contextuelle approfondie : Capable d'analyser des requêtes complexes et de générer du code adapté au contexte
Génération de code robuste : Inclut automatiquement la gestion d'erreurs, les docstrings et les bonnes pratiques
Polyvalence technologique : Supporte de nombreux langages de programmation et frameworks
Analyse et débogage : Excellente capacité à identifier et corriger les erreurs dans le code existant

4. Inconvénients ou limites perçues

Dépendance à la qualité du prompt : Les résultats varient significativement selon la précision de la demande
Limitations sur les projets très spécifiques : Peut avoir des difficultés avec des domaines très techniques ou propriétaires
Pas de persistance : Ne garde pas en mémoire les interactions précédentes entre les sessions

5. Cas d'utilisation typiques

Génération de fonctions utilitaires et d'algorithmes
Débogage et refactoring de code existant
Génération de tests unitaires
Documentation automatique de code
Création de prototypes et d'applications web simples

Partie 2 : Génération de code avec IA
Exercice 2.1 : Fonction calculate
Analyse des différents prompts
Prompt Vague :
Le code généré était fonctionnel mais basique, sans gestion d'erreurs appropriée, sans docstring détaillé, et avec des noms de variables peu explicites.
Prompt Spécifique :
Le code généré était nettement amélioré avec :

Gestion complète des erreurs (division par zéro, opérateurs invalides)
Docstring détaillé avec exemples
Arrondi correct pour les divisions
Structure claire et commentaires appropriés

Prompt avec Persona :
Le code était le plus professionnel avec :

Respect strict des conventions PEP8
Structure modulaire et sécurisée
Gestion d'erreurs exhaustive
Documentation complète et professionnelle

Réponses aux questions d'analyse critique

Différences observées : Le prompt vague a généré du code basique sans robustesse. Le prompt spécifique a ajouté la gestion d'erreurs et la documentation. Le prompt avec persona a produit du code de qualité professionnelle respectant toutes les bonnes pratiques.
Principe le plus impactant : La spécificité a eu le plus grand impact, car elle a permis de définir exactement les comportements attendus, la gestion d'erreurs, et les standards de qualité.
Erreurs introduites : Le prompt vague a généré du code sans gestion de la division par zéro. Les autres versions étaient robustes.
Coût en temps : Un prompt vague nécessite plusieurs itérations de correction (2-3 fois plus de temps) comparé à un prompt spécifique qui produit directement du code de qualité.

Exercice 2.2 : Fonction format_product_code
Analyse de l'impact des exemples
Zero-Shot Prompting :
Le code généré était correct mais basique, avec une gestion d'erreurs minimale.
One-Shot Prompting :
L'ajout d'un exemple a considérablement amélioré la compréhension de l'IA, produisant un code plus précis et mieux structuré.
Few-Shot Prompting :
Les exemples multiples, incluant le cas d'erreur, ont permis une gestion d'erreurs plus robuste et complète.
Réponses aux questions d'analyse critique

Influence des exemples : Les exemples ont drastiquement amélioré la précision du code généré. L'IA a mieux compris les règles de formatage et les cas d'erreur grâce aux exemples concrets.
Utilité du Few-Shot Prompting : Particulièrement utile pour des logiques métier complexes, des formats spécifiques, ou des règles de validation non-standard.
Limites des exemples : Au-delà de 3-4 exemples, l'amélioration devient marginale. La qualité des exemples est plus importante que leur quantité.

Exercice 2.3 : Mini-application Web
L'expérimentation a montré que :

Le prompt vague a généré une calculatrice basique sans style
L'ajout de détails techniques a produit une interface moderne avec gestion d'erreurs
La spécification des styles a considérablement amélioré l'expérience utilisateur

Partie 3 : Débogage et Amélioration du Code
Exercice 3.1 : Débogage assisté
L'IA a rapidement identifié l'erreur TypeError causée par la chaîne 'three' dans la liste de nombres et a proposé une solution robuste avec validation des types.
Exercice 3.2 : Refactoring
Le code de tri initial était difficile à lire et non modulaire. Le refactoring a produit :

Fonctions modulaires avec noms explicites
Respect des conventions PEP8
Documentation complète
Structure professionnelle

Exercice 3.3 : Génération de Documentation
L'IA a généré :

Docstrings conformes aux standards Google/NumPy
Documentation README claire et structurée
Exemples d'utilisation pratiques

Conclusion
L'ingénierie de prompt est cruciale pour obtenir du code de qualité avec l'IA. Les principes clés sont :

Spécificité : Définir clairement les exigences
Exemples : Illustrer les comportements attendus
Contexte : Préciser l'environnement et les contraintes
Persona : Utiliser un rôle professionnel pour du code de qualité
Itération : Affiner progressivement les prompts