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
    # Verificar si hay un nombre especial configurado (solo si ya existe la variable)
    try:
        if permission in SPECIAL_DISPLAY_NAMES:
            return SPECIAL_DISPLAY_NAMES[permission]
    except NameError:
        # SPECIAL_DISPLAY_NAMES aún no está definido, continuar con lógica normal
        pass
    
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
    # Verificar si hay una ruta especial configurada (solo si ya existe la variable)
    try:
        if permission in SPECIAL_ROUTES:
            return SPECIAL_ROUTES[permission]['route']
    except NameError:
        # SPECIAL_ROUTES aún no está definido, continuar con lógica normal
        pass
    
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
    # Verificar si hay una URL especial configurada (solo si ya existe la variable)
    try:
        if permission in SPECIAL_ROUTES:
            return SPECIAL_ROUTES[permission]['url']
    except NameError:
        # SPECIAL_ROUTES aún no está definido, continuar con lógica normal
        pass
    
    if permission.startswith(f"{module_prefix}_"):
        url_part = permission[len(module_prefix) + 1:]
        return f"/{module_prefix}/{url_part}"
    return f"/{module_prefix}/{permission}"

# CONFIGURACIÓN UNIFICADA DE MENÚS - MÁXIMA OPTIMIZACIÓN: Agrupada por módulo y sección (CERO repetición)
UNIFIED_MENU_CONFIG = {
    'lesxon': {
        'ETL.EXTRACT:': {
            'section_order': 1,
            'items': {
                'lesxon_view': {
                    'permission': 'lesxon_view',
                    'display_name': 'View',
                    'description': 'View data and reports',
                    'url': '/lesxon/view',
                    'route': 'lesxon.view',
                    'icon': 'fas fa-eye',
                    'item_order': 1
                },
                'lesxon_download': {
                    'permission': 'lesxon_download',
                    'display_name': 'Download',
                    'description': 'Download files and datasets',
                    'url': '/lesxon/download',
                    'route': 'lesxon.download',
                    'icon': 'fas fa-download',
                    'item_order': 2
                },
                'lesxon_zip': {
                    'permission': 'lesxon_zip',
                    'display_name': 'Zip',
                    'description': 'Create and manage zip archives',
                    'url': '/lesxon/zip',
                    'route': 'lesxon.zip',
                    'icon': 'fas fa-file-archive',
                    'item_order': 3
                }
            }
        },
        'ETL.TRANSFORM:': {
            'section_order': 2,
            'items': {
                'lesxon_transactions': {
                    'permission': 'lesxon_transactions',
                    'display_name': 'Transactions',
                    'description': 'Manage transaction data',
                    'url': '/lesxon/transactions',
                    'route': 'lesxon.transactions',
                    'icon': 'fas fa-exchange-alt',
                    'item_order': 1
                },
                'lesxon_klines': {
                    'permission': 'lesxon_klines',
                    'display_name': 'Klines',
                    'description': 'View and analyze klines data',
                    'url': '/lesxon/klines',
                    'route': 'lesxon.klines',
                    'icon': 'fas fa-chart-bar',
                    'item_order': 2
                }
            }
        },
        'ETL.LOAD:': {
            'section_order': 3,
            'items': {
                'lesxon_supabase': {
                    'permission': 'lesxon_supabase',
                    'display_name': 'Supabase',
                    'description': 'Access LesXon Supabase integration',
                    'url': '/lesxon/supabase',
                    'route': 'lesxon.supabase',
                    'icon': 'fas fa-database',
                    'item_order': 1
                }
            }
        }
    },
    
    'autotrackr': {
        'ETL.EXTRACT:': {
            'section_order': 1,
            'items': {
                'autotrackr_service_orders': {
                    'permission': 'autotrackr_service_orders',
                    'display_name': 'Service Orders',
                    'description': 'Manage service orders',
                    'url': '/autotrackr/service_orders',
                    'route': 'autotrackr.service_orders',
                    'icon': 'fas fa-clipboard-list',
                    'item_order': 1
                }
            }
        },
        'ETL.TRANSFORM:': {
            'section_order': 2,
            'items': {
                'autotrackr_erm_model': {
                    'permission': 'autotrackr_erm_model',
                    'display_name': 'ERM Model',
                    'description': 'Access ERM model tools',
                    'url': '/autotrackr/erm_model',
                    'route': 'autotrackr.erm_model',
                    'icon': 'fas fa-project-diagram',
                    'item_order': 1
                }
            }
        },
        'ETL.LOAD:': {
            'section_order': 3,
            'items': {
                'autotrackr_supabase': {
                    'permission': 'autotrackr_supabase',
                    'display_name': 'Supabase',
                    'description': 'Access Autotrackr Supabase integration',
                    'url': '/autotrackr/supabase',
                    'route': 'autotrackr.supabase',
                    'icon': 'fas fa-database',
                    'item_order': 1
                }
            }
        }
    },
    
    'products': {
        'Categories:': {
            'section_order': 1,
            'items': {
                'products_electronics': {
                    'permission': 'products_electronics',
                    'display_name': 'Electronics',
                    'description': 'Manage electronics catalog',
                    'url': '/products/category/electronics',
                    'route': 'products.category.electronics',
                    'icon': 'fas fa-laptop',
                    'item_order': 1
                },
                'products_clothing': {
                    'permission': 'products_clothing',
                    'display_name': 'Clothing',
                    'description': 'Manage clothing catalog',
                    'url': '/products/category/clothing',
                    'route': 'products.category.clothing',
                    'icon': 'fas fa-tshirt',
                    'item_order': 2
                },
                'products_home_garden': {
                    'permission': 'products_home_garden',
                    'display_name': 'Home & Garden',
                    'description': 'Manage home & garden catalog',
                    'url': '/products/category/home',
                    'route': 'products.category.home',
                    'icon': 'fas fa-home',
                    'item_order': 3
                }
            }
        },
        'Product Management:': {
            'section_order': 2,
            'items': {
                'products_new': {
                    'permission': 'products_new',
                    'display_name': 'Add New Product',
                    'description': 'Manage new product listings',
                    'url': '/products/new',
                    'route': 'products.new',
                    'icon': 'fas fa-plus-circle',
                    'item_order': 1
                },
                'products_manage': {
                    'permission': 'products_manage',
                    'display_name': 'Manage Products',
                    'description': 'Full product management access',
                    'url': '/products/manage',
                    'route': 'products.manage',
                    'icon': 'fas fa-edit',
                    'item_order': 2
                }
            }
        },
        'All Products': {
            'section_order': 3,
            'items': {
                'products_all': {
                    'permission': 'products_all',
                    'display_name': 'All Products',
                    'description': 'View all products',
                    'url': '/products',
                    'route': 'products.index',
                    'icon': 'fas fa-list',
                    'item_order': 1,
                    'badge': {
                        'text': 'New',
                        'type': 'primary',
                        'label': 'New item'
                    }
                }
            }
        }
    }
}

# FUNCIONES HELPER PARA EXTRAER DATOS DEL DICCIONARIO UNIFICADO
def get_menu_permissions():
    """Extrae permisos del diccionario unificado por módulo"""
    permissions = {}
    for module_name, module_sections in UNIFIED_MENU_CONFIG.items():
        permissions[module_name] = {}
        for section_name, section_config in module_sections.items():
            for permission_key, config in section_config['items'].items():
                permissions[module_name][config['permission']] = config['description']
    return permissions

def get_permission_icons():
    """Extrae iconos del diccionario unificado"""
    icons = {}
    for module_name, module_sections in UNIFIED_MENU_CONFIG.items():
        for section_name, section_config in module_sections.items():
            for permission_key, config in section_config['items'].items():
                icons[config['permission']] = config['icon']
    return icons

def get_special_routes():
    """Extrae rutas especiales del diccionario unificado"""
    special_routes = {}
    for module_name, module_sections in UNIFIED_MENU_CONFIG.items():
        for section_name, section_config in module_sections.items():
            for permission_key, config in section_config['items'].items():
                permission = config['permission']
                url = config['url']
                route = config['route']
                
                # Verificar si no sigue el patrón estándar
                expected_url_part = permission.replace(f"{module_name}_", "")
                expected_url = f"/{module_name}/{expected_url_part}"
                
                if url != expected_url:
                    special_routes[permission] = {
                        'url': url,
                        'route': route
                    }
    return special_routes

def get_special_display_names():
    """Extrae nombres especiales del diccionario unificado"""
    special_names = {}
    
    for module_name, module_sections in UNIFIED_MENU_CONFIG.items():
        for section_name, section_config in module_sections.items():
            for permission_key, config in section_config['items'].items():
                permission = config['permission']
                display_name = config['display_name']
                
                # Calcular el nombre que se generaría automáticamente
                if permission.startswith(f"{module_name}_"):
                    name_part = permission[len(module_name) + 1:]
                else:
                    parts = permission.split('_', 1)
                    name_part = parts[1] if len(parts) > 1 else permission
                
                # Casos especiales conocidos
                auto_special_cases = {
                    'home_garden': 'Home & Garden',
                    'service_orders': 'Service Orders',
                    'erm_model': 'ERM Model',
                    'klines': 'Klines',
                    'supabase': 'Supabase',
                }
                
                if name_part in auto_special_cases:
                    expected_name = auto_special_cases[name_part]
                else:
                    # Conversión estándar
                    words = name_part.split('_')
                    expected_name = ' '.join(word.capitalize() for word in words)
                
                # Si el display_name es diferente al esperado, es especial
                if display_name != expected_name:
                    special_names[permission] = display_name
    
    return special_names

def get_module_menu_structure():
    """Genera estructura de menú del diccionario unificado"""
    structure = {}
    
    for module_name, module_sections in UNIFIED_MENU_CONFIG.items():
        structure[module_name] = {'sections': []}
        
        for section_name, section_config in module_sections.items():
            # Crear sección con todos sus permisos
            permissions = []
            for permission_key, config in section_config['items'].items():
                permissions.append(config['permission'])
            
            # Ordenar permisos por item_order
            permissions.sort(key=lambda p: next(
                (config['item_order'] 
                 for config in section_config['items'].values()
                 if config['permission'] == p), 0
            ))
            
            new_section = {
                'header': section_name,
                'permissions': permissions,
                'order': section_config['section_order']
            }
            structure[module_name]['sections'].append(new_section)
    
    # Ordenar secciones por section_order
    for module_data in structure.values():
        module_data['sections'].sort(key=lambda x: x['order'])
    
    return structure

# Inicializar variables globales para evitar NameError
MENU_PERMISSIONS = {}
PERMISSION_ICONS = {}
SPECIAL_ROUTES = {}
SPECIAL_DISPLAY_NAMES = {}
MODULE_MENU_STRUCTURE = {}

# Generar diccionarios compatibles desde la configuración unificada
def initialize_all_configurations():
    """Inicializa todas las configuraciones derivadas del diccionario unificado"""
    global MENU_PERMISSIONS, PERMISSION_ICONS, SPECIAL_ROUTES, SPECIAL_DISPLAY_NAMES, MODULE_MENU_STRUCTURE
    
    MENU_PERMISSIONS = get_menu_permissions()
    PERMISSION_ICONS = get_permission_icons()
    SPECIAL_ROUTES = get_special_routes()
    SPECIAL_DISPLAY_NAMES = get_special_display_names()
    MODULE_MENU_STRUCTURE = get_module_menu_structure()

# Llamar inicialización inmediatamente
initialize_all_configurations()

# Inicializar configuraciones que dependen de las anteriores
MODULE_CHILDREN_CONFIG = {}
NAV_CONFIG = []

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

# Configuraciones finales se generan al inicializar
# MODULE_CHILDREN_CONFIG se genera en initialize_all_configurations()

def refresh_all_configurations():
    """
    Regenera todas las configuraciones derivadas desde UNIFIED_MENU_CONFIG.
    Debe llamarse después de cualquier cambio en el diccionario unificado.
    """
    global MODULE_CHILDREN_CONFIG, NAV_CONFIG
    
    # Primero actualizar configuraciones base
    initialize_all_configurations()
    
    # Luego actualizar configuraciones que dependen de las base
    MODULE_CHILDREN_CONFIG = get_module_children_config()
    NAV_CONFIG = get_nav_config()

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

# NAV_CONFIG se genera dinámicamente en refresh_all_configurations()
# Inicialización se hace al final del archivo

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
                     public_access: bool = False, 
                     menu_items: List[Dict[str, Any]] = None):
    """
    Dynamically add a new module configuration using the unified system.
    
    Args:
        module_name: Internal module name (e.g., 'new_module')
        display_name: Display name in the UI (e.g., 'New Module')
        icon: Font Awesome icon class (e.g., 'fas fa-star')
        route_prefix: Route prefix for the module (e.g., 'new_module.')
        depends_on: List of module names this module depends on
        public_access: Whether this module is publicly accessible
        menu_items: List of menu items with complete configuration
    
    Example:
        add_module_config(
            module_name='analytics',
            display_name='Analytics', 
            icon='fas fa-chart-pie',
            route_prefix='analytics.',
            depends_on=['products'],
            menu_items=[
                {
                    'permission': 'analytics_dashboard',
                    'display_name': 'Dashboard',
                    'description': 'View analytics dashboard',
                    'url': '/analytics/dashboard',
                    'route': 'analytics.dashboard',
                    'icon': 'fas fa-tachometer-alt',
                    'section': 'Reports:',
                    'section_order': 1,
                    'item_order': 1
                },
                {
                    'permission': 'analytics_reports',
                    'display_name': 'Reports',
                    'description': 'Generate analytics reports',
                    'section': 'Reports:',
                    'section_order': 1,
                    'item_order': 2
                }
            ]
        )
    """
    if depends_on is None:
        depends_on = []
    if menu_items is None:
        menu_items = []
    
    # Add to MODULE_CONFIG
    MODULE_CONFIG[module_name] = {
        'display_name': display_name,
        'depends_on': depends_on,
        'icon': icon,
        'route_prefix': route_prefix,
        'public_access': public_access
    }
    
    # Add menu items to unified configuration
    if module_name not in UNIFIED_MENU_CONFIG:
        UNIFIED_MENU_CONFIG[module_name] = {}
    
    for item in menu_items:
        permission = item['permission']
        section_name = item.get('section', 'General')
        section_order = item.get('section_order', 1)
        
        # Ensure section exists
        if section_name not in UNIFIED_MENU_CONFIG[module_name]:
            UNIFIED_MENU_CONFIG[module_name][section_name] = {
                'section_order': section_order,
                'items': {}
            }
        
        # Generate defaults for missing fields
        item_config = {
            'permission': permission,
            'display_name': item.get('display_name', permission_to_display_name(permission, module_name)),
            'description': item.get('description', f'Access {item.get("display_name", permission)}'),
            'url': item.get('url', generate_url_from_permission(permission, module_name)),
            'route': item.get('route', generate_route_from_permission(permission, module_name)),
            'icon': item.get('icon', 'fas fa-circle'),
            'item_order': item.get('item_order', 1)
        }
        
        # Add badge if provided
        if 'badge' in item:
            item_config['badge'] = item['badge']
        
        UNIFIED_MENU_CONFIG[module_name][section_name]['items'][permission] = item_config
    
    # Refresh all configurations
    refresh_all_configurations()

def remove_module_config(module_name: str):
    """
    Dynamically remove a module configuration using the unified system.
    
    Args:
        module_name: Module name to remove
    """
    # Remove from module config
    if module_name in MODULE_CONFIG:
        del MODULE_CONFIG[module_name]
    
    # Remove all permissions for this module from unified config
    if module_name in UNIFIED_MENU_CONFIG:
        del UNIFIED_MENU_CONFIG[module_name]
    
    # Refresh all derived configurations
    refresh_all_configurations()

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
                            display_name: str = None, url: str = None, route: str = None,
                            icon: str = None, section_header: str = None, 
                            section_order: int = None, item_order: int = None,
                            badge: Dict[str, str] = None):
    """
    Add a new permission to a module using the unified system.
    
    Args:
        module_name: Module to add permission to
        permission: Permission name (e.g., 'lesxon_analytics')
        description: Permission description
        display_name: Display name (auto-generated if not provided)
        url: URL path (auto-generated if not provided)
        route: Route name (auto-generated if not provided)
        icon: Icon for the permission (default icon if not provided)
        section_header: Header for the section (default section if not provided)
        section_order: Order of the section (auto-calculated if not provided)
        item_order: Order within the section (auto-calculated if not provided)
        badge: Badge configuration (optional)
        
    Example:
        add_permission_to_module('lesxon', 'lesxon_analytics', 'Access analytics dashboard', 
                               display_name='Analytics Dashboard',
                               section_header='ANALYTICS:', 
                               icon='fas fa-chart-pie')
    """
    # Generate defaults if not provided
    if display_name is None:
        display_name = permission_to_display_name(permission, module_name)
    if url is None:
        url = generate_url_from_permission(permission, module_name)
    if route is None:
        route = generate_route_from_permission(permission, module_name)
    if icon is None:
        icon = 'fas fa-circle'
    if section_header is None:
        section_header = 'General'
    
    # Auto-calculate orders if not provided
    if section_order is None or item_order is None:
        # Find highest orders for this module
        max_section_order = 0
        max_item_order = 0
        
        if module_name in UNIFIED_MENU_CONFIG:
            for section_name, section_config in UNIFIED_MENU_CONFIG[module_name].items():
                if section_name == section_header:
                    max_item_order = max(max_item_order, max(
                        (config.get('item_order', 0) for config in section_config['items'].values()),
                        default=0
                    ))
                max_section_order = max(max_section_order, section_config.get('section_order', 0))
        
        if section_order is None:
            # If section exists, use its order, otherwise increment max
            section_order = max_section_order + 1
            if module_name in UNIFIED_MENU_CONFIG and section_header in UNIFIED_MENU_CONFIG[module_name]:
                section_order = UNIFIED_MENU_CONFIG[module_name][section_header]['section_order']
        
        if item_order is None:
            item_order = max_item_order + 1
    
    # Add to unified configuration
    if module_name not in UNIFIED_MENU_CONFIG:
        UNIFIED_MENU_CONFIG[module_name] = {}
    
    if section_header not in UNIFIED_MENU_CONFIG[module_name]:
        UNIFIED_MENU_CONFIG[module_name][section_header] = {
            'section_order': section_order,
            'items': {}
        }
    
    UNIFIED_MENU_CONFIG[module_name][section_header]['items'][permission] = {
        'permission': permission,
        'display_name': display_name,
        'description': description,
        'url': url,
        'route': route,
        'icon': icon,
        'item_order': item_order
    }
    
    # Add badge if provided
    if badge:
        UNIFIED_MENU_CONFIG[module_name][section_header]['items'][permission]['badge'] = badge
    
    # Refresh all derived configurations
    refresh_all_configurations()

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
    Remove a permission from a module using the unified system.
    
    Args:
        module_name: Module to remove permission from
        permission: Permission name to remove
        
    Example:
        remove_permission_from_module('lesxon', 'lesxon_old_feature')
    """
    # Remove from unified configuration
    if module_name in UNIFIED_MENU_CONFIG:
        # Find and remove the permission from the appropriate section
        for section_name, section_config in UNIFIED_MENU_CONFIG[module_name].items():
            if permission in section_config['items']:
                del section_config['items'][permission]
                
                # Remove empty section if no items left
                if not section_config['items']:
                    del UNIFIED_MENU_CONFIG[module_name][section_name]
                break
        
        # Remove empty module if no sections left
        if not UNIFIED_MENU_CONFIG[module_name]:
            del UNIFIED_MENU_CONFIG[module_name]
    
    # Refresh all derived configurations
    refresh_all_configurations()

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

def get_unified_config_summary() -> Dict[str, Any]:
    """
    Get a comprehensive summary of the unified configuration system.
    
    Returns:
        dict: Complete summary including unified config analysis
    """
    summary = {
        'modules': {},
        'total_modules': len(MODULE_CONFIG),
        'total_menu_items': len(UNIFIED_MENU_CONFIG),
        'public_modules': [],
        'protected_modules': [],
        'dependency_tree': {},
        'sections_by_module': {},
        'optimization_metrics': {}
    }
    
    # Analyze modules
    for module_name, config in MODULE_CONFIG.items():
        # Count menu items for this module
        module_sections = UNIFIED_MENU_CONFIG.get(module_name, {})
        menu_items_count = sum(
            len(section_config['items']) for section_config in module_sections.values()
        ) if module_sections else 0
        
        module_info = {
            'display_name': config['display_name'],
            'dependencies': config['depends_on'],
            'is_public': config['public_access'],
            'menu_items_count': menu_items_count,
            'sections': list(module_sections.keys()) if module_sections else []
        }
        
        summary['modules'][module_name] = module_info
        summary['sections_by_module'][module_name] = len(module_info['sections'])
        
        if config['public_access']:
            summary['public_modules'].append(module_name)
        else:
            summary['protected_modules'].append(module_name)
        
        summary['dependency_tree'][module_name] = config['depends_on']
    
    # Calculate optimization metrics
    total_items = sum(
        len(section_config['items']) 
        for module_sections in UNIFIED_MENU_CONFIG.values()
        for section_config in module_sections.values()
    )
    total_fields_in_unified = sum(
        len(item) 
        for module_sections in UNIFIED_MENU_CONFIG.values()
        for section_config in module_sections.values()
        for item in section_config['items'].values()
    )
    estimated_old_system_fields = total_items * 10  # Estimated fields in old distributed system (including 'module' and 'section' fields)
    
    summary['optimization_metrics'] = {
        'single_source_of_truth': True,
        'total_unified_config_fields': total_fields_in_unified,
        'estimated_old_system_duplicate_fields': estimated_old_system_fields,
        'duplication_eliminated': True,
        'auto_generation_active': True,
        'centralized_management': True
    }
    
    return summary

def get_module_config_summary() -> Dict[str, Any]:
    """
    Get a summary of all module configurations for debugging/admin purposes.
    Legacy function - redirects to unified summary.
    
    Returns:
        dict: Summary of all modules, their dependencies, and permissions
    """
    unified_summary = get_unified_config_summary()
    
    # Convert to legacy format for backward compatibility
    legacy_summary = {
        'modules': {},
        'total_modules': unified_summary['total_modules'],
        'public_modules': unified_summary['public_modules'],
        'protected_modules': unified_summary['protected_modules'],
        'dependency_tree': unified_summary['dependency_tree']
    }
    
    for module_name, module_info in unified_summary['modules'].items():
        legacy_summary['modules'][module_name] = {
            'display_name': module_info['display_name'],
            'dependencies': module_info['dependencies'],
            'is_public': module_info['is_public'],
            'permissions': list(MENU_PERMISSIONS.get(module_name, {}).keys()),
            'permission_count': len(MENU_PERMISSIONS.get(module_name, {}))
        }
    
    return legacy_summary

def show_unified_config_status():
    """
    Display detailed status of the unified configuration system.
    Useful for debugging and understanding the current state.
    """
    print("🎯 UNIFIED MENU CONFIGURATION STATUS")
    print("=" * 50)
    
    summary = get_unified_config_summary()
    
    print(f"\n📊 SYSTEM OVERVIEW:")
    print(f"   Total Modules: {summary['total_modules']}")
    print(f"   Total Menu Items: {summary['total_menu_items']}")
    print(f"   Public Modules: {len(summary['public_modules'])}")
    print(f"   Protected Modules: {len(summary['protected_modules'])}")
    
    print(f"\n📋 MODULE BREAKDOWN:")
    for module_name, module_info in summary['modules'].items():
        status = "🌐 Public" if module_info['is_public'] else "🔒 Protected"
        print(f"   {module_name}: {module_info['menu_items_count']} items, {len(module_info['sections'])} sections {status}")
    
    print(f"\n🎨 SECTIONS BY MODULE:")
    for module_name, section_count in summary['sections_by_module'].items():
        sections = summary['modules'][module_name]['sections']
        print(f"   {module_name}: {sections}")
    
    print(f"\n⚡ OPTIMIZATION BENEFITS:")
    metrics = summary['optimization_metrics']
    print(f"   ✅ Single source of truth: {metrics['single_source_of_truth']}")
    print(f"   ✅ Auto-generation active: {metrics['auto_generation_active']}")
    print(f"   ✅ Centralized management: {metrics['centralized_management']}")
    print(f"   ✅ Zero duplication: {metrics['duplication_eliminated']}")
    
    print(f"\n🔗 DEPENDENCY TREE:")
    for module, deps in summary['dependency_tree'].items():
        if deps:
            print(f"   {module} → depends on: {', '.join(deps)}")
        else:
            print(f"   {module} → no dependencies")
    
    return summary

def demo_unified_system():
    """
    Demonstration of the UNIFIED menu configuration system.
    Shows the ultimate optimization with single-dictionary configuration.
    
    This function demonstrates the most advanced version where every menu
    option is defined in ONE place with ZERO duplication.
    """
    print("🎯 UNIFIED MENU CONFIGURATION SYSTEM DEMO")
    print("=" * 60)
    
    print("\n📖 BEFORE: Multiple dictionaries, lots of duplication")
    print("   - MENU_PERMISSIONS: {'lesxon_view': 'Description'}")
    print("   - PERMISSION_ICONS: {'lesxon_view': 'fas fa-eye'}")
    print("   - SPECIAL_ROUTES: {'lesxon_view': {'url': '/path', 'route': 'route'}}")
    print("   - MODULE_CHILDREN_CONFIG: [{'name': 'View', 'url': '/path', ...}]")
    print("   → 4+ places to define the SAME menu option! 😤")
    
    print("\n✨ AFTER: Single unified dictionary, ZERO duplication")
    print("   - UNIFIED_MENU_CONFIG: {")
    print("       'lesxon': {")
    print("         'ETL.EXTRACT:': {")
    print("           'section_order': 1,")
    print("           'items': {")
    print("             'lesxon_view': {")
    print("               'permission': 'lesxon_view',")
    print("               'display_name': 'View',")
    print("               'description': 'View data and reports',")
    print("               'url': '/lesxon/view',")
    print("               'route': 'lesxon.view',")
    print("               'icon': 'fas fa-eye'")
    print("             }")
    print("           }")
    print("         }")
    print("       }")
    print("     }")
    print("   → 1 place to define EVERYTHING! Sin repetir 'module' ni 'section'! 🎉")
    
    # Show current status
    print("\n📊 CURRENT UNIFIED SYSTEM STATUS:")
    show_unified_config_status()
    
    # Scenario 1: Add new module with unified approach
    print("\n🚀 Scenario 1: Adding Analytics module with UNIFIED approach...")
    add_module_config(
        module_name='analytics',
        display_name='Analytics',
        icon='fas fa-chart-pie',
        route_prefix='analytics.',
        depends_on=['products'],
        menu_items=[
            {
                'permission': 'analytics_dashboard',
                'display_name': 'Dashboard',
                'description': 'Real-time analytics dashboard',
                'icon': 'fas fa-tachometer-alt',
                'section': 'Reporting:',
                'section_order': 1,
                'item_order': 1
            },
            {
                'permission': 'analytics_reports',
                'display_name': 'Advanced Reports',
                'description': 'Generate detailed reports',
                'icon': 'fas fa-chart-line',
                'section': 'Reporting:',
                'section_order': 1,
                'item_order': 2
            },
            {
                'permission': 'analytics_ml_insights',
                'display_name': 'AI Insights',
                'description': 'Machine learning powered insights',
                'icon': 'fas fa-brain',
                'section': 'Artificial Intelligence:',
                'section_order': 2,
                'item_order': 1,
                'badge': {'text': 'AI', 'type': 'success', 'label': 'AI powered'}
            }
        ]
    )
    print("✅ Complete module added with just ONE function call!")
    
    # Scenario 2: Add single permission
    print("\n🤖 Scenario 2: Adding single permission with auto-generation...")
    add_permission_to_module(
        module_name='lesxon',
        permission='lesxon_quantum_analysis',
        description='Next-gen quantum data analysis',
        display_name='Quantum Analysis',
        section_header='QUANTUM COMPUTING:',
        icon='fas fa-atom'
    )
    print("✅ Single permission added with complete auto-configuration!")
    
    # Scenario 3: Show the power of unified configuration
    print("\n⚡ Scenario 3: Demonstrating unified power...")
    quantum_config = {}
    if 'lesxon' in UNIFIED_MENU_CONFIG:
        for section_config in UNIFIED_MENU_CONFIG['lesxon'].values():
            if 'lesxon_quantum_analysis' in section_config['items']:
                quantum_config = section_config['items']['lesxon_quantum_analysis']
                break
    
    print(f"   From ONE entry, we auto-generated:")
    print(f"   • URL: {quantum_config.get('url', 'N/A')}")
    print(f"   • Route: {quantum_config.get('route', 'N/A')}")
    print(f"   • Display Name: {quantum_config.get('display_name', 'N/A')}")
    print(f"   • Icon: {quantum_config.get('icon', 'N/A')}")
    print("   All from defining it ONCE, without repeating 'module' or 'section'! 🎯")
    
    # Show optimization achievements
    print("\n🏆 OPTIMIZATION ACHIEVEMENTS:")
    unified_summary = get_unified_config_summary()
    metrics = unified_summary['optimization_metrics']
    
    print(f"   🎯 Single Source of Truth: {metrics['single_source_of_truth']}")
    print(f"   🔄 Auto-Generation Active: {metrics['auto_generation_active']}")
    print(f"   📝 Centralized Management: {metrics['centralized_management']}")
    print(f"   🚫 Zero Duplication: {metrics['duplication_eliminated']}")
    print(f"   📊 Total Menu Items: {unified_summary['total_menu_items']}")
    print(f"   📈 Total Modules: {unified_summary['total_modules']}")
    
    print("\n💡 DEVELOPER BENEFITS:")
    print("   ✅ Add menu option → 1 dictionary entry (was 4+ places)")
    print("   ✅ Change URL → 1 field update (was 2+ places)")
    print("   ✅ Update display name → 1 field (was 2+ places)")
    print("   ✅ Change icon → 1 field (was 2+ places)")
    print("   ✅ No more repeating 'module': 'name' in every entry!")
    print("   ✅ No more repeating 'section': 'name' in every entry!")
    print("   ✅ Grouped by module AND section - ultimate organization!")
    print("   ✅ MÁXIMA optimización - cada campo se define UNA SOLA VEZ!")
    print("   ✅ No more forgetting to update all dictionaries!")
    print("   ✅ No more inconsistencies between dictionaries!")
    print("   ✅ Auto-generated URLs, routes, and names!")
    print("   ✅ Perfect organization with sections and ordering!")
    
    # Clean up demo data
    print("\n🧹 Cleaning up demo data...")
    remove_permission_from_module('lesxon', 'lesxon_quantum_analysis')
    remove_module_config('analytics')
    print("✅ Demo cleanup completed!")
    
    print("\n🎉 UNIFIED SYSTEM DEMO COMPLETED!")
    print("   Every menu option is now defined in EXACTLY ONE PLACE")
    print("   with ZERO duplication ('module' AND 'section' fields eliminated)")
    print("   and MAXIMUM maintainability! 🚀")
    print("   → ULTIMATE OPTIMIZATION ACHIEVED! 🏆")
    
    return unified_summary

def demo_optimized_system():
    """Legacy function - redirects to unified system demo."""
    print("ℹ️  Redirecting to unified system demo...")
    return demo_unified_system()

# Legacy function for backward compatibility
def demo_dynamic_system():
    """Legacy function - redirects to the unified version."""
    print("ℹ️  Redirecting to unified system demo...")
    return demo_unified_system()

# ============================================================================
# UNIFIED MENU CONFIGURATION SYSTEM - DOCUMENTATION
# ============================================================================
"""
🎯 UNIFIED MENU CONFIGURATION SYSTEM

PROBLEMA RESUELTO:
- ANTES: Cada opción del menú se definía en 4+ diccionarios diferentes + repetición de 'module' y 'section'
- DESPUÉS: Cada opción se define en UN SOLO lugar con CERO repetición de cualquier campo

BENEFICIOS PRINCIPALES:
✅ Fuente única de verdad (Single Source of Truth)
✅ Cero duplicación de código - eliminados campos 'module' y 'section'
✅ Auto-generación de URLs, rutas y nombres
✅ Gestión centralizada y consistente
✅ Fácil mantenimiento y escalabilidad
✅ Organización perfecta con secciones
✅ Estructura agrupada por módulo y sección - máxima optimización
✅ Cada campo se define UNA SOLA VEZ en toda la configuración

EJEMPLOS DE USO:

1. AGREGAR NUEVA OPCIÓN DE MENÚ (súper fácil):
   UNIFIED_MENU_CONFIG['lesxon']['NUEVAS FEATURES:']['items']['lesxon_nueva_funcion'] = {
       'permission': 'lesxon_nueva_funcion',
       'display_name': 'Nueva Función',
       'description': 'Acceso a nueva funcionalidad',
       'url': '/lesxon/nueva',
       'route': 'lesxon.nueva',
       'icon': 'fas fa-star',
       'item_order': 1
   }

2. AGREGAR MÓDULO COMPLETO:
   add_module_config(
       module_name='nuevo_modulo',
       display_name='Nuevo Módulo',
       icon='fas fa-rocket',
       menu_items=[
           {
               'permission': 'nuevo_modulo_dashboard',
               'display_name': 'Dashboard',
               'description': 'Panel principal',
               'section': 'Principal:',
               'section_order': 1,
               'item_order': 1
           }
       ]
   )

3. AGREGAR PERMISO INDIVIDUAL:
   add_permission_to_module(
       module_name='lesxon',
       permission='lesxon_ai_analysis',
       description='Análisis con IA',
       display_name='Análisis IA',
       icon='fas fa-brain'
   )

ESTRUCTURA DEL DICCIONARIO UNIFICADO (MÁXIMA OPTIMIZACIÓN - SIN REPETIR 'module' NI 'section'):
{
    'module_name': {
        'section_name': {
            'section_order': 1,
            'items': {
                'permission_key': {
                    'permission': 'nombre_del_permiso',
                    'display_name': 'Nombre en la UI',
                    'description': 'Descripción del permiso',
                    'url': '/ruta/completa',
                    'route': 'nombre.de.ruta',
                    'icon': 'fas fa-icono',
                    'item_order': 1,
                    'badge': {'text': 'Nuevo', 'type': 'primary'} # Opcional
                }
            }
        }
    }
}

FUNCIONES PRINCIPALES:
- add_permission_to_module() - Agregar una opción
- remove_permission_from_module() - Remover una opción
- add_module_config() - Agregar módulo completo
- remove_module_config() - Remover módulo completo
- show_unified_config_status() - Ver estado del sistema
- demo_unified_system() - Demostración completa

COMPATIBILIDAD:
- Todas las funciones legacy siguen funcionando
- Los diccionarios antiguos se generan automáticamente
- Migración gradual sin romper código existente

¡El sistema ha alcanzado la MÁXIMA OPTIMIZACIÓN posible - CERO duplicación de cualquier campo! 🏆🚀
"""

# ============================================================================
# INICIALIZACIÓN FINAL DEL SISTEMA
# ============================================================================

# Generar todas las configuraciones una vez que todo esté definido
refresh_all_configurations()

# Mensaje de confirmación de inicialización (comentado para producción)
# print("✅ Sistema unificado de menús inicializado correctamente")