def calculate(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.
    
    Args:
        a (int): Premier entier
        b (int): Deuxième entier  
        op (str): Opération à effectuer ('+', '-', '*', '/')
        
    Returns:
        float: Résultat de l'opération (arrondi à 2 décimales pour la division)
        
    Raises:
        ValueError: Si l'opération n'est pas valide
        ZeroDivisionError: Si division par zéro
        TypeError: Si les paramètres ne sont pas du bon type
        
    Examples:
        >>> calculate(5, 3, '+')
        8
        >>> calculate(5, 3, '/')
        1.67
    """
    # Validation des types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Les paramètres a et b doivent être des entiers")
    
    if not isinstance(op, str):
        raise TypeError("Le paramètre op doit être une chaîne de caractères")
    
    # Validation de l'opération
    valid_operations = ['+', '-', '*', '/']
    if op not in valid_operations:
        raise ValueError(f"Opération invalide. Utilisez: {', '.join(valid_operations)}")
    
    # Exécution de l'opération
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        result = a / b
        return round(result, 2)


# Tests unitaires
import pytest

def test_calculate_addition():
    """Test de l'addition"""
    assert calculate(5, 3, '+') == 8
    assert calculate(-2, 7, '+') == 5
    assert calculate(0, 0, '+') == 0

def test_calculate_soustraction():
    """Test de la soustraction"""
    assert calculate(5, 3, '-') == 2
    assert calculate(3, 5, '-') == -2
    assert calculate(10, 10, '-') == 0

def test_calculate_multiplication():
    """Test de la multiplication"""
    assert calculate(5, 3, '*') == 15
    assert calculate(-2, 4, '*') == -8
    assert calculate(0, 5, '*') == 0

def test_calculate_division():
    """Test de la division"""
    assert calculate(5, 3, '/') == 1.67
    assert calculate(10, 2, '/') == 5.0
    assert calculate(7, 2, '/') == 3.5

def test_calculate_division_par_zero():
    """Test de la division par zéro"""
    with pytest.raises(ZeroDivisionError):
        calculate(5, 0, '/')

def test_calculate_operation_invalide():
    """Test avec opération invalide"""
    with pytest.raises(ValueError):
        calculate(5, 3, '%')
    with pytest.raises(ValueError):
        calculate(5, 3, 'add')

def test_calculate_types_invalides():
    """Test avec types invalides"""
    with pytest.raises(TypeError):
        calculate(5.5, 3, '+')
    with pytest.raises(TypeError):
        calculate(5, '3', '+')
    with pytest.raises(TypeError):
        calculate(5, 3, 123)


if __name__ == "__main__":
    # Tests de démonstration
    print("=== Tests de démonstration ===")
    try:
        print(f"calculate(5, 3, '+') = {calculate(5, 3, '+')}")
        print(f"calculate(5, 3, '-') = {calculate(5, 3, '-')}")
        print(f"calculate(5, 3, '*') = {calculate(5, 3, '*')}")
        print(f"calculate(5, 3, '/') = {calculate(5, 3, '/')}")
        
        # Test d'erreur
        print(f"calculate(5, 0, '/') = ", end="")
        calculate(5, 0, '/')
    except ZeroDivisionError as e:
        print(f"Erreur attrapée: {e}")
        
    print("\nExécutez 'pytest calculate.py' pour lancer tous les tests")