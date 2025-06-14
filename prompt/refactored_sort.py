"""
Module de tri par sélection avec fonctions utilitaires.
Ce module implémente l'algorithme de tri par sélection de manière modulaire et lisible.
"""

def bubble_sort(numbers_list):
    """
    Trie une liste d'entiers par ordre croissant en utilisant l'algorithme de tri à bulles.
    
    Args:
        numbers_list (list): Liste d'entiers à trier
        
    Returns:
        list: Liste triée par ordre croissant
        
    Raises:
        TypeError: Si un élément n'est pas un entier
        ValueError: Si la liste est None
        
    Examples:
        >>> bubble_sort([5, 3, 8, 6, 7, 2])
        [2, 3, 5, 6, 7, 8]
        >>> bubble_sort([1])
        [1]
        >>> bubble_sort([])
        []
    
    Complexité:
        Temps: O(n²) dans le pire cas
        Espace: O(1) - tri en place
    """
    # Validation des entrées
    if numbers_list is None:
        raise ValueError("La liste ne peut pas être None")
    
    # Copie de la liste pour éviter de modifier l'originale
    sorted_numbers = numbers_list.copy()
    
    # Validation des types
    for number in sorted_numbers:
        if not isinstance(number, int):
            raise TypeError(f"Tous les éléments doivent être des entiers. '{number}' n'est pas un entier.")
    
    # Algorithme de tri à bulles
    list_length = len(sorted_numbers)
    
    for current_position in range(list_length):
        for comparison_position in range(current_position + 1, list_length):
            if sorted_numbers[current_position] > sorted_numbers[comparison_position]:
                # Échange des éléments
                swap_elements(sorted_numbers, current_position, comparison_position)
    
    return sorted_numbers


def swap_elements(array, index_a, index_b):
    """
    Échange deux éléments dans un tableau aux indices spécifiés.
    
    Args:
        array (list): Le tableau contenant les éléments
        index_a (int): Index du premier élément
        index_b (int): Index du deuxième élément
        
    Raises:
        IndexError: Si les indices sont hors limites
    """
    if index_a < 0 or index_a >= len(array) or index_b < 0 or index_b >= len(array):
        raise IndexError("Les indices sont hors limites")
    
    temporary_value = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = temporary_value


def display_sorting_result(original_list, sorted_list):
    """
    Affiche le résultat du tri de manière formatée.
    
    Args:
        original_list (list): Liste originale avant tri
        sorted_list (list): Liste après tri
    """
    print(f"Liste originale: {original_list}")
    print(f"Liste triée:     {sorted_list}")
    print(f"Nombre d'éléments: {len(sorted_list)}")


def validate_sorting(sorted_list):
    """
    Vérifie si une liste est correctement triée par ordre croissant.
    
    Args:
        sorted_list (list): Liste à vérifier
        
    Returns:
        bool: True si la liste est triée, False sinon
    """
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] > sorted_list[i + 1]:
            return False
    return True


# Tests unitaires
import pytest

def test_bubble_sort_basic():
    """Test de tri basique"""
    assert bubble_sort([5, 3, 8, 6, 7, 2]) == [2, 3, 5, 6, 7, 8]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []

def test_bubble_sort_already_sorted():
    """Test avec liste déjà triée"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    """Test avec liste triée en ordre décroissant"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_with_duplicates():
    """Test avec doublons"""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_bubble_sort_invalid_types():
    """Test avec types invalides"""
    with pytest.raises(TypeError):
        bubble_sort([1, 2, 'three', 4])
    
    with pytest.raises(TypeError):
        bubble_sort([1, 2.5, 3])

def test_bubble_sort_none_input():
    """Test avec entrée None"""
    with pytest.raises(ValueError):
        bubble_sort(None)

def test_swap_elements():
    """Test de la fonction d'échange"""
    test_array = [1, 2, 3, 4, 5]
    swap_elements(test_array, 0, 4)
    assert test_array == [5, 2, 3, 4, 1]

def test_swap_elements_invalid_indices():
    """Test échange avec indices invalides"""
    test_array = [1, 2, 3]
    with pytest.raises(IndexError):
        swap_elements(test_array, 0, 10)

def test_validate_sorting():
    """Test de validation du tri"""
    assert validate_sorting([1, 2, 3, 4, 5]) == True
    assert validate_sorting([5, 4, 3, 2, 1]) == False
    assert validate_sorting([1, 1, 2, 2, 3]) == True
    assert validate_sorting([]) == True


if __name__ == "__main__":
    # Démonstration du programme
    print("=== Démonstration du Tri à Bulles ===")
    
    # Exemple principal
    original_numbers = [5, 3, 8, 6, 7, 2]
    sorted_numbers = bubble_sort(original_numbers)
    
    display_sorting_result(original_numbers, sorted_numbers)
    
    # Validation du résultat
    is_correctly_sorted = validate_sorting(sorted_numbers)
    print(f"Le tri est correct: {is_correctly_sorted}")
    
    # Autres exemples
    print("\n=== Autres exemples ===")
    test_cases = [
        [1],
        [],
        [5, 4, 3, 2, 1],
        [1, 1, 2, 2, 3, 3]
    ]
    
    for test_case in test_cases:
        try:
            result = bubble_sort(test_case)
            display_sorting_result(test_case, result)
            print("-" * 30)
        except Exception as error:
            print(f"Erreur avec {test_case}: {error}")
    
    print("\nExécutez 'pytest refactored_sort.py' pour lancer tous les tests")