from typing import Any, Dict, List, Optional

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

# Dynamic menu children configuration
MODULE_CHILDREN_CONFIG = {
    'lesxon': [
        {'header': True, 'text': 'ETL.EXTRACT:'},
        {'name': 'View', 'url': '/lesxon/view', 'route': 'lesxon.view', 'permission': 'lesxon_view', 'default_show': False, 'icon': 'fas fa-eye'},
        {'name': 'Download', 'url': '/lesxon/download', 'route': 'lesxon.download', 'permission': 'lesxon_download', 'default_show': False, 'icon': 'fas fa-download'},
        {'name': 'Zip', 'url': '/lesxon/zip', 'route': 'lesxon.zip', 'permission': 'lesxon_zip', 'default_show': False, 'icon': 'fas fa-file-archive'},
        {'divider': True},
        {'header': True, 'text': 'ETL.TRANSFORM:'},
        {'name': 'Transactions', 'url': '/lesxon/transactions', 'route': 'lesxon.transactions', 'permission': 'lesxon_transactions', 'default_show': False, 'icon': 'fas fa-exchange-alt'},
        {'name': 'Klines', 'url': '/lesxon/klines', 'route': 'lesxon.klines', 'permission': 'lesxon_klines', 'default_show': False, 'icon': 'fas fa-chart-bar'},
        {'divider': True},
        {'header': True, 'text': 'ETL.LOAD:'},
        {'name': 'Supabase', 'url': '/lesxon/supabase', 'route': 'lesxon.supabase', 'permission': 'lesxon_supabase', 'default_show': False, 'icon': 'fas fa-database'},
    ],
    'autotrackr': [
        {'header': True, 'text': 'ETL.EXTRACT:'},
        {'name': 'Service orders', 'url': '/autotrackr/service_orders', 'route': 'autotrackr.service_orders', 'permission': 'autotrackr_service_orders', 'default_show': False, 'icon': 'fas fa-clipboard-list'},
        {'divider': True},
        {'header': True, 'text': 'ETL.TRANSFORM:'},
        {'name': 'ERM model', 'url': '/autotrackr/erm_model', 'route': 'autotrackr.erm_model', 'permission': 'autotrackr_erm_model', 'default_show': False, 'icon': 'fas fa-project-diagram'},
        {'divider': True},
        {'header': True, 'text': 'ETL.LOAD:'},
        {'name': 'Supabase', 'url': '/autotrackr/supabase', 'route': 'autotrackr.supabase', 'permission': 'autotrackr_supabase', 'default_show': False, 'icon': 'fas fa-database'},
    ],
    'products': [
        {'header': True, 'text': 'Categories:'},
        {'name': 'Electronics', 'url': '/products/category/electronics', 'route': 'products.category.electronics', 'permission': 'products_electronics', 'default_show': False, 'icon': 'fas fa-laptop'},
        {'name': 'Clothing', 'url': '/products/category/clothing', 'route': 'products.category.clothing', 'permission': 'products_clothing', 'default_show': False, 'icon': 'fas fa-tshirt'},
        {'name': 'Home & Garden', 'url': '/products/category/home', 'route': 'products.category.home', 'permission': 'products_home_garden', 'default_show': False, 'icon': 'fas fa-home'},
        {'divider': True},
        {'header': True, 'text': 'Product Management:'},
        {'name': 'Add New Product', 'url': '/products/new', 'route': 'products.new', 'permission': 'products_new', 'default_show': False, 'icon': 'fas fa-plus-circle'},
        {'name': 'Manage Products', 'url': '/products/manage', 'route': 'products.manage', 'permission': 'products_manage', 'default_show': False, 'icon': 'fas fa-edit'},
        {'divider': True},
        {'name': 'All Products', 'url': '/products', 'route': 'products.index', 'permission': 'products_all', 'default_show': False, 'badge': {'text': 'New', 'type': 'primary', 'label': 'New item'}, 'icon': 'fas fa-list'},
    ]
}

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
                     children: List[Dict[str, Any]] = None):
    """
    Dynamically add a new module configuration.
    
    Args:
        module_name: Internal module name (e.g., 'new_module')
        display_name: Display name in the UI (e.g., 'New Module')
        icon: Font Awesome icon class (e.g., 'fas fa-star')
        route_prefix: Route prefix for the module (e.g., 'new_module.')
        depends_on: List of module names this module depends on
        public_access: Whether this module is publicly accessible
        permissions: Dictionary of permissions for this module
        children: List of child menu items for this module
    
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
            children=[
                {'header': True, 'text': 'Reports:'},
                {'name': 'Dashboard', 'url': '/analytics/dashboard', 'route': 'analytics.dashboard', 'permission': 'analytics_dashboard', 'default_show': False, 'icon': 'fas fa-tachometer-alt'},
                {'name': 'Reports', 'url': '/analytics/reports', 'route': 'analytics.reports', 'permission': 'analytics_reports', 'default_show': False, 'icon': 'fas fa-chart-bar'}
            ]
        )
    """
    if depends_on is None:
        depends_on = []
    if permissions is None:
        permissions = {}
    if children is None:
        children = []
    
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
    
    # Add to MODULE_CHILDREN_CONFIG if children provided
    if children:
        MODULE_CHILDREN_CONFIG[module_name] = children
    
    # Refresh NAV_CONFIG
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
        del MENU_PERMISSIONS[module_name]
    
    if module_name in MODULE_CHILDREN_CONFIG:
        del MODULE_CHILDREN_CONFIG[module_name]
    
    # Refresh NAV_CONFIG
    global NAV_CONFIG
    NAV_CONFIG = get_nav_config()

def update_module_children(module_name: str, children: List[Dict[str, Any]]):
    """
    Update the children configuration for a module dynamically.
    
    Args:
        module_name: Module to update
        children: New list of child menu items
        
    Example:
        # Add a new menu item to LesXon
        lesxon_children = MODULE_CHILDREN_CONFIG['lesxon'].copy()
        lesxon_children.append({
            'name': 'Analytics', 
            'url': '/lesxon/analytics', 
            'route': 'lesxon.analytics', 
            'permission': 'lesxon_analytics', 
            'default_show': False, 
            'icon': 'fas fa-chart-pie'
        })
        update_module_children('lesxon', lesxon_children)
    """
    if module_name in MODULE_CONFIG:
        MODULE_CHILDREN_CONFIG[module_name] = children
        
        # Refresh NAV_CONFIG
        global NAV_CONFIG
        NAV_CONFIG = get_nav_config()

def add_child_to_module(module_name: str, child_item: Dict[str, Any], position: int = None):
    """
    Add a single child item to a module's menu.
    
    Args:
        module_name: Module to add child to
        child_item: Child item configuration
        position: Position to insert at (None = append at end)
        
    Example:
        # Add a new item to LesXon at the end
        add_child_to_module('lesxon', {
            'name': 'New Feature', 
            'url': '/lesxon/new', 
            'route': 'lesxon.new', 
            'permission': 'lesxon_new', 
            'default_show': False, 
            'icon': 'fas fa-star'
        })
        
        # Add a divider at position 3
        add_child_to_module('lesxon', {'divider': True}, 3)
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

def remove_child_from_module(module_name: str, child_name: str = None, position: int = None):
    """
    Remove a child item from a module's menu.
    
    Args:
        module_name: Module to remove child from
        child_name: Name of child to remove (for named items)
        position: Position of child to remove (for any item type)
        
    Example:
        # Remove by name
        remove_child_from_module('lesxon', 'View')
        
        # Remove by position
        remove_child_from_module('lesxon', position=0)
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
DYNAMIC PERMISSIONS SYSTEM USAGE EXAMPLES:

1. Make Products public (everyone can see it):
   make_module_public('products', True)

2. Add a new module with dependencies and children:
   add_module_config(
       module_name='premium', 
       display_name='Premium Features',
       icon='fas fa-crown',
       route_prefix='premium.',
       depends_on=['products'],
       permissions={
           'premium_analytics': 'Access premium analytics',
           'premium_export': 'Export premium data'
       },
       children=[
           {'header': True, 'text': 'Premium Tools:'},
           {'name': 'Analytics', 'url': '/premium/analytics', 'route': 'premium.analytics', 'permission': 'premium_analytics', 'default_show': False, 'icon': 'fas fa-chart-pie'},
           {'name': 'Export', 'url': '/premium/export', 'route': 'premium.export', 'permission': 'premium_export', 'default_show': False, 'icon': 'fas fa-download'}
       ]
   )

3. Update dependencies (make LesXon require both Products and Premium):
   update_module_dependencies('lesxon', ['products', 'premium'])

4. Add a new child item to an existing module:
   add_child_to_module('lesxon', {
       'name': 'Machine Learning', 
       'url': '/lesxon/ml', 
       'route': 'lesxon.ml', 
       'permission': 'lesxon_ml', 
       'default_show': False, 
       'icon': 'fas fa-robot'
   })

5. Remove a child item by name:
   remove_child_from_module('lesxon', 'View')

6. Update entire children configuration:
   new_children = [
       {'header': True, 'text': 'New Section:'},
       {'name': 'New Tool', 'url': '/lesxon/new-tool', 'route': 'lesxon.new_tool', 'permission': 'lesxon_new', 'default_show': False, 'icon': 'fas fa-tools'}
   ]
   update_module_children('lesxon', new_children)

7. Remove a module completely:
   remove_module_config('old_module')

8. Check module accessibility:
   if is_module_accessible(user, 'lesxon'):
       # User can access LesXon

9. Get configuration summary:
   summary = get_module_config_summary()
   print(f"Total modules: {summary['total_modules']}")
   print(f"Public modules: {summary['public_modules']}")

10. Complex example - Create a tiered system:
    # Create base module
    add_module_config('base', 'Base Tools', 'fas fa-tools', 'base.', public_access=True)
    
    # Create premium module that depends on base
    add_module_config('premium', 'Premium', 'fas fa-crown', 'premium.', depends_on=['base'])
    
    # Create enterprise module that depends on premium
    add_module_config('enterprise', 'Enterprise', 'fas fa-building', 'enterprise.', depends_on=['premium'])
    
    # Now enterprise users need base AND premium permissions to see enterprise features
"""

def demo_dynamic_system():
    """
    Demonstration of the dynamic permissions system capabilities.
    Call this function to see the system in action.
    
    This function shows various scenarios of how to use the dynamic system
    without hardcoded values.
    """
    print("🚀 DYNAMIC PERMISSIONS SYSTEM DEMO")
    print("=" * 50)
    
    # Scenario 1: Add a new Analytics module
    print("\n📊 Scenario 1: Adding Analytics module...")
    add_module_config(
        module_name='analytics',
        display_name='Analytics',
        icon='fas fa-chart-pie',
        route_prefix='analytics.',
        depends_on=['products'],
        permissions={
            'analytics_dashboard': 'View analytics dashboard',
            'analytics_reports': 'Generate reports',
            'analytics_export': 'Export analytics data'
        },
        children=[
            {'header': True, 'text': 'Analytics Tools:'},
            {'name': 'Dashboard', 'url': '/analytics/dashboard', 'route': 'analytics.dashboard', 'permission': 'analytics_dashboard', 'default_show': False, 'icon': 'fas fa-tachometer-alt'},
            {'name': 'Reports', 'url': '/analytics/reports', 'route': 'analytics.reports', 'permission': 'analytics_reports', 'default_show': False, 'icon': 'fas fa-file-chart-line'},
            {'divider': True},
            {'name': 'Export Data', 'url': '/analytics/export', 'route': 'analytics.export', 'permission': 'analytics_export', 'default_show': False, 'icon': 'fas fa-download'}
        ]
    )
    print("✅ Analytics module added successfully!")
    
    # Scenario 2: Make Products public
    print("\n🌐 Scenario 2: Making Products module public...")
    make_module_public('products', True)
    print("✅ Products is now publicly accessible!")
    
    # Scenario 3: Add Machine Learning to LesXon
    print("\n🤖 Scenario 3: Adding ML feature to LesXon...")
    add_child_to_module('lesxon', {
        'name': 'Machine Learning',
        'url': '/lesxon/ml',
        'route': 'lesxon.ml',
        'permission': 'lesxon_ml',
        'default_show': False,
        'icon': 'fas fa-robot'
    })
    # Also add the permission
    MENU_PERMISSIONS['lesxon']['lesxon_ml'] = 'Access ML features'
    print("✅ Machine Learning added to LesXon!")
    
    # Scenario 4: Create tiered dependency system
    print("\n🏢 Scenario 4: Creating Enterprise tier...")
    add_module_config(
        module_name='enterprise',
        display_name='Enterprise',
        icon='fas fa-building',
        route_prefix='enterprise.',
        depends_on=['products', 'analytics'],  # Requires both Products and Analytics
        permissions={
            'enterprise_admin': 'Enterprise administration',
            'enterprise_audit': 'Access audit logs'
        },
        children=[
            {'header': True, 'text': 'Enterprise Features:'},
            {'name': 'Administration', 'url': '/enterprise/admin', 'route': 'enterprise.admin', 'permission': 'enterprise_admin', 'default_show': False, 'icon': 'fas fa-cogs'},
            {'name': 'Audit Logs', 'url': '/enterprise/audit', 'route': 'enterprise.audit', 'permission': 'enterprise_audit', 'default_show': False, 'icon': 'fas fa-clipboard-list'}
        ]
    )
    print("✅ Enterprise module created with multi-dependencies!")
    
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
    
    print("\n✨ Demo completed! All changes are immediately active.")
    print("   The navigation will now reflect these dynamic changes.")
    
    return summary

def auto_generate_child_config(module_name: str, child_name: str, **overrides) -> Dict[str, Any]:
    """
    Auto-generate child configuration to avoid repeating module names.
    
    Args:
        module_name: Name of the parent module (e.g., 'lesxon')
        child_name: Name of the child item (e.g., 'View')
        **overrides: Any properties to override the auto-generated values
        
    Returns:
        dict: Complete child configuration
        
    Example:
        # Instead of:
        {'name': 'View', 'url': '/lesxon/view', 'route': 'lesxon.view', 'permission': 'lesxon_view', 'icon': 'fas fa-eye'}
        
        # Use:
        auto_generate_child_config('lesxon', 'View', icon='fas fa-eye')
    """
    # Convert name to URL-friendly format
    url_name = child_name.lower().replace(' ', '_').replace('&', 'and')
    
    # Auto-generate standard properties
    config = {
        'name': child_name,
        'url': f'/{module_name}/{url_name}',
        'route': f'{module_name}.{url_name}',
        'permission': f'{module_name}_{url_name}',
        'default_show': False,
    }
    
    # Apply any overrides
    config.update(overrides)
    
    return config

def create_menu_section(header_text: str, items: List[Dict[str, Any]], add_divider: bool = True) -> List[Dict[str, Any]]:
    """
    Create a menu section with header and items.
    
    Args:
        header_text: Text for the section header
        items: List of menu items for this section
        add_divider: Whether to add a divider after the section
        
    Returns:
        list: Section configuration including header, items, and optional divider
    """
    section = [{'header': True, 'text': header_text}]
    section.extend(items)
    
    if add_divider:
        section.append({'divider': True})
    
    return section

def build_module_children(module_name: str, sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Build complete children configuration for a module using sections.
    
    Args:
        module_name: Name of the module
        sections: List of section configurations
        
    Returns:
        list: Complete children configuration
        
    Example:
        build_module_children('lesxon', [
            {
                'header': 'ETL.EXTRACT:',
                'items': [
                    {'name': 'View', 'icon': 'fas fa-eye'},
                    {'name': 'Download', 'icon': 'fas fa-download'},
                ]
            },
            {
                'header': 'ETL.TRANSFORM:', 
                'items': [
                    {'name': 'Transactions', 'icon': 'fas fa-exchange-alt'},
                ]
            }
        ])
    """
    children = []
    
    for i, section in enumerate(sections):
        # Add section header
        children.append({'header': True, 'text': section['header']})
        
        # Add section items with auto-generation
        for item_config in section['items']:
            if 'name' in item_config:
                # Auto-generate child config
                child_item = auto_generate_child_config(module_name, item_config['name'])
                # Apply any custom overrides
                child_item.update({k: v for k, v in item_config.items() if k != 'name'})
                children.append(child_item)
            else:
                # Pass through non-standard items (like custom dividers)
                children.append(item_config)
        
        # Add divider between sections (except for the last one)
        if i < len(sections) - 1:
            children.append({'divider': True})
    
    return children

def auto_generate_permissions(module_name: str, children_config: List[Dict[str, Any]]) -> Dict[str, str]:
    """
    Auto-generate permissions dictionary from children configuration.
    
    Args:
        module_name: Name of the module
        children_config: Children configuration list
        
    Returns:
        dict: Permissions dictionary with auto-generated descriptions
    """
    permissions = {}
    
    for child in children_config:
        if 'permission' in child and 'name' in child:
            # Generate description based on the action name
            action_name = child['name'].lower()
            if 'view' in action_name or 'see' in action_name:
                description = f"View {child['name'].lower()} data"
            elif 'download' in action_name:
                description = f"Download {child['name'].lower()} files"
            elif 'manage' in action_name or 'edit' in action_name:
                description = f"Manage {child['name'].lower()}"
            elif 'create' in action_name or 'add' in action_name:
                description = f"Create new {child['name'].lower()}"
            elif 'delete' in action_name or 'remove' in action_name:
                description = f"Delete {child['name'].lower()}"
            else:
                description = f"Access {child['name'].lower()} functionality"
            
            permissions[child['permission']] = description
    
    return permissions