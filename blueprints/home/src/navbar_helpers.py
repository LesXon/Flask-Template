from typing import Any, Dict, List, Optional

# Helper functions para generar nombres automáticamente
def permission_to_display_name(permission: str, module_prefix: str = None) -> str:
    """
    Convierte un nombre de permiso a un nombre de display.
    
    Ejemplos:
        'lesxon_view' -> 'View'
        'autotrackr_service_orders' -> 'Service Orders'
        'products_home_garden' -> 'Home & Garden'
        'lesxon_klines' -> 'Klines'
    """
    # Verificar si hay un nombre especial configurado
    if permission in SPECIAL_DISPLAY_NAMES:
        return SPECIAL_DISPLAY_NAMES[permission]
    
    # Remover el prefijo del módulo si se proporciona
    if module_prefix and permission.startswith(f"{module_prefix}_"):
        name_part = permission[len(module_prefix) + 1:]
    else:
        # Intentar detectar el prefijo automáticamente
        parts = permission.split('_', 1)
        if len(parts) > 1:
            name_part = parts[1]
        else:
            name_part = permission
    
    # Casos especiales
    special_cases = {
        'home_garden': 'Home & Garden',
        'service_orders': 'Service Orders',
        'erm_model': 'ERM Model',
        'klines': 'Klines',
        'supabase': 'Supabase',
    }
    
    if name_part in special_cases:
        return special_cases[name_part]
    
    # Conversión estándar: separar por underscore y capitalizar
    words = name_part.split('_')
    return ' '.join(word.capitalize() for word in words)

def generate_route_from_permission(permission: str, module_prefix: str) -> str:
    """
    Genera una ruta a partir de un permiso.
    
    Ejemplos:
        'lesxon_view', 'lesxon' -> 'lesxon.view'
        'autotrackr_service_orders', 'autotrackr' -> 'autotrackr.service_orders'
    """
    # Verificar si hay una ruta especial configurada
    if permission in SPECIAL_ROUTES:
        return SPECIAL_ROUTES[permission]['route']
    
    if permission.startswith(f"{module_prefix}_"):
        route_part = permission[len(module_prefix) + 1:]
        return f"{module_prefix}.{route_part}"
    return f"{module_prefix}.{permission}"

def generate_url_from_permission(permission: str, module_prefix: str) -> str:
    """
    Genera una URL a partir de un permiso.
    
    Ejemplos:
        'lesxon_view', 'lesxon' -> '/lesxon/view'
        'autotrackr_service_orders', 'autotrackr' -> '/autotrackr/service_orders'
    """
    # Verificar si hay una URL especial configurada
    if permission in SPECIAL_ROUTES:
        return SPECIAL_ROUTES[permission]['url']
    
    if permission.startswith(f"{module_prefix}_"):
        url_part = permission[len(module_prefix) + 1:]
        return f"/{module_prefix}/{url_part}"
    return f"/{module_prefix}/{permission}"

# Centralized menu permissions configuration
MENU_PERMISSIONS = {
    'lesxon': {
        'lesxon_view': 'View data and reports',
        'lesxon_download': 'Download files and datasets', 
        'lesxon_zip': 'Create and manage zip archives',
        'lesxon_transactions': 'Manage transaction data',
        'lesxon_klines': 'View and analyze klines data',
        'lesxon_supabase': 'Access LesXon Supabase integration'
    },
    'autotrackr': {
        'autotrackr_service_orders': 'Manage service orders',
        'autotrackr_erm_model': 'Access ERM model tools',
        'autotrackr_supabase': 'Access Autotrackr Supabase integration'
    },
    'products': {
        'products_electronics': 'Manage electronics catalog',
        'products_clothing': 'Manage clothing catalog',
        'products_home_garden': 'Manage home & garden catalog',
        'products_all': 'View all products',
        'products_new': 'Manage new product listings',
        'products_manage': 'Full product management access'
    }
}

# Configuración de iconos por permiso (opcional)
PERMISSION_ICONS = {
    'lesxon_view': 'fas fa-eye',
    'lesxon_download': 'fas fa-download',
    'lesxon_zip': 'fas fa-file-archive',
    'lesxon_transactions': 'fas fa-exchange-alt',
    'lesxon_klines': 'fas fa-chart-bar',
    'lesxon_supabase': 'fas fa-database',
    'autotrackr_service_orders': 'fas fa-clipboard-list',
    'autotrackr_erm_model': 'fas fa-project-diagram',
    'autotrackr_supabase': 'fas fa-database',
    'products_electronics': 'fas fa-laptop',
    'products_clothing': 'fas fa-tshirt',
    'products_home_garden': 'fas fa-home',
    'products_new': 'fas fa-plus-circle',
    'products_manage': 'fas fa-edit',
    'products_all': 'fas fa-list',
}

# Configuración especial de rutas para casos que no siguen el patrón estándar
SPECIAL_ROUTES = {
    'products_electronics': {
        'url': '/products/category/electronics',
        'route': 'products.category.electronics'
    },
    'products_clothing': {
        'url': '/products/category/clothing', 
        'route': 'products.category.clothing'
    },
    'products_home_garden': {
        'url': '/products/category/home',
        'route': 'products.category.home'
    },
    'products_all': {
        'url': '/products',
        'route': 'products.index'
    }
}

# Configuración especial de nombres para casos que requieren formato específico
SPECIAL_DISPLAY_NAMES = {
    'products_new': 'Add New Product',
    'products_manage': 'Manage Products'
}

# Module configuration with dependencies and metadata
MODULE_CONFIG = {
    'lesxon': {
        'display_name': 'LesXon',
        'depends_on': ['products'],  # LesXon requires Products permissions
        'icon': 'fas fa-chart-line',
        'route_prefix': 'lesxon.',
        'public_access': False
    },
    'autotrackr': {
        'display_name': 'Autotrackr', 
        'depends_on': ['products'],  # Autotrackr requires Products permissions
        'icon': 'fas fa-cogs',
        'route_prefix': 'autotrackr.',
        'public_access': False
    },
    'products': {
        'display_name': 'Products',
        'depends_on': [],  # Products has no dependencies
        'icon': 'fas fa-shopping-cart', 
        'route_prefix': 'products.',
        'public_access': False  # Set to True to make Products public
    },
    'home': {
        'display_name': 'Home',
        'depends_on': [],
        'icon': 'fas fa-home',
        'route_prefix': None,
        'public_access': True  # Home is always public
    }
}

# Estructura optimizada para la organización de menús
MODULE_MENU_STRUCTURE = {
    'lesxon': {
        'sections': [
            {
                'header': 'ETL.EXTRACT:',
                'permissions': ['lesxon_view', 'lesxon_download', 'lesxon_zip']
            },
            {
                'header': 'ETL.TRANSFORM:',
                'permissions': ['lesxon_transactions', 'lesxon_klines']
            },
            {
                'header': 'ETL.LOAD:',
                'permissions': ['lesxon_supabase']
            }
        ]
    },
    'autotrackr': {
        'sections': [
            {
                'header': 'ETL.EXTRACT:',
                'permissions': ['autotrackr_service_orders']
            },
            {
                'header': 'ETL.TRANSFORM:',
                'permissions': ['autotrackr_erm_model']
            },
            {
                'header': 'ETL.LOAD:',
                'permissions': ['autotrackr_supabase']
            }
        ]
    },
    'products': {
        'sections': [
            {
                'header': 'Categories:',
                'permissions': ['products_electronics', 'products_clothing', 'products_home_garden']
            },
            {
                'header': 'Product Management:',
                'permissions': ['products_new', 'products_manage']
            },
            {
                'header': None,  # Sin header para esta sección
                'permissions': ['products_all'],
                'badges': {
                    'products_all': {'text': 'New', 'type': 'primary', 'label': 'New item'}
                }
            }
        ]
    }
}

def generate_module_children_config(module_name: str) -> List[Dict[str, Any]]:
    """
    Genera automáticamente la configuración de children para un módulo
    basándose en MODULE_MENU_STRUCTURE y MENU_PERMISSIONS.
    """
    if module_name not in MODULE_MENU_STRUCTURE:
        return []
    
    children = []
    structure = MODULE_MENU_STRUCTURE[module_name]
    
    for i, section in enumerate(structure['sections']):
        # Agregar header si existe
        if section.get('header'):
            children.append({'header': True, 'text': section['header']})
        
        # Agregar elementos del menú
        for permission in section['permissions']:
            child_item = {
                'name': permission_to_display_name(permission, module_name),
                'url': generate_url_from_permission(permission, module_name),
                'route': generate_route_from_permission(permission, module_name),
                'permission': permission,
                'default_show': False,
                'icon': PERMISSION_ICONS.get(permission, 'fas fa-circle')
            }
            
            # Agregar badge si existe
            badges = section.get('badges', {})
            if permission in badges:
                child_item['badge'] = badges[permission]
            
            children.append(child_item)
        
        # Agregar divider después de cada sección (excepto la última)
        if i < len(structure['sections']) - 1:
            children.append({'divider': True})
    
    return children

# Dynamic menu children configuration - ahora generada automáticamente
def get_module_children_config():
    """
    Genera dinámicamente la configuración de children para todos los módulos.
    """
    config = {}
    for module_name in MODULE_MENU_STRUCTURE.keys():
        config[module_name] = generate_module_children_config(module_name)
    return config

# Generar MODULE_CHILDREN_CONFIG automáticamente
MODULE_CHILDREN_CONFIG = get_module_children_config()

def refresh_module_children_config():
    """
    Regenera MODULE_CHILDREN_CONFIG basándose en las configuraciones actuales.
    Útil cuando se han agregado nuevos permisos o modificado la estructura.
    """
    global MODULE_CHILDREN_CONFIG
    MODULE_CHILDREN_CONFIG = get_module_children_config()

def get_module_name_from_nav_item(item_name: str) -> Optional[str]:
    """
    Dynamically find module name based on display name.
    
    Args:
        item_name: Display name from navigation item
        
    Returns:
        str: Module name or None if not found
    """
    for module_name, config in MODULE_CONFIG.items():
        if config['display_name'] == item_name:
            return module_name
    return None

def check_module_dependencies(user: Optional[Dict[str, Any]], module_name: str) -> bool:
    """
    Check if user has permissions for all module dependencies.
    
    Args:
        user: User dictionary containing permissions
        module_name: Name of the module to check dependencies for
        
    Returns:
        bool: True if all dependencies are satisfied, False otherwise
    """
    if module_name not in MODULE_CONFIG:
        return False
        
    module_config = MODULE_CONFIG[module_name]
    dependencies = module_config.get('depends_on', [])
    
    # If no dependencies, check passes
    if not dependencies:
        return True
    
    # If no user (public access), check if all dependencies are public
    if not user:
        return all(MODULE_CONFIG.get(dep, {}).get('public_access', False) for dep in dependencies)
    
    # Check if user has permissions for all dependencies
    return all(has_module_permissions(user, dep) for dep in dependencies)

def is_module_accessible(user: Optional[Dict[str, Any]], module_name: str) -> bool:
    """
    Check if a module is accessible to the user based on permissions and dependencies.
    
    Args:
        user: User dictionary containing permissions
        module_name: Name of the module to check
        
    Returns:
        bool: True if module is accessible, False otherwise
    """
    if module_name not in MODULE_CONFIG:
        return False
        
    module_config = MODULE_CONFIG[module_name]
    
    # Check if module has public access
    if module_config.get('public_access', False):
        return True
    
    # If not public and no user, deny access
    if not user:
        return False
    
    # Check dependencies first
    if not check_module_dependencies(user, module_name):
        return False
    
    # Finally check if user has permissions for this specific module
    return has_module_permissions(user, module_name)

def get_all_permissions():
    """Get all available permissions as a flat list."""
    all_perms = []
    for module_perms in MENU_PERMISSIONS.values():
        all_perms.extend(module_perms.keys())
    return all_perms

def get_module_permissions(module_name):
    """Get permissions for a specific module."""
    return list(MENU_PERMISSIONS.get(module_name, {}).keys())

def create_default_permissions(modules=None):
    """Create a default permissions dictionary for specified modules."""
    if modules is None:
        modules = MENU_PERMISSIONS.keys()
    
    permissions = {}
    for module in modules:
        if module in MENU_PERMISSIONS:
            for perm in MENU_PERMISSIONS[module]:
                permissions[perm] = True
    return permissions

def has_module_permissions(user: Optional[Dict[str, Any]], module_name: str) -> bool:
    """
    Check if the user has at least one permission for a specific module.
    
    Args:
        user: User dictionary containing permissions
        module_name: Name of the module (e.g., 'lesxon', 'autotrackr', 'products')
        
    Returns:
        bool: True if user has any permission for the module, False otherwise
    """
    if not user or 'permissions' not in user:
        return False
    
    permissions = user.get('permissions', {})
    module_perms = get_module_permissions(module_name)
    
    # Check if user has at least one permission for this module
    return any(permissions.get(perm, False) for perm in module_perms)


"""Helper functions for generating navbar context."""

def get_navbar_context(
    current_route: Optional[str] = None, 
    user: Optional[Dict[str, Any]] = None, 
    **kwargs: Any
) -> Dict[str, Any]:
    """Generates a consistent navbar context dictionary for templates.

    This function builds the context required by the navbar.html template,
    including application details, search settings, authentication links, and
    the dynamic navigation structure.

    Args:
        current_route: The name of the current active route (e.g., 'home.home').
        user: An optional dictionary containing authenticated user information.
        **kwargs: Additional context variables to override or add to the defaults.

    Returns:
        A dictionary containing all necessary variables for rendering the navbar.
    """
    # Base application and UI configuration
    context = {
        'app_name': 'Flask Demo App',
        'current_route': current_route,
        'show_new_badge': True,
    }

    # Search component configuration
    search_config = {
        'search_enabled': False,
        'search_placeholder': 'Search the site...',
        'search_url': '/search',
        'search_param': 'q',
        'search_button_text': 'Search',
    }

    # Authentication links and text configuration
    auth_config = {
        'auth_enabled': True,
        'registration_enabled': True,
        'login_text': 'Sign In',
        'register_text': 'Create Account',
        'url_for_login': '/login',
        'url_for_register': '/register',
        'url_for_logout': '/logout',
        'url_for_profile': '/profile',
        'url_for_settings': '/settings',
        'url_for_notifications': '/notifications',
    }
    
    context.update(search_config)
    context.update(auth_config)

    # Add user-specific information if a user object is provided
    if user:
        context.update({
            'current_user': user,
            'notifications_enabled': True,
            'notification_count': user.get('notification_count', 0),
        })

    # Generate and add the main navigation structure
    context['nav_items'] = generate_nav_items(current_route, user)
    
    # Add helper functions to context
    context['has_lesxon_permissions'] = has_lesxon_permissions
    context['has_autotrackr_permissions'] = has_autotrackr_permissions
    context['has_module_permissions'] = has_module_permissions
    context['get_module_permissions'] = get_module_permissions
    context['get_user_permission_summary'] = get_user_permission_summary
    
    # Allow any provided kwargs to override the defaults
    context.update(kwargs)
    
    return context

def _build_menu_children(
    items_config: List[Dict[str, Any]], 
    current_route: Optional[str], 
    user: Optional[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Builds a list of dropdown menu items from a configuration."""
    children = []
    use_permissions = user and 'permissions' in user
    permissions = user.get('permissions', {}) if use_permissions else {}

    for item_config in items_config:
        # For headers and dividers
        if 'name' not in item_config:
            children.append(item_config)
            continue

        # For menu links
        required_perm = item_config.get('permission')
        
        # Determine if the item should be shown
        show_item = True
        if use_permissions and required_perm:
            show_item = permissions.get(required_perm, False)
        elif not use_permissions:
            # Show if it's a default item or if no permission is required
            show_item = item_config.get('default_show', True) if required_perm else True

        if show_item:
            item = {
                'name': item_config['name'],
                'url': item_config['url'],
                'active': current_route == item_config.get('route'),
            }
            if 'badge' in item_config:
                item['badge'] = item_config['badge']
            if 'icon' in item_config:
                item['icon'] = item_config['icon']
            children.append(item)
            
    return children

# Centralized navigation configuration - now dynamic based on MODULE_CONFIG
def get_nav_config():
    """
    Generate navigation configuration dynamically based on MODULE_CONFIG.
    This eliminates hardcoded navigation structure.
    """
    nav_config = []
    
    # Home is always first
    if 'home' in MODULE_CONFIG:
        home_config = MODULE_CONFIG['home']
        nav_config.append({
            'name': home_config['display_name'],
            'url': '/',
            'route': 'home.home',
            'icon': home_config['icon'],
        })
    
    # Add other modules dynamically
    for module_name, module_config in MODULE_CONFIG.items():
        if module_name == 'home':  # Skip home, already added
            continue
            
        nav_item = {
            'name': module_config['display_name'],
            'route_prefix': module_config['route_prefix'],
            'icon': module_config['icon'],
            'module_name': module_name,  # Add module_name for easy reference
            'children': MODULE_CHILDREN_CONFIG.get(module_name, [])  # Use dynamic children configuration
        }
        
        nav_config.append(nav_item)
    
    return nav_config

# Legacy NAV_CONFIG for backward compatibility (now generated dynamically)
NAV_CONFIG = get_nav_config()

def generate_nav_items(current_route: Optional[str] = None, user: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Generates the navigation structure for the main menu.

    Defines the default navigation items, including dropdowns and links,
    and sets the 'active' state based on the current route.

    Args:
        current_route: The name of the current active route to determine
                       which nav item is currently active.
        user: An optional dictionary containing authenticated user information
              to dynamically adjust the navigation items.

    Returns:
        A list of dictionaries, where each dictionary represents a
        navigation item or a dropdown menu.
    """
    nav_items = []
    
    # Get current navigation configuration (generated dynamically)
    nav_config = get_nav_config()
    
    for item_config in nav_config:
        route = item_config.get('route')
        route_prefix = item_config.get('route_prefix')
        
        # Get module name dynamically instead of hardcoding
        module_name = item_config.get('module_name') or get_module_name_from_nav_item(item_config['name'])
        
        # Use dynamic accessibility check instead of hardcoded logic
        if module_name and not is_module_accessible(user, module_name):
            continue  # Skip this menu item if not accessible
        
        is_active = (route and current_route == route) or \
                    (route_prefix and current_route and current_route.startswith(route_prefix))

        item = {
            'name': item_config['name'],
            'url': item_config.get('url', '#'),
            'active': is_active,
            'children': [],
        }

        if 'icon' in item_config:
            item['icon'] = item_config['icon']

        if 'children' in item_config:
            item['children'] = _build_menu_children(item_config['children'], current_route, user)
            
            # If this is a protected module and has no visible menu items (only headers/dividers), skip it
            if module_name and user:
                actual_menu_items = [child for child in item['children'] if 'name' in child]
                if len(actual_menu_items) == 0:
                    continue

        nav_items.append(item)
    
    # Special case for the test page to dynamically insert a nav item
    if current_route == 'home.test_responsive_navbar':
        test_page = {
            'name': 'Test Page',
            'url': '/test-responsive-navbar',
            'active': True,
            'children': [],
        }
        # Ensure 'Home' is not active when the test page is active
        if nav_items and nav_items[0].get('name') == 'Home':
            nav_items[0]['active'] = False
        nav_items.insert(1, test_page)
    
    return nav_items

def get_user_permission_summary(user: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Get a summary of user permissions organized by module.
    
    Args:
        user: User dictionary containing permissions
        
    Returns:
        dict: Summary with modules and their permission status
    """
    if not user or 'permissions' not in user:
        return {'modules': {}, 'total_permissions': 0, 'has_access': False}
    
    permissions = user.get('permissions', {})
    summary = {'modules': {}, 'total_permissions': 0, 'has_access': False}
    
    for module_name, module_perms in MENU_PERMISSIONS.items():
        module_summary = {
            'name': module_name.title(),
            'permissions': {},
            'has_access': False,
            'permission_count': 0
        }
        
        for perm_name, perm_desc in module_perms.items():
            has_perm = permissions.get(perm_name, False)
            module_summary['permissions'][perm_name] = {
                'has_permission': has_perm,
                'description': perm_desc
            }
            if has_perm:
                module_summary['permission_count'] += 1
                summary['total_permissions'] += 1
        
        module_summary['has_access'] = module_summary['permission_count'] > 0
        summary['modules'][module_name] = module_summary
    
    summary['has_access'] = summary['total_permissions'] > 0
    return summary

def has_lesxon_permissions(user: Optional[Dict[str, Any]]) -> bool:
    """
    Check if the user has at least one LesXon permission.
    Uses the centralized MENU_PERMISSIONS configuration.
    
    Args:
        user: User dictionary containing permissions
        
    Returns:
        bool: True if user has any LesXon permission, False otherwise
    """
    return has_module_permissions(user, 'lesxon')

def has_autotrackr_permissions(user: Optional[Dict[str, Any]]) -> bool:
    """
    Check if the user has at least one Autotrackr permission.
    Uses the centralized MENU_PERMISSIONS configuration.
    
    Args:
        user: User dictionary containing permissions
        
    Returns:
        bool: True if user has any Autotrackr permission, False otherwise
    """
    return has_module_permissions(user, 'autotrackr')

def add_module_config(module_name: str, display_name: str, icon: str, 
                     route_prefix: str = None, depends_on: List[str] = None, 
                     public_access: bool = False, permissions: Dict[str, str] = None,
                     menu_structure: Dict[str, Any] = None):
    """
    Dynamically add a new module configuration using the optimized system.
    
    Args:
        module_name: Internal module name (e.g., 'new_module')
        display_name: Display name in the UI (e.g., 'New Module')
        icon: Font Awesome icon class (e.g., 'fas fa-star')
        route_prefix: Route prefix for the module (e.g., 'new_module.')
        depends_on: List of module names this module depends on
        public_access: Whether this module is publicly accessible
        permissions: Dictionary of permissions for this module
        menu_structure: Optimized menu structure using sections and permissions
    
    Example:
        add_module_config(
            module_name='analytics',
            display_name='Analytics', 
            icon='fas fa-chart-pie',
            route_prefix='analytics.',
            depends_on=['products'],
            permissions={
                'analytics_dashboard': 'View analytics dashboard',
                'analytics_reports': 'Generate analytics reports'
            },
            menu_structure={
                'sections': [
                    {
                        'header': 'Reports:',
                        'permissions': ['analytics_dashboard', 'analytics_reports']
                    }
                ]
            }
        )
    """
    if depends_on is None:
        depends_on = []
    if permissions is None:
        permissions = {}
    if menu_structure is None:
        menu_structure = {'sections': []}
    
    # Add to MODULE_CONFIG
    MODULE_CONFIG[module_name] = {
        'display_name': display_name,
        'depends_on': depends_on,
        'icon': icon,
        'route_prefix': route_prefix,
        'public_access': public_access
    }
    
    # Add to MENU_PERMISSIONS if permissions provided
    if permissions:
        MENU_PERMISSIONS[module_name] = permissions
    
    # Add to MODULE_MENU_STRUCTURE if menu_structure provided
    if menu_structure:
        MODULE_MENU_STRUCTURE[module_name] = menu_structure
    
    # Refresh configurations
    refresh_module_children_config()
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def remove_module_config(module_name: str):
    """
    Dynamically remove a module configuration.
    
    Args:
        module_name: Module name to remove
    """
    if module_name in MODULE_CONFIG:
        del MODULE_CONFIG[module_name]
    
    if module_name in MENU_PERMISSIONS:
        # Remove all related icons and special configurations
        for permission in MENU_PERMISSIONS[module_name].keys():
            if permission in PERMISSION_ICONS:
                del PERMISSION_ICONS[permission]
            if permission in SPECIAL_ROUTES:
                del SPECIAL_ROUTES[permission]
            if permission in SPECIAL_DISPLAY_NAMES:
                del SPECIAL_DISPLAY_NAMES[permission]
        del MENU_PERMISSIONS[module_name]
    
    if module_name in MODULE_MENU_STRUCTURE:
        del MODULE_MENU_STRUCTURE[module_name]
    
    if module_name in MODULE_CHILDREN_CONFIG:
        del MODULE_CHILDREN_CONFIG[module_name]
    
    # Refresh configurations
    refresh_module_children_config()
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def update_module_menu_structure(module_name: str, menu_structure: Dict[str, Any]):
    """
    Update the menu structure for a module dynamically using the optimized system.
    
    Args:
        module_name: Module to update
        menu_structure: New menu structure with sections and permissions
        
    Example:
        # Update LesXon menu structure
        update_module_menu_structure('lesxon', {
            'sections': [
                {
                    'header': 'ETL.EXTRACT:',
                    'permissions': ['lesxon_view', 'lesxon_download', 'lesxon_zip']
                },
                {
                    'header': 'NEW SECTION:',
                    'permissions': ['lesxon_analytics']
                }
            ]
        })
    """
    if module_name in MODULE_CONFIG:
        MODULE_MENU_STRUCTURE[module_name] = menu_structure
        
        # Refresh configurations
        refresh_module_children_config()
        global NAV_CONFIG
        NAV_CONFIG = get_nav_config()

def update_module_children(module_name: str, children: List[Dict[str, Any]]):
    """
    Update the children configuration for a module dynamically (legacy support).
    Note: Consider using update_module_menu_structure for better maintainability.
    
    Args:
        module_name: Module to update
        children: New list of child menu items
    """
    if module_name in MODULE_CONFIG:
        MODULE_CHILDREN_CONFIG[module_name] = children
        
        # Refresh NAV_CONFIG
        global NAV_CONFIG
        NAV_CONFIG = get_nav_config()

def add_permission_to_module(module_name: str, permission: str, description: str, 
                            section_header: str = None, icon: str = None):
    """
    Add a new permission to a module using the optimized system.
    
    Args:
        module_name: Module to add permission to
        permission: Permission name (e.g., 'lesxon_analytics')
        description: Permission description
        section_header: Header for the section (if creating new section)
        icon: Icon for the permission (optional)
        
    Example:
        add_permission_to_module('lesxon', 'lesxon_analytics', 'Access analytics dashboard', 
                               section_header='ANALYTICS:', icon='fas fa-chart-pie')
    """
    # Add to MENU_PERMISSIONS
    if module_name not in MENU_PERMISSIONS:
        MENU_PERMISSIONS[module_name] = {}
    MENU_PERMISSIONS[module_name][permission] = description
    
    # Add icon if provided
    if icon:
        PERMISSION_ICONS[permission] = icon
    
    # Add to menu structure
    if module_name not in MODULE_MENU_STRUCTURE:
        MODULE_MENU_STRUCTURE[module_name] = {'sections': []}
    
    # Find existing section or create new one
    sections = MODULE_MENU_STRUCTURE[module_name]['sections']
    target_section = None
    
    if section_header:
        # Look for existing section with this header
        for section in sections:
            if section.get('header') == section_header:
                target_section = section
                break
        
        # Create new section if not found
        if not target_section:
            target_section = {'header': section_header, 'permissions': []}
            sections.append(target_section)
    else:
        # Add to last section or create default section
        if sections:
            target_section = sections[-1]
        else:
            target_section = {'permissions': []}
            sections.append(target_section)
    
    # Add permission to section
    if 'permissions' not in target_section:
        target_section['permissions'] = []
    target_section['permissions'].append(permission)
    
    # Refresh configurations
    refresh_module_children_config()
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def add_child_to_module(module_name: str, child_item: Dict[str, Any], position: int = None):
    """
    Add a single child item to a module's menu (legacy support).
    Note: Consider using add_permission_to_module for better maintainability.
    
    Args:
        module_name: Module to add child to
        child_item: Child item configuration
        position: Position to insert at (None = append at end)
    """
    if module_name not in MODULE_CHILDREN_CONFIG:
        MODULE_CHILDREN_CONFIG[module_name] = []
    
    if position is None:
        MODULE_CHILDREN_CONFIG[module_name].append(child_item)
    else:
        MODULE_CHILDREN_CONFIG[module_name].insert(position, child_item)
    
    # Refresh NAV_CONFIG
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def remove_permission_from_module(module_name: str, permission: str):
    """
    Remove a permission from a module using the optimized system.
    
    Args:
        module_name: Module to remove permission from
        permission: Permission name to remove
        
    Example:
        remove_permission_from_module('lesxon', 'lesxon_old_feature')
    """
    # Remove from MENU_PERMISSIONS
    if module_name in MENU_PERMISSIONS and permission in MENU_PERMISSIONS[module_name]:
        del MENU_PERMISSIONS[module_name][permission]
    
    # Remove from PERMISSION_ICONS
    if permission in PERMISSION_ICONS:
        del PERMISSION_ICONS[permission]
    
    # Remove from SPECIAL_ROUTES
    if permission in SPECIAL_ROUTES:
        del SPECIAL_ROUTES[permission]
    
    # Remove from SPECIAL_DISPLAY_NAMES
    if permission in SPECIAL_DISPLAY_NAMES:
        del SPECIAL_DISPLAY_NAMES[permission]
    
    # Remove from menu structure
    if module_name in MODULE_MENU_STRUCTURE:
        sections = MODULE_MENU_STRUCTURE[module_name]['sections']
        for section in sections:
            if 'permissions' in section and permission in section['permissions']:
                section['permissions'].remove(permission)
        
        # Remove empty sections
        MODULE_MENU_STRUCTURE[module_name]['sections'] = [
            section for section in sections 
            if section.get('permissions') or section.get('header')
        ]
    
    # Refresh configurations
    refresh_module_children_config()
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def remove_child_from_module(module_name: str, child_name: str = None, position: int = None):
    """
    Remove a child item from a module's menu (legacy support).
    Note: Consider using remove_permission_from_module for better maintainability.
    
    Args:
        module_name: Module to remove child from
        child_name: Name of child to remove (for named items)
        position: Position of child to remove (for any item type)
    """
    if module_name not in MODULE_CHILDREN_CONFIG:
        return
    
    children = MODULE_CHILDREN_CONFIG[module_name]
    
    if position is not None and 0 <= position < len(children):
        children.pop(position)
    elif child_name:
        MODULE_CHILDREN_CONFIG[module_name] = [
            child for child in children 
            if child.get('name') != child_name
        ]
    
    # Refresh NAV_CONFIG
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def update_module_dependencies(module_name: str, new_dependencies: List[str]):
    """
    Update dependencies for a module dynamically.
    
    Args:
        module_name: Module to update
        new_dependencies: New list of dependencies
        
    Example:
        # Make LesXon and Autotrackr depend on both Products and a new 'premium' module
        update_module_dependencies('lesxon', ['products', 'premium'])
        update_module_dependencies('autotrackr', ['products', 'premium'])
    """
    if module_name in MODULE_CONFIG:
        MODULE_CONFIG[module_name]['depends_on'] = new_dependencies
        
        # Refresh NAV_CONFIG
        global NAV_CONFIG
        NAV_CONFIG = get_nav_config()

def make_module_public(module_name: str, is_public: bool = True):
    """
    Make a module public or private dynamically.
    
    Args:
        module_name: Module to update
        is_public: Whether the module should be public
        
    Example:
        # Make Products public so everyone can see it
        make_module_public('products', True)
    """
    if module_name in MODULE_CONFIG:
        MODULE_CONFIG[module_name]['public_access'] = is_public
        
        # Refresh NAV_CONFIG
        global NAV_CONFIG
        NAV_CONFIG = get_nav_config()

def get_module_config_summary() -> Dict[str, Any]:
    """
    Get a summary of all module configurations for debugging/admin purposes.
    
    Returns:
        dict: Summary of all modules, their dependencies, and permissions
    """
    summary = {
        'modules': {},
        'total_modules': len(MODULE_CONFIG),
        'public_modules': [],
        'protected_modules': [],
        'dependency_tree': {}
    }
    
    for module_name, config in MODULE_CONFIG.items():
        module_info = {
            'display_name': config['display_name'],
            'dependencies': config['depends_on'],
            'is_public': config['public_access'],
            'permissions': list(MENU_PERMISSIONS.get(module_name, {}).keys()),
            'permission_count': len(MENU_PERMISSIONS.get(module_name, {}))
        }
        
        summary['modules'][module_name] = module_info
        
        if config['public_access']:
            summary['public_modules'].append(module_name)
        else:
            summary['protected_modules'].append(module_name)
        
        # Build dependency tree
        summary['dependency_tree'][module_name] = config['depends_on']
    
    return summary

# Example usage documentation (for reference)
"""
OPTIMIZED DYNAMIC PERMISSIONS SYSTEM USAGE EXAMPLES:

=== BASIC MODULE MANAGEMENT ===

1. Make Products public (everyone can see it):
   make_module_public('products', True)

2. Add a new module with optimized structure:
   add_module_config(
       module_name='analytics', 
       display_name='Analytics',
       icon='fas fa-chart-pie',
       route_prefix='analytics.',
       depends_on=['products'],
       permissions={
           'analytics_dashboard': 'View analytics dashboard',
           'analytics_reports': 'Generate analytics reports',
           'analytics_export': 'Export analytics data'
       },
       menu_structure={
           'sections': [
               {
                   'header': 'Reporting:',
                   'permissions': ['analytics_dashboard', 'analytics_reports']
               },
               {
                   'header': 'Data Export:',
                   'permissions': ['analytics_export']
               }
           ]
       }
   )

3. Update dependencies (make LesXon require both Products and Analytics):
   update_module_dependencies('lesxon', ['products', 'analytics'])

=== PERMISSION MANAGEMENT ===

4. Add a new permission to existing module:
   add_permission_to_module('lesxon', 'lesxon_machine_learning', 
                           'Access ML features', 
                           section_header='AI/ML:', 
                           icon='fas fa-robot')

5. Remove a permission:
   remove_permission_from_module('lesxon', 'lesxon_old_feature')

6. Update menu structure for a module:
   update_module_menu_structure('lesxon', {
       'sections': [
           {
               'header': 'ETL.EXTRACT:',
               'permissions': ['lesxon_view', 'lesxon_download', 'lesxon_zip']
           },
           {
               'header': 'AI/ML:',
               'permissions': ['lesxon_machine_learning']
           },
           {
               'header': 'ETL.LOAD:',
               'permissions': ['lesxon_supabase']
           }
       ]
   })

=== LEGACY SUPPORT ===

7. Legacy method - Add child item directly (not recommended):
   add_child_to_module('lesxon', {
       'name': 'Manual Item', 
       'url': '/lesxon/manual', 
       'route': 'lesxon.manual', 
       'permission': 'lesxon_manual', 
       'default_show': False, 
       'icon': 'fas fa-cog'
   })

8. Legacy method - Remove child by name:
   remove_child_from_module('lesxon', 'View')

=== ADVANCED FEATURES ===

9. Remove a module completely:
   remove_module_config('old_module')

10. Check module accessibility:
    if is_module_accessible(user, 'lesxon'):
        # User can access LesXon

11. Get configuration summary:
    summary = get_module_config_summary()
    print(f"Total modules: {summary['total_modules']}")
    print(f"Public modules: {summary['public_modules']}")

12. Complex example - Create a tiered system with optimized structure:
    # Create base module
    add_module_config('base', 'Base Tools', 'fas fa-tools', 'base.', 
                     public_access=True,
                     permissions={'base_tools': 'Access basic tools'},
                     menu_structure={'sections': [{'permissions': ['base_tools']}]})
    
    # Create premium module that depends on base
    add_module_config('premium', 'Premium', 'fas fa-crown', 'premium.', 
                     depends_on=['base'],
                     permissions={'premium_features': 'Access premium features'},
                     menu_structure={'sections': [{'permissions': ['premium_features']}]})
    
    # Create enterprise module that depends on premium
    add_module_config('enterprise', 'Enterprise', 'fas fa-building', 'enterprise.', 
                     depends_on=['premium'],
                     permissions={'enterprise_admin': 'Enterprise administration'},
                     menu_structure={'sections': [{'permissions': ['enterprise_admin']}]})

=== OPTIMIZATION BENEFITS ===

✅ No more duplicate menu names - extracted automatically from permissions
✅ Centralized permission management
✅ Automatic URL/route generation
✅ Easy bulk operations on menu structures
✅ Consistent naming conventions
✅ Special cases handled through configuration, not code
✅ Backward compatibility maintained
"""

def demo_optimized_system():
    """
    Demonstration of the optimized dynamic permissions system capabilities.
    Call this function to see the new system in action.
    
    This function shows various scenarios using the optimized system
    with automatic name generation and reduced duplication.
    """
    print("🚀 OPTIMIZED DYNAMIC PERMISSIONS SYSTEM DEMO")
    print("=" * 60)
    
    # Scenario 1: Add a new Analytics module using optimized structure
    print("\n📊 Scenario 1: Adding Analytics module with optimized structure...")
    add_module_config(
        module_name='analytics',
        display_name='Analytics',
        icon='fas fa-chart-pie',
        route_prefix='analytics.',
        depends_on=['products'],
        permissions={
            'analytics_dashboard': 'View analytics dashboard',
            'analytics_reports': 'Generate detailed reports',
            'analytics_export': 'Export analytics data',
            'analytics_insights': 'AI-powered insights'
        },
        menu_structure={
            'sections': [
                {
                    'header': 'Reporting:',
                    'permissions': ['analytics_dashboard', 'analytics_reports']
                },
                {
                    'header': 'Data & AI:',
                    'permissions': ['analytics_export', 'analytics_insights']
                }
            ]
        }
    )
    print("✅ Analytics module added with auto-generated menu items!")
    
    # Scenario 2: Make Products public
    print("\n🌐 Scenario 2: Making Products module public...")
    make_module_public('products', True)
    print("✅ Products is now publicly accessible!")
    
    # Scenario 3: Add Machine Learning to LesXon using optimized method
    print("\n🤖 Scenario 3: Adding ML feature to LesXon using optimized method...")
    add_permission_to_module('lesxon', 'lesxon_machine_learning', 
                           'Access ML and AI features', 
                           section_header='AI/ML:', 
                           icon='fas fa-robot')
    print("✅ Machine Learning added to LesXon with auto-generated menu item!")
    
    # Scenario 4: Create tiered dependency system
    print("\n🏢 Scenario 4: Creating Enterprise tier with optimized structure...")
    add_module_config(
        module_name='enterprise',
        display_name='Enterprise',
        icon='fas fa-building',
        route_prefix='enterprise.',
        depends_on=['products', 'analytics'],  # Requires both Products and Analytics
        permissions={
            'enterprise_admin': 'Enterprise administration',
            'enterprise_audit': 'Access comprehensive audit logs',
            'enterprise_compliance': 'Compliance and governance tools'
        },
        menu_structure={
            'sections': [
                {
                    'header': 'Administration:',
                    'permissions': ['enterprise_admin']
                },
                {
                    'header': 'Governance:',
                    'permissions': ['enterprise_audit', 'enterprise_compliance']
                }
            ]
        }
    )
    print("✅ Enterprise module created with auto-generated structure!")
    
    # Scenario 5: Demonstrate permission removal
    print("\n🗑️ Scenario 5: Removing an old permission from LesXon...")
    add_permission_to_module('lesxon', 'lesxon_deprecated_feature', 'Old feature')
    print("   Added temporary feature...")
    remove_permission_from_module('lesxon', 'lesxon_deprecated_feature')
    print("✅ Removed deprecated feature - menu automatically updated!")
    
    # Show optimization benefits
    print("\n🎯 OPTIMIZATION BENEFITS DEMONSTRATED:")
    print("   ✅ No manual menu item creation - auto-generated from permissions")
    print("   ✅ Consistent naming: 'lesxon_machine_learning' → 'Machine Learning'")
    print("   ✅ Automatic URL generation: → '/lesxon/machine_learning'")
    print("   ✅ Automatic route generation: → 'lesxon.machine_learning'")
    print("   ✅ Centralized icon management")
    print("   ✅ Section-based organization without duplication")
    
    # Show final configuration
    print("\n📋 FINAL CONFIGURATION SUMMARY:")
    summary = get_module_config_summary()
    print(f"Total modules: {summary['total_modules']}")
    print(f"Public modules: {summary['public_modules']}")
    print(f"Protected modules: {summary['protected_modules']}")
    
    print("\n🔗 DEPENDENCY TREE:")
    for module, deps in summary['dependency_tree'].items():
        if deps:
            print(f"  {module} → depends on: {', '.join(deps)}")
        else:
            print(f"  {module} → no dependencies")
    
    print("\n📊 PERMISSION SUMMARY:")
    total_permissions = sum(len(perms) for perms in MENU_PERMISSIONS.values())
    print(f"  Total permissions across all modules: {total_permissions}")
    for module, perms in MENU_PERMISSIONS.items():
        if module in ['analytics', 'enterprise']:  # Show new modules
            print(f"  {module}: {len(perms)} permissions")
    
    print("\n✨ Demo completed! All changes are immediately active.")
    print("   The navigation uses the optimized system with zero duplication.")
    
    return summary

# Legacy function for backward compatibility
def demo_dynamic_system():
    """Legacy function - redirects to the optimized version."""
    print("ℹ️  Redirecting to optimized demo...")
    return demo_optimized_system()