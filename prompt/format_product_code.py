import re
import pytest

def format_product_code(product_id):
    """
    Formate un identifiant produit selon les règles internes.
    
    Le product_id doit être une chaîne de 10 caractères alphanumériques.
    La fonction insère des tirets après le 3ème et 7ème caractère.
    
    Args:
        product_id (str): Identifiant produit de 10 caractères alphanumériques
        
    Returns:
        str: Identifiant formaté avec tirets (format: XXX-XXXX-XXXX)
        
    Raises:
        ValueError: Si l'entrée n'est pas valide (longueur ou caractères)
        
    Examples:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'
    """
    # Validation du type
    if not isinstance(product_id, str):
        raise ValueError("L'identifiant produit doit être une chaîne de caractères")
    
    # Validation de la longueur
    if len(product_id) != 10:
        raise ValueError("L'identifiant produit doit contenir exactement 10 caractères")
    
    # Validation des caractères (alphanumériques uniquement)
    if not re.match(r'^[A-Za-z0-9]+$', product_id):
        raise ValueError("L'identifiant produit doit contenir uniquement des caractères alphanumériques")
    
    # Formatage avec tirets
    formatted = f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
    return formatted


# Tests unitaires
def test_format_product_code_valid():
    """Test avec identifiants valides"""
    assert format_product_code("ABC123DEF4") == "ABC-123-DEF4"
    assert format_product_code("XYZ987GHIJ") == "XYZ-987-GHIJ"
    assert format_product_code("1234567890") == "123-4567-890"
    assert format_product_code("ABCDEFGHIJ") == "ABC-DEFG-HIJ"

def test_format_product_code_invalid_length():
    """Test avec longueurs invalides"""
    with pytest.raises(ValueError, match="exactement 10 caractères"):
        format_product_code("SHORT")
    with pytest.raises(ValueError, match="exactement 10 caractères"):
        format_product_code("TOOLONGSTRING")
    with pytest.raises(ValueError, match="exactement 10 caractères"):
        format_product_code("")

def test_format_product_code_invalid_characters():
    """Test avec caractères invalides"""
    with pytest.raises(ValueError, match="alphanumériques"):
        format_product_code("ABC-123DEF")  # Contient un tiret
    with pytest.raises(ValueError, match="alphanumériques"):
        format_product_code("ABC 123DEF")  # Contient un espace
    with pytest.raises(ValueError, match="alphanumériques"):
        format_product_code("ABC@123DEF")  # Contient un caractère spécial

def test_format_product_code_invalid_type():
    """Test avec types invalides"""
    with pytest.raises(ValueError, match="chaîne de caractères"):
        format_product_code(1234567890)
    with pytest.raises(ValueError, match="chaîne de caractères"):
        format_product_code(None)


if __name__ == "__main__":
    # Tests de démonstration
    print("=== Tests de démonstration ===")
    
    # Cas valides
    print("Cas valides:")
    test_cases = ["ABC123DEF4", "XYZ987GHIJ", "1234567890"]
    for case in test_cases:
        result = format_product_code(case)
        print(f"  {case} -> {result}")
    
    # Cas d'erreur
    print("\nCas d'erreur:")
    error_cases = ["SHORT", "ABC-123DEF", "TOOLONGSTRING"]
    for case in error_cases:
        try:
            result = format_product_code(case)
            print(f"  {case} -> {result}")
        except ValueError as e:
            print(f"  {case} -> Erreur: {e}")
    
    print("\nExécutez 'pytest product_code.py' pour lancer tous les tests")