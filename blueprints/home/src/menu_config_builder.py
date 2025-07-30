"""
Generador de configuración de menús dinámico
Este módulo contiene la función para construir el UNIFIED_MENU_CONFIG
manteniendo la estructura paso a paso exacta.
"""

def build_unified_menu_config():
    """
    Construye el UNIFIED_MENU_CONFIG paso a paso.
    Mantiene exactamente la misma estructura de asignación individual.
    
    Returns:
        dict: Configuración completa del menú unificado
    """
    
    UNIFIED_MENU_CONFIG = {}

    # ===== MÓDULO HOME =====
    UNIFIED_MENU_CONFIG['home'] = {}

    # Habilitar módulo home (sin secciones para que no tenga submenú)
    UNIFIED_MENU_CONFIG['home']['enabled'] = True

    # ===== MÓDULO LESXON =====
    UNIFIED_MENU_CONFIG['lesxon'] = {}

    # ----- SECCIÓN ETL.EXTRACT -----
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:'] = {}
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:']['section_order'] = 1
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:']['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:']['items'] = {}

    # Item: lesxon_view
    item_menu = {}
    item_menu['permission'] = 'lesxon_view'
    item_menu['display_name'] = 'View'
    item_menu['description'] = 'View data and reports'
    item_menu['url'] = '/lesxon/view'
    item_menu['route'] = 'lesxon.view'
    item_menu['icon'] = 'fas fa-eye'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:']['items']['lesxon_view'] = item_menu

    # Item: lesxon_download
    item_menu = {}
    item_menu['permission'] = 'lesxon_download'
    item_menu['display_name'] = 'Download'
    item_menu['description'] = 'Download files and datasets'
    item_menu['url'] = '/lesxon/download'
    item_menu['route'] = 'lesxon.download'
    item_menu['icon'] = 'fas fa-download'
    item_menu['item_order'] = 2
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:']['items']['lesxon_download'] = item_menu

    # Item: lesxon_zip
    item_menu = {}
    item_menu['permission'] = 'lesxon_zip'
    item_menu['display_name'] = 'Zip'
    item_menu['description'] = 'Create and manage zip archives'
    item_menu['url'] = '/lesxon/zip'
    item_menu['route'] = 'lesxon.zip'
    item_menu['icon'] = 'fas fa-file-archive'
    item_menu['item_order'] = 3
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.EXTRACT:']['items']['lesxon_zip'] = item_menu

    # ----- SECCIÓN ETL.TRANSFORM -----
    UNIFIED_MENU_CONFIG['lesxon']['ETL.TRANSFORM:'] = {}
    UNIFIED_MENU_CONFIG['lesxon']['ETL.TRANSFORM:']['section_order'] = 2
    UNIFIED_MENU_CONFIG['lesxon']['ETL.TRANSFORM:']['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.TRANSFORM:']['items'] = {}

    # Item: lesxon_transactions
    item_menu = {}
    item_menu['permission'] = 'lesxon_transactions'
    item_menu['display_name'] = 'Transactions'
    item_menu['description'] = 'Manage transaction data'
    item_menu['url'] = '/lesxon/transactions'
    item_menu['route'] = 'lesxon.transactions'
    item_menu['icon'] = 'fas fa-exchange-alt'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.TRANSFORM:']['items']['lesxon_transactions'] = item_menu

    # Item: lesxon_klines
    item_menu = {}
    item_menu['permission'] = 'lesxon_klines'
    item_menu['display_name'] = 'Klines'
    item_menu['description'] = 'View and analyze klines data'
    item_menu['url'] = '/lesxon/klines'
    item_menu['route'] = 'lesxon.klines'
    item_menu['icon'] = 'fas fa-chart-bar'
    item_menu['item_order'] = 2
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.TRANSFORM:']['items']['lesxon_klines'] = item_menu

    # ----- SECCIÓN ETL.LOAD -----
    UNIFIED_MENU_CONFIG['lesxon']['ETL.LOAD:'] = {}
    UNIFIED_MENU_CONFIG['lesxon']['ETL.LOAD:']['section_order'] = 3
    UNIFIED_MENU_CONFIG['lesxon']['ETL.LOAD:']['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.LOAD:']['items'] = {}

    # Item: lesxon_supabase
    item_menu = {}
    item_menu['permission'] = 'lesxon_supabase'
    item_menu['display_name'] = 'Supabase'
    item_menu['description'] = 'Access LesXon Supabase integration'
    item_menu['url'] = '/lesxon/supabase'
    item_menu['route'] = 'lesxon.supabase'
    item_menu['icon'] = 'fas fa-database'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['lesxon']['ETL.LOAD:']['items']['lesxon_supabase'] = item_menu

    # Habilitar módulo lesxon
    UNIFIED_MENU_CONFIG['lesxon']['enabled'] = True

    # ===== MÓDULO AUTOTRACKR =====
    UNIFIED_MENU_CONFIG['autotrackr'] = {}

    # ----- SECCIÓN ETL.EXTRACT -----
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.EXTRACT:'] = {}
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.EXTRACT:']['section_order'] = 1
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.EXTRACT:']['enabled'] = True
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.EXTRACT:']['items'] = {}

    # Item: autotrackr_service_orders
    item_menu = {}
    item_menu['permission'] = 'autotrackr_service_orders'
    item_menu['display_name'] = 'Service Orders'
    item_menu['description'] = 'Manage service orders'
    item_menu['url'] = '/autotrackr/service_orders'
    item_menu['route'] = 'autotrackr.service_orders'
    item_menu['icon'] = 'fas fa-clipboard-list'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.EXTRACT:']['items']['autotrackr_service_orders'] = item_menu

    # ----- SECCIÓN ETL.TRANSFORM -----
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.TRANSFORM:'] = {}
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.TRANSFORM:']['section_order'] = 2
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.TRANSFORM:']['enabled'] = True
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.TRANSFORM:']['items'] = {}

    # Item: autotrackr_erm_model
    item_menu = {}
    item_menu['permission'] = 'autotrackr_erm_model'
    item_menu['display_name'] = 'ERM Model'
    item_menu['description'] = 'Access ERM model tools'
    item_menu['url'] = '/autotrackr/erm_model'
    item_menu['route'] = 'autotrackr.erm_model'
    item_menu['icon'] = 'fas fa-project-diagram'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.TRANSFORM:']['items']['autotrackr_erm_model'] = item_menu

    # ----- SECCIÓN ETL.LOAD -----
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.LOAD:'] = {}
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.LOAD:']['section_order'] = 3
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.LOAD:']['enabled'] = True
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.LOAD:']['items'] = {}

    # Item: autotrackr_supabase
    item_menu = {}
    item_menu['permission'] = 'autotrackr_supabase'
    item_menu['display_name'] = 'Supabase'
    item_menu['description'] = 'Access Autotrackr Supabase integration'
    item_menu['url'] = '/autotrackr/supabase'
    item_menu['route'] = 'autotrackr.supabase'
    item_menu['icon'] = 'fas fa-database'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['autotrackr']['ETL.LOAD:']['items']['autotrackr_supabase'] = item_menu

    # Habilitar módulo autotrackr
    UNIFIED_MENU_CONFIG['autotrackr']['enabled'] = True

    # ===== MÓDULO PRODUCTS =====
    UNIFIED_MENU_CONFIG['products'] = {}

    # ----- SECCIÓN Categories -----
    UNIFIED_MENU_CONFIG['products']['Categories:'] = {}
    UNIFIED_MENU_CONFIG['products']['Categories:']['section_order'] = 1
    UNIFIED_MENU_CONFIG['products']['Categories:']['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Categories:']['items'] = {}

    # Item: products_electronics
    item_menu = {}
    item_menu['permission'] = 'products_electronics'
    item_menu['display_name'] = 'Electronics'
    item_menu['description'] = 'Manage electronics catalog'
    item_menu['url'] = '/products/category/electronics'
    item_menu['route'] = 'products.category.electronics'
    item_menu['icon'] = 'fas fa-laptop'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Categories:']['items']['products_electronics'] = item_menu

    # Item: products_clothing
    item_menu = {}
    item_menu['permission'] = 'products_clothing'
    item_menu['display_name'] = 'Clothing'
    item_menu['description'] = 'Manage clothing catalog'
    item_menu['url'] = '/products/category/clothing'
    item_menu['route'] = 'products.category.clothing'
    item_menu['icon'] = 'fas fa-tshirt'
    item_menu['item_order'] = 2
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Categories:']['items']['products_clothing'] = item_menu

    # Item: products_home_garden
    item_menu = {}
    item_menu['permission'] = 'products_home_garden'
    item_menu['display_name'] = 'Home & Garden'
    item_menu['description'] = 'Manage home & garden catalog'
    item_menu['url'] = '/products/category/home'
    item_menu['route'] = 'products.category.home'
    item_menu['icon'] = 'fas fa-home'
    item_menu['item_order'] = 3
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Categories:']['items']['products_home_garden'] = item_menu

    # ----- SECCIÓN Product Management -----
    UNIFIED_MENU_CONFIG['products']['Product Management:'] = {}
    UNIFIED_MENU_CONFIG['products']['Product Management:']['section_order'] = 2
    UNIFIED_MENU_CONFIG['products']['Product Management:']['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Product Management:']['items'] = {}

    # Item: products_new
    item_menu = {}
    item_menu['permission'] = 'products_new'
    item_menu['display_name'] = 'Add New Product'
    item_menu['description'] = 'Manage new product listings'
    item_menu['url'] = '/products/new'
    item_menu['route'] = 'products.new'
    item_menu['icon'] = 'fas fa-plus-circle'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Product Management:']['items']['products_new'] = item_menu

    # Item: products_manage
    item_menu = {}
    item_menu['permission'] = 'products_manage'
    item_menu['display_name'] = 'Manage Products'
    item_menu['description'] = 'Full product management access'
    item_menu['url'] = '/products/manage'
    item_menu['route'] = 'products.manage'
    item_menu['icon'] = 'fas fa-edit'
    item_menu['item_order'] = 2
    item_menu['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['Product Management:']['items']['products_manage'] = item_menu

    # ----- SECCIÓN All Products -----
    UNIFIED_MENU_CONFIG['products']['All Products'] = {}
    UNIFIED_MENU_CONFIG['products']['All Products']['section_order'] = 3
    UNIFIED_MENU_CONFIG['products']['All Products']['enabled'] = True
    UNIFIED_MENU_CONFIG['products']['All Products']['items'] = {}

    # Item: products_all
    item_menu = {}
    item_menu['permission'] = 'products_all'
    item_menu['display_name'] = 'All Products'
    item_menu['description'] = 'View all products'
    item_menu['url'] = '/products'
    item_menu['route'] = 'products.index'
    item_menu['icon'] = 'fas fa-list'
    item_menu['item_order'] = 1
    item_menu['enabled'] = True
    item_menu['badge'] = {}
    item_menu['badge']['text'] = 'New'
    item_menu['badge']['type'] = 'primary'
    item_menu['badge']['label'] = 'New item'
    UNIFIED_MENU_CONFIG['products']['All Products']['items']['products_all'] = item_menu

    # Habilitar módulo products
    UNIFIED_MENU_CONFIG['products']['enabled'] = True
    
    return UNIFIED_MENU_CONFIG


def get_menu_configuration():
    """
    Función de conveniencia para obtener la configuración del menú.
    Permite cachear o modificar la configuración en el futuro si es necesario.
    
    Returns:
        dict: Configuración del menú unificado
    """
    return build_unified_menu_config() 