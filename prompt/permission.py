"""
Module de gestion des permissions utilisateur.

Ce module fournit des fonctionnalités pour déterminer les permissions
d'un utilisateur en fonction de son rôle dans le système.
"""

from typing import List, Dict, Any


def get_user_permissions(user_id: str, system_context: Dict[str, List[str]]) -> List[str]:
    """
    Détermine les permissions d'un utilisateur selon son rôle dans le système.
    
    Cette fonction analyse le contexte système pour identifier le rôle de l'utilisateur
    et retourne les permissions appropriées. Le système supporte trois niveaux de permissions :
    - Administrateur : accès complet (read, write, delete, admin)
    - Éditeur : accès en lecture/écriture (read, write)
    - Utilisateur standard : accès en lecture seule (read)
    
    Args:
        user_id (str): Identifiant unique de l'utilisateur
        system_context (Dict[str, List[str]]): Dictionnaire contenant les listes d'utilisateurs
            par rôle. Doit contenir les clés 'admins' et 'editors' avec des listes
            d'identifiants utilisateur.
            
    Returns:
        List[str]: Liste des permissions accordées à l'utilisateur.
            Permissions possibles : 'read', 'write', 'delete', 'admin'
            
    Raises:
        TypeError: Si user_id n'est pas une chaîne ou si system_context n'est pas un dict
        ValueError: Si system_context ne contient pas les clés requises
        
    Examples:
        >>> context = {
        ...     'admins': ['admin1', 'admin2'],
        ...     'editors': ['editor1', 'editor2']
        ... }
        >>> get_user_permissions('admin1', context)
        ['read', 'write', 'delete', 'admin']
        >>> get_user_permissions('editor1', context)
        ['read', 'write']
        >>> get_user_permissions('user1', context)
        ['read']
        
    Note:
        Si un utilisateur n'est présent dans aucune liste de rôle,
        il reçoit automatiquement les permissions de base ('read').
    """
    # Validation des types d'entrée
    if not isinstance(user_id, str):
        raise TypeError("user_id doit être une chaîne de caractères")
    
    if not isinstance(system_context, dict):
        raise TypeError("system_context doit être un dictionnaire")
    
    # Validation de la structure du contexte système
    required_keys = ['admins', 'editors']
    for key in required_keys:
        if key not in system_context:
            raise ValueError(f"system_context doit contenir la clé '{key}'")
        if not isinstance(system_context[key], list):
            raise ValueError(f"system_context['{key}'] doit être une liste")
    
    # Détermination des permissions selon le rôle
    if user_id in system_context['admins']:
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context['editors']:
        return ['read', 'write']
    else:
        return ['read']


def has_permission(user_permissions: List[str], required_permission: str) -> bool:
    """
    Vérifie si l'utilisateur possède une permission spécifique.
    
    Args:
        user_permissions (List[str]): Liste des permissions de l'utilisateur
        required_permission (str): Permission requise à vérifier
        
    Returns:
        bool: True si l'utilisateur possède la permission, False sinon
        
    Examples:
        >>> permissions = ['read', 'write']
        >>> has_permission(permissions, 'write')
        True
        >>> has_permission(permissions, 'delete')
        False
    """
    return required_permission in user_permissions


def get_role_name(user_id: str, system_context: Dict[str, List[str]]) -> str:
    """
    Retourne le nom du rôle d'un utilisateur.
    
    Args:
        user_id (str): Identifiant de l'utilisateur
        system_context (Dict[str, List[str]]): Contexte système
        
    Returns:
        str: Nom du rôle ('admin', 'editor', ou 'user')
    """
    if user_id in system_context.get('admins', []):
        return 'admin'
    elif user_id in system_context.get('editors', []):
        return 'editor'
    else:
        return 'user'


# Tests unitaires
import pytest

def test_get_user_permissions_admin():
    """Test des permissions administrateur"""
    context = {
        'admins': ['admin1', 'admin2'],
        'editors': ['editor1', 'editor2']
    }
    permissions = get_user_permissions('admin1', context)
    assert permissions == ['read', 'write', 'delete', 'admin']
    assert len(permissions) == 4

def test_get_user_permissions_editor():
    """Test des permissions éditeur"""
    context = {
        'admins': ['admin1'],
        'editors': ['editor1', 'editor2']
    }
    permissions = get_user_permissions('editor1', context)
    assert permissions == ['read', 'write']
    assert len(permissions) == 2

def test_get_user_permissions_regular_user():
    """Test des permissions utilisateur standard"""
    context = {
        'admins': ['admin1'],
        'editors': ['editor1']
    }
    permissions = get_user_permissions('user1', context)
    assert permissions == ['read']
    assert len(permissions) == 1

def test_get_user_permissions_invalid_user_id():
    """Test avec user_id invalide"""
    context = {'admins': [], 'editors': []}
    with pytest.raises(TypeError):
        get_user_permissions(123, context)

def test_get_user_permissions_invalid_context():
    """Test avec contexte invalide"""
    with pytest.raises(TypeError):
        get_user_permissions('user1', 'invalid_context')
    
    with pytest.raises(ValueError):
        get_user_permissions('user1', {'admins': []})  # Manque 'editors'

def test_has_permission():
    """Test de vérification des permissions"""
    permissions = ['read', 'write']
    assert has_permission(permissions, 'read') == True
    assert has_permission(permissions, 'write') == True
    assert has_permission(permissions, 'delete') == False
    assert has_permission(permissions, 'admin') == False

def test_get_role_name():
    """Test de récupération du nom de rôle"""
    context = {
        'admins': ['admin1'],
        'editors': ['editor1']
    }
    assert get_role_name('admin1', context) == 'admin'
    assert get_role_name('editor1', context) == 'editor'
    assert get_role_name('user1', context) == 'user'


if __name__ == "__main__":
    # Démonstration du module
    print("=== Démonstration du système de permissions ===")
    
    # Configuration du contexte système
    system_context = {
        'admins': ['admin1', 'admin2'],
        'editors': ['editor1', 'editor2', 'editor3']
    }
    
    # Test avec différents utilisateurs
    test_users = ['admin1', 'editor1', 'user1', 'user2']
    
    print("Configuration du système:")
    print(f"  Administrateurs: {system_context['admins']}")
    print(f"  Éditeurs: {system_context['editors']}")
    print()
    
    for user in test_users:
        permissions = get_user_permissions(user, system_context)
        role = get_role_name(user, system_context)
        
        print(f"Utilisateur: {user}")
        print(f"  Rôle: {role}")
        print(f"  Permissions: {permissions}")
        
        # Tests de permissions spécifiques
        can_read = has_permission(permissions, 'read')
        can_write = has_permission(permissions, 'write')
        can_delete = has_permission(permissions, 'delete')
        can_admin = has_permission(permissions, 'admin')
        
        print(f"  Peut lire: {can_read}")
        print(f"  Peut écrire: {can_write}")
        print(f"  Peut supprimer: {can_delete}")
        print(f"  Est administrateur: {can_admin}")
        print("-" * 40)
    
    print("\nExécutez 'pytest permissions.py' pour lancer tous les tests")