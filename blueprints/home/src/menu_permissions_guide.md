# Sistema Centralizado de Permisos del Menú

## Descripción General

Este sistema centraliza la gestión de permisos para los elementos del menú principal de la aplicación Flask.

## Configuración de Permisos

### Diccionario MENU_PERMISSIONS

Todos los permisos están definidos en `navbar_helpers.py` en el diccionario `MENU_PERMISSIONS`:

```python
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
```

## Funciones Disponibles

### 1. `get_all_permissions()`
Obtiene todos los permisos disponibles como una lista plana.

### 2. `get_module_permissions(module_name)`
Obtiene los permisos para un módulo específico.

### 3. `create_default_permissions(modules=None)`
Crea un diccionario de permisos por defecto para los módulos especificados.

**Ejemplo de uso:**
```python
# Crear permisos completos para todos los módulos
all_perms = create_default_permissions()

# Crear permisos solo para LesXon y Products
limited_perms = create_default_permissions(['lesxon', 'products'])
```

### 4. `has_module_permissions(user, module_name)`
Verifica si un usuario tiene al menos un permiso para un módulo específico.

### 5. `get_user_permission_summary(user)`
Obtiene un resumen completo de los permisos del usuario organizados por módulo.

## Implementación en Login

En `homeRoutes.py`, los permisos se crean usando:

```python
# Usuario con acceso completo
userPermissions = create_default_permissions(['lesxon', 'autotrackr', 'products'])

# Usuario con acceso limitado (sin LesXon)
userPermissions = create_default_permissions(['autotrackr', 'products'])
```

## Usuarios de Prueba

1. **test@example.com / password123**: Acceso completo a todos los módulos
2. **limited@example.com / password123**: Acceso limitado (sin LesXon)

## Verificación en Templates

En `navbar.html`, la verificación se hace con:

```html
{% if item.name == 'LesXon' %}
  {% if current_user and has_lesxon_permissions(current_user) %}
    {{ render_nav_item(item) }}
  {% endif %}
{% endif %}
```

## Agregar Nuevos Permisos

1. **Agregar al diccionario MENU_PERMISSIONS**:
   ```python
   'nuevo_modulo': {
       'nuevo_modulo_permiso1': 'Descripción del permiso',
       'nuevo_modulo_permiso2': 'Descripción del permiso'
   }
   ```

2. **Actualizar la asignación de permisos en homeRoutes.py**:
   ```python
   userPermissions = create_default_permissions(['lesxon', 'autotrackr', 'products', 'nuevo_modulo'])
   ```

3. **Actualizar NAV_CONFIG** en `navbar_helpers.py` para incluir los nuevos elementos del menú.

## Ventajas del Sistema

- ✅ **Centralizado**: Una sola fuente de verdad para los permisos
- ✅ **Mantenible**: Fácil de agregar/quitar permisos
- ✅ **Consistente**: Evita errores de tipeo
- ✅ **Flexible**: Permite crear usuarios con permisos específicos
- ✅ **Documentado**: Cada permiso tiene una descripción clara 