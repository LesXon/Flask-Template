from typing import Any, Dict, List, Optional

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

# Centralized navigation configuration
NAV_CONFIG = [
    {
        'name': 'Home',
        'url': '/',
        'route': 'home.home',
        'icon': 'fas fa-home',
    },
    {
        'name': 'LesXon',
        'route_prefix': 'lesxon.',
        'icon': 'fas fa-chart-line',
        'children': [

            {'header': True, 'text': 'ETL.EXTRACT:'},
            
            {'name': 'View',
             'url': '/lesxon/view',
             'route': 'lesxon.view',
             'permission': 'lesxon_view',
             'default_show': False,
             'icon': 'fas fa-eye'
            },
            
            {'name': 'Download', 
             'url': '/lesxon/download',
             'route': 'lesxon.download',
             'permission': 'lesxon_download',
             'default_show': False,
             'icon': 'fas fa-download'
            },
            
            {'name': 'Zip', 
             'url': '/lesxon/zip',
             'route': 'lesxon.zip',
             'permission': 'lesxon_zip',
             'default_show': False,
             'icon': 'fas fa-file-archive'
             },
            
            {'divider': True},
            
            {'header': True, 'text': 'ETL.TRANSFORM:'},
            
            {'name': 'Transactions',
             'url': '/lesxon/transactions',
             'route': 'lesxon.transactions',
             'permission': 'lesxon_transactions',
             'default_show': False,
             'icon': 'fas fa-exchange-alt'
             },
            
            {'name': 'Klines', 
             'url': '/lesxon/klines',
             'route': 'lesxon.klines',
             'permission': 'lesxon_klines',
             'default_show': False,
             'icon': 'fas fa-chart-bar'
            },
            
            {'divider': True},
            
            {'header': True, 'text': 'ETL.LOAD:'},
            
            {'name': 'Supabase',
             'url': '/lesxon/supabase',
             'route': 'lesxon.supabase',
             'permission': 'lesxon_supabase',
             'default_show': False,
             'icon': 'fas fa-database'
             },
        ]
    },
    {
        'name': 'Autotrackr',
        'route_prefix': 'autotrackr.',
        'icon': 'fas fa-cogs',
        'children': [

            {'header': True, 'text': 'ETL.EXTRACT:'},

            {'name': 'Service orders',
             'url': '/autotrackr/service_orders',
             'route': 'autotrackr.service_orders',
             'permission': 'autotrackr_service_orders', 
             'default_show': False,
             'icon': 'fas fa-clipboard-list'
            },

            {'divider': True},

            {'header': True, 'text': 'ETL.TRANSFORM:'},
            
            {'name': 'ERM model',
             'url': '/autotrackr/erm_model',
             'route': 'autotrackr.erm_model',
             'permission': 'autotrackr_erm_model',
             'default_show': False,
             'icon': 'fas fa-project-diagram'
            },

            {'divider': True},
            
            {'header': True, 'text': 'ETL.LOAD:'},
            
            {'name': 'Supabase', 
             'url': '/autotrackr/supabase', 
             'route': 'autotrackr.supabase',
             'permission': 'autotrackr_supabase',
             'default_show': False,
             'icon': 'fas fa-database'
            },
        ]
    },
    {
        'name': 'Products',
        'route_prefix': 'products.',
        'icon': 'fas fa-shopping-cart',
        'children': [

            {'header': True, 'text': 'Categories:'},
            
            {'name': 'Electronics',
             'url': '/products/category/electronics',
             'route': 'products.category.electronics',
             'permission': 'products_electronics',
             'default_show': False,
             'icon': 'fas fa-laptop'
            },
            
            {'name': 'Clothing',
             'url': '/products/category/clothing',
             'route': 'products.category.clothing',
             'permission': 'products_clothing',
             'default_show': False,
             'icon': 'fas fa-tshirt'
            },
            
            {'name': 'Home & Garden',
             'url': '/products/category/home',
             'route': 'products.category.home',
             'permission': 'products_home_garden',
             'default_show': False,
             'icon': 'fas fa-home'
            },
            
            {'divider': True},
            
            {'header': True, 'text': 'Product Management:'},
            
            {'name': 'Add New Product',
             'url': '/products/new',
             'route': 'products.new',
             'permission': 'products_new',
             'default_show': False,
             'icon': 'fas fa-plus-circle'
            },
            
            {'name': 'Manage Products',
             'url': '/products/manage',
             'route': 'products.manage',
             'permission': 'products_manage',
             'default_show': False,
             'icon': 'fas fa-edit'
            },
            
            {'divider': True},
            
            {'name': 'All Products',
             'url': '/products',
             'route': 'products.index',
             'permission': 'products_all',
             'default_show': False,
             'badge': {'text': 'New', 'type': 'primary', 'label': 'New item'},
             'icon': 'fas fa-list'
            },
        ]
    }
]

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
    for item_config in NAV_CONFIG:
        route = item_config.get('route')
        route_prefix = item_config.get('route_prefix')
        
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