from typing import Any, Dict, List, Optional
import os
from .menu_config_builder import get_menu_configuration

# ========== UNIFIED MENU CONFIGURATION (EXTERNALLY GENERATED) ==========
UNIFIED_MENU_CONFIG = get_menu_configuration()

# ========== DYNAMIC CONFIGURATION SYSTEM ==========

def get_app_config() -> Dict[str, Any]:
    """Gets application configuration from environment variables or defaults"""
    return {
        'app_name': os.getenv('APP_NAME', 'Flask Demo App'),
        'show_new_badge': os.getenv('SHOW_NEW_BADGE', 'true').lower() == 'true',
        'base_url': os.getenv('BASE_URL', ''),
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('FLASK_ENV', 'development')
    }

def get_search_config() -> Dict[str, Any]:
    """Gets search configuration from environment variables or defaults"""
    return {
        'search_enabled': os.getenv('SEARCH_ENABLED', 'false').lower() == 'true',
        'search_placeholder': os.getenv('SEARCH_PLACEHOLDER', 'Search the site...'),
        'search_url': os.getenv('SEARCH_URL', '/search'),
        'search_param': os.getenv('SEARCH_PARAM', 'q'),
        'search_button_text': os.getenv('SEARCH_BUTTON_TEXT', 'Search'),
    }

def get_auth_config() -> Dict[str, Any]:
    """Gets authentication configuration from environment variables or defaults"""
    base_url = os.getenv('BASE_URL', '')
    return {
        'auth_enabled': os.getenv('AUTH_ENABLED', 'true').lower() == 'true',
        'registration_enabled': os.getenv('REGISTRATION_ENABLED', 'true').lower() == 'true',
        'login_text': os.getenv('LOGIN_TEXT', 'Sign In'),
        'register_text': os.getenv('REGISTER_TEXT', 'Create Account'),
        'url_for_login': f"{base_url}{os.getenv('LOGIN_URL', '/login')}",
        'url_for_register': f"{base_url}{os.getenv('REGISTER_URL', '/register')}",
        'url_for_logout': f"{base_url}{os.getenv('LOGOUT_URL', '/logout')}",
        'url_for_profile': f"{base_url}{os.getenv('PROFILE_URL', '/profile')}",
        'url_for_settings': f"{base_url}{os.getenv('SETTINGS_URL', '/settings')}",
        'url_for_notifications': f"{base_url}{os.getenv('NOTIFICATIONS_URL', '/notifications')}",
    }

def get_notification_config() -> Dict[str, Any]:
    """Gets notification configuration from environment variables or defaults"""
    return {
        'notifications_enabled': os.getenv('NOTIFICATIONS_ENABLED', 'true').lower() == 'true',
        'default_notification_count': int(os.getenv('DEFAULT_NOTIFICATION_COUNT', '0')),
        'max_notification_count': int(os.getenv('MAX_NOTIFICATION_COUNT', '99')),
        'notification_badge_threshold': int(os.getenv('NOTIFICATION_BADGE_THRESHOLD', '1'))
    }

def build_dynamic_navbar_config() -> Dict[str, Any]:
    """Builds complete navbar configuration dynamically"""
    config = {}
    config.update(get_app_config())
    config.update(get_search_config())
    config.update(get_auth_config())
    return config

# Cache the configuration for performance
DEFAULT_NAVBAR_CONFIG = build_dynamic_navbar_config()

def get_module_config_from_unified() -> Dict[str, Dict[str, Any]]:
    """Extracts module configuration dynamically from UNIFIED_MENU_CONFIG"""
    module_config = {}
    
    # Get base URL for route prefixes
    base_url = os.getenv('BASE_URL', '')
    
    for module_name, module_data in UNIFIED_MENU_CONFIG.items():
        if not isinstance(module_data, dict) or not module_data.get('enabled', True):
            continue
            
        # Extract module configuration from environment or use smart defaults
        config = {
            'display_name': os.getenv(f'{module_name.upper()}_DISPLAY_NAME', module_name.title()),
            'depends_on': os.getenv(f'{module_name.upper()}_DEPENDS_ON', '').split(',') if os.getenv(f'{module_name.upper()}_DEPENDS_ON') else [],
            'icon': os.getenv(f'{module_name.upper()}_ICON', _get_default_icon(module_name)),
            'route_prefix': f"{module_name}." if module_name != 'home' else None,
            'public_access': os.getenv(f'{module_name.upper()}_PUBLIC_ACCESS', 'false' if module_name != 'home' else 'true').lower() == 'true',
            'base_url': f"{base_url}/{module_name}" if module_name != 'home' else base_url,
            'enabled': module_data.get('enabled', True)
        }
        
        module_config[module_name] = config
    
    return module_config

def _get_default_icon(module_name: str) -> str:
    """Gets default icon for a module based on its name"""
    icon_mapping = {
        'home': 'fas fa-home',
        'lesxon': 'fas fa-chart-line', 
        'autotrackr': 'fas fa-cogs',
        'products': 'fas fa-shopping-cart',
        'analytics': 'fas fa-chart-pie',
        'reports': 'fas fa-file-alt',
        'settings': 'fas fa-cog',
        'admin': 'fas fa-shield-alt',
        'users': 'fas fa-users',
        'dashboard': 'fas fa-tachometer-alt'
    }
    return icon_mapping.get(module_name, 'fas fa-circle')

# Generate dynamic module configuration
MODULE_CONFIG = get_module_config_from_unified()

# ========== OPTIMIZED HELPER FUNCTIONS ==========

def _is_enabled(item: Dict[str, Any]) -> bool:
    """Checks if an element is enabled"""
    return item.get('enabled', True)

def _is_valid_section(section_name: str, section_config: Any) -> bool:
    """Checks if a section is valid and enabled"""
    return (section_name != 'enabled' and 
            isinstance(section_config, dict) and 
            _is_enabled(section_config))

def _extract_all_menu_data():
    """
    Extracts all menu data in a single optimized pass.
    Avoids repetitive loops and duplicate calculations.
    """
    permissions = {}
    icons = {}
    structure = {}
    item_lookup = {}  # For fast lookups
    
    for module_name, module_sections in UNIFIED_MENU_CONFIG.items():
        if not isinstance(module_sections, dict) or not _is_enabled(module_sections):
            continue
            
        # Initialize structures for this module
        permissions[module_name] = {}
        structure[module_name] = {'sections': []}
        item_lookup[module_name] = {}
        
        # Process sections
        sections_data = []
        
        for section_name, section_config in module_sections.items():
            if not _is_valid_section(section_name, section_config):
                continue
                
            section_permissions = []
            items = section_config.get('items', {})
            
            # Process section items
            for permission_key, config in items.items():
                if not _is_enabled(config):
                    continue
                    
                permission = config['permission']
                
                # Extract data for multiple purposes
                permissions[module_name][permission] = config['description']
                icons[permission] = config['icon']
                item_lookup[module_name][permission] = config
                section_permissions.append(permission)
            
            if section_permissions:
                # Sort permissions by item_order
                section_permissions.sort(key=lambda p: items[p].get('item_order', 0))
                
                sections_data.append({
                    'header': section_name,
                    'permissions': section_permissions,
                    'order': section_config.get('section_order', 0)
                })
        
        # Sort sections by order
        sections_data.sort(key=lambda x: x['order'])
        structure[module_name]['sections'] = sections_data
    
    return permissions, icons, structure, item_lookup

# ========== OPTIMIZED GLOBAL VARIABLES ==========
# Calculated once instead of multiple loops
MENU_PERMISSIONS, PERMISSION_ICONS, MODULE_MENU_STRUCTURE, _ITEM_LOOKUP = _extract_all_menu_data()

# ========== DYNAMIC CONFIGURATION REFRESH FUNCTIONS ==========

def refresh_configuration():
    """Refreshes all dynamic configurations"""
    global DEFAULT_NAVBAR_CONFIG, MODULE_CONFIG, MENU_PERMISSIONS, PERMISSION_ICONS, MODULE_MENU_STRUCTURE, _ITEM_LOOKUP
    
    # Refresh navbar config
    DEFAULT_NAVBAR_CONFIG = build_dynamic_navbar_config()
    
    # Refresh module config
    MODULE_CONFIG = get_module_config_from_unified()
    
    # Refresh menu data
    MENU_PERMISSIONS, PERMISSION_ICONS, MODULE_MENU_STRUCTURE, _ITEM_LOOKUP = _extract_all_menu_data()

def update_app_config(**kwargs):
    """Updates application configuration dynamically"""
    for key, value in kwargs.items():
        os.environ[key.upper()] = str(value)
    refresh_configuration()

# ========== OPTIMIZED ACCESS FUNCTIONS ==========

def get_all_permissions() -> List[str]:
    """Gets all available permissions as a flat list"""
    return [perm for module_perms in MENU_PERMISSIONS.values() for perm in module_perms]

def get_module_permissions(module_name: str) -> List[str]:
    """Gets permissions for a specific module"""
    return list(MENU_PERMISSIONS.get(module_name, {}).keys())

def create_default_permissions(modules: Optional[List[str]] = None) -> Dict[str, bool]:
    """Creates a default permissions dictionary for specified modules"""
    if modules is None:
        modules = list(MENU_PERMISSIONS.keys())
    
    return {
        perm: True 
        for module in modules 
        if module in MENU_PERMISSIONS
        for perm in MENU_PERMISSIONS[module]
    }

def has_module_permissions(user: Optional[Dict[str, Any]], module_name: str) -> bool:
    """Checks if the user has at least one permission for a specific module"""
    if not user or 'permissions' not in user:
        return False
    
    user_permissions = user['permissions']
    module_perms = MENU_PERMISSIONS.get(module_name, {})
    
    return any(user_permissions.get(perm, False) for perm in module_perms)

def check_module_dependencies(user: Optional[Dict[str, Any]], module_name: str) -> bool:
    """Checks if the user has permissions for all module dependencies"""
    module_config = MODULE_CONFIG.get(module_name)
    if not module_config:
        return False
        
    dependencies = module_config.get('depends_on', [])
    if not dependencies:
        return True
    
    if not user:
        return all(MODULE_CONFIG.get(dep, {}).get('public_access', False) for dep in dependencies)
    
    return all(has_module_permissions(user, dep) for dep in dependencies)

def is_module_accessible(user: Optional[Dict[str, Any]], module_name: str) -> bool:
    """Checks if a module is accessible to the user"""
    module_config = MODULE_CONFIG.get(module_name)
    if not module_config:
        return False
        
    if module_config.get('public_access', False):
        return True
    
    if not user:
        return False
    
    return (check_module_dependencies(user, module_name) and 
            has_module_permissions(user, module_name))

# ========== OPTIMIZED MENU GENERATION FUNCTIONS ==========

def generate_module_children_config(module_name: str) -> List[Dict[str, Any]]:
    """Automatically generates children configuration for a module (optimized)"""
    structure = MODULE_MENU_STRUCTURE.get(module_name)
    if not structure:
        return []
    
    children = []
    item_configs = _ITEM_LOOKUP.get(module_name, {})
    
    for i, section in enumerate(structure['sections']):
        # Add header if it exists
        if section.get('header'):
            children.append({'header': True, 'text': section['header']})
        
        # Add section items
        for permission in section['permissions']:
            config = item_configs.get(permission)
            if config:
                child_item = {
                    'name': config['display_name'],
                    'url': config['url'],
                    'route': config['route'],
                    'permission': permission,
                    'default_show': False,
                    'icon': config['icon']
                }
                
                if 'badge' in config:
                    child_item['badge'] = config['badge']
                
                children.append(child_item)
        
        # Add divider (except after the last section)
        if i < len(structure['sections']) - 1:
            children.append({'divider': True})
    
    return children

def get_module_children_config() -> Dict[str, List[Dict[str, Any]]]:
    """Dynamically generates children configuration for all modules"""
    return {
        module_name: generate_module_children_config(module_name)
        for module_name in MODULE_MENU_STRUCTURE
    }

MODULE_CHILDREN_CONFIG = get_module_children_config()

# ========== OPTIMIZED NAVIGATION FUNCTIONS ==========

def get_nav_config() -> List[Dict[str, Any]]:
    """Dynamically generates navigation configuration (optimized)"""
    nav_config = []
    
    # Add HOME first (always visible, no submenu)
    if 'home' in MODULE_CONFIG and MODULE_CONFIG['home'].get('enabled', True):
        nav_config.append({
            'name': 'Home',
            'url': '/',
            'route': 'home.home',
            'icon': 'fas fa-home',
            'module_name': 'home',
            'children': []  # No submenu for HOME
        })
    
    # Add other enabled modules
    for module_name, module_config in MODULE_CONFIG.items():
        if module_name == 'home' or not module_config.get('enabled', True):
            continue
            
        nav_config.append({
            'name': module_config['display_name'],
            'route_prefix': module_config['route_prefix'],
            'icon': module_config['icon'],
            'module_name': module_name,
            'children': MODULE_CHILDREN_CONFIG.get(module_name, [])
        })
    
    return nav_config

def _build_menu_children(items_config: List[Dict[str, Any]], 
                        current_route: Optional[str], 
                        user: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Builds dropdown menu items list (optimized)"""
    if not items_config:
        return []
    
    user_permissions = user.get('permissions', {}) if user and 'permissions' in user else {}
    children = []

    for item_config in items_config:
        # Headers and dividers pass through directly
        if 'name' not in item_config:
            children.append(item_config)
            continue

        # Check permissions
        required_perm = item_config.get('permission')
        if required_perm and user_permissions:
            show_item = user_permissions.get(required_perm, False)
        else:
            show_item = item_config.get('default_show', True) if required_perm else True

        if show_item:
            item = {
                'name': item_config['name'],
                'url': item_config['url'],
                'active': current_route == item_config.get('route'),
            }
            
            # Add optional properties efficiently
            for key in ('badge', 'icon'):
                if key in item_config:
                    item[key] = item_config[key]
            
            children.append(item)
            
    return children

def generate_nav_items(current_route: Optional[str] = None, 
                      user: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Generates the navigation structure for the main menu (optimized)"""
    nav_config = get_nav_config()
    nav_items = []
    
    for item_config in nav_config:
        module_name = item_config.get('module_name')
        
        # HOME is always accessible, skip permission check for it
        if module_name and module_name != 'home' and not is_module_accessible(user, module_name):
            continue
        
        # Determine if active
        route = item_config.get('route')
        route_prefix = item_config.get('route_prefix')
        is_active = ((route and current_route == route) or 
                    (route_prefix and current_route and current_route.startswith(route_prefix)))

        # Build basic item
        item = {
            'name': item_config['name'],
            'url': item_config.get('url', '#'),
            'active': is_active,
            'children': [],
        }

        if 'icon' in item_config:
            item['icon'] = item_config['icon']

        # Process children if they exist
        if 'children' in item_config:
            item['children'] = _build_menu_children(item_config['children'], current_route, user)
            
            # If it's a protected module with no visible items, skip it
            # But never skip HOME
            if module_name and module_name != 'home' and user:
                actual_items = [child for child in item['children'] if 'name' in child]
                if not actual_items:
                    continue

        nav_items.append(item)
    
    return nav_items

# ========== OPTIMIZED MAIN FUNCTION ==========

def get_navbar_context(current_route: Optional[str] = None, 
                      user: Optional[Dict[str, Any]] = None, 
                      **kwargs: Any) -> Dict[str, Any]:
    """Generates consistent context for the navbar (optimized)"""
    # Start with base configuration
    context = DEFAULT_NAVBAR_CONFIG.copy()
    context['current_route'] = current_route

    # Add user information if it exists
    if user:
        notification_config = get_notification_config()
        
        context.update({
            'current_user': user,
            'notifications_enabled': notification_config['notifications_enabled'],
            'notification_count': min(
                user.get('notification_count', notification_config['default_notification_count']),
                notification_config['max_notification_count']
            ),
        })

    # Generate navigation
    context['nav_items'] = generate_nav_items(current_route, user)
    context['has_module_permissions'] = has_module_permissions
    
    # Apply overrides
    context.update(kwargs)
    
    return context

# ========== LEGACY FUNCTIONS (maintained for compatibility) ==========

def get_menu_permissions() -> Dict[str, Dict[str, str]]:
    """Legacy function - returns pre-calculated MENU_PERMISSIONS"""
    return MENU_PERMISSIONS

def get_permission_icons() -> Dict[str, str]:
    """Legacy function - returns pre-calculated PERMISSION_ICONS"""
    return PERMISSION_ICONS

def get_module_menu_structure() -> Dict[str, Dict[str, Any]]:
    """Legacy function - returns pre-calculated MODULE_MENU_STRUCTURE"""
    return MODULE_MENU_STRUCTURE