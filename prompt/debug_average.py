def calculate_average(numbers_list):
    """
    Calcule la moyenne arithmétique d'une liste de nombres.
    
    Args:
        numbers_list (list): Liste de nombres (int ou float)
        
    Returns:
        float: La moyenne arithmétique des nombres
        
    Raises:
        ValueError: Si la liste est vide
        TypeError: Si un élément de la liste n'est pas un nombre
        
    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([1.5, 2.5, 3.5])
        2.5
    """
    # Vérification si la liste est vide
    if not numbers_list:
        raise ValueError("La liste ne peut pas être vide")
    
    # Vérification que tous les éléments sont des nombres
    total = 0
    for num in numbers_list:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Tous les éléments doivent être des nombres. '{num}' n'est pas un nombre.")
        total += num
    
    # Calcul de la moyenne
    average = total / len(numbers_list)
    return round(average, 2)


# Tests unitaires avec pytest
import pytest

def test_calculate_average_valid():
    """Test avec des listes valides"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5
    assert calculate_average([10]) == 10.0
    assert calculate_average([-1, 1]) == 0.0

def test_calculate_average_empty_list():
    """Test avec liste vide"""
    with pytest.raises(ValueError, match="La liste ne peut pas être vide"):
        calculate_average([])

def test_calculate_average_invalid_types():
    """Test avec types invalides"""
    with pytest.raises(TypeError, match="n'est pas un nombre"):
        calculate_average([1, 2, 'three', 4])
    
    with pytest.raises(TypeError, match="n'est pas un nombre"):