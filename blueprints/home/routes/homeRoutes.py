import os
import datetime

import platform
from pathlib import Path

from flask import render_template, session, redirect, url_for, request, flash

from ..home import bp
from ..src.navbar_helpers import get_navbar_context, create_default_permissions

@bp.route('/')
def home():

    # Implementation      
    currentDirectory = os.getcwd()   
    operating_system = platform.platform()

    user_os = os.getlogin()
 
    documents_path = Path.home()   

    currentDirectory = os.getcwd()         

    # Get the current date and time object
    now = datetime.datetime.now()

    # Converts date and time object to timestamp in seconds
    timestamp = str(int(datetime.datetime.timestamp(now)))

    # Get user from session if available
    user = session.get('user')

    username = user.get('user') if user else 'Guest'

    # Get navbar context using the helper function
    navbar_context = get_navbar_context(current_route='home.home', user=user)

    # Parameters html
    parameter = {}
    parameter['operating_system'] = str(operating_system)
    parameter['user'] = str(username)
    parameter['documents_path'] = str(documents_path / "Documents")
    parameter['currentDirectory'] = str(currentDirectory)
    parameter['timestamp'] = str(timestamp)

    return render_template('home.html', parameter=parameter, **navbar_context)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        remember = request.form.get('remember') == '1'
        
        # Validation
        errors = {}
        
        if not email:
            errors['email'] = 'El correo electrónico es requerido'
        elif '@' not in email or '.' not in email.split('@')[-1]:
            errors['email'] = 'Ingresa un correo electrónico válido'
            
        if not password:
            errors['password'] = 'La contraseña es requerida'
        elif len(password) < 6:
            errors['password'] = 'La contraseña debe tener al menos 6 caracteres'
        
        if errors:
            # Get navbar context
            navbar_context = get_navbar_context(current_route='home.login')
            return render_template('login.html', errors=errors, **navbar_context)
        
        # Simulate authentication (replace with real authentication)
        if email == 'test@example.com' and password == 'password123':
            
            # Create user permissions using centralized configuration - FULL ACCESS
            userPermissions = create_default_permissions(['lesxon', 'autotrackr', 'products'])

            user_data = {}
            user_data['user'] = email.split('@')[0]
            user_data['email'] = email
            user_data['is_authenticated'] = True
            user_data['avatar'] = 'https://via.placeholder.com/24'
            user_data['notification_count'] = 5
            user_data['permissions'] = userPermissions

            session['user'] = user_data
            session.permanent = remember
            
            flash('¡Bienvenido! Has iniciado sesión correctamente (acceso completo).', 'success')
            return redirect(url_for('home.home'))
            
        elif email == 'limited@example.com' and password == 'password123':
            
            # Create user with LIMITED permissions - only autotrackr and products, NO lesxon
            userPermissions = create_default_permissions(['lesxon', 'autotrackr', 'products'])

            user_data = {}
            user_data['user'] = email.split('@')[0]
            user_data['email'] = email
            user_data['is_authenticated'] = True
            user_data['avatar'] = 'https://via.placeholder.com/24'
            user_data['notification_count'] = 3
            user_data['permissions'] = userPermissions

            session['user'] = user_data
            session.permanent = remember
            
            flash('¡Bienvenido! Has iniciado sesión correctamente (acceso limitado).', 'success')
            return redirect(url_for('home.home'))
            
        else:
            error = 'Credenciales incorrectas. Intenta con:<br>• test@example.com / password123 (acceso completo)<br>• limited@example.com / password123 (sin acceso a LesXon)'
            navbar_context = get_navbar_context(current_route='home.login')
            return render_template('login.html', error=error, **navbar_context)
    
    # GET request - show login form
    navbar_context = get_navbar_context(current_route='home.login')
    return render_template('login.html', **navbar_context)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()
        phone = request.form.get('phone', '').strip()
        terms = request.form.get('terms') == '1'
        newsletter = request.form.get('newsletter') == '1'
        
        # Validation
        errors = {}
        
        if not first_name:
            errors['first_name'] = 'El nombre es requerido'
        elif len(first_name) < 2:
            errors['first_name'] = 'El nombre debe tener al menos 2 caracteres'
            
        if not last_name:
            errors['last_name'] = 'El apellido es requerido'
        elif len(last_name) < 2:
            errors['last_name'] = 'El apellido debe tener al menos 2 caracteres'
            
        if not email:
            errors['email'] = 'El correo electrónico es requerido'
        elif '@' not in email or '.' not in email.split('@')[-1]:
            errors['email'] = 'Ingresa un correo electrónico válido'
            
        if not password:
            errors['password'] = 'La contraseña es requerida'
        elif len(password) < 8:
            errors['password'] = 'La contraseña debe tener al menos 8 caracteres'
        elif not any(c.isupper() for c in password):
            errors['password'] = 'La contraseña debe incluir al menos una mayúscula'
        elif not any(c.islower() for c in password):
            errors['password'] = 'La contraseña debe incluir al menos una minúscula'
        elif not any(c.isdigit() for c in password):
            errors['password'] = 'La contraseña debe incluir al menos un número'
            
        if not confirm_password:
            errors['confirm_password'] = 'Debes confirmar tu contraseña'
        elif password != confirm_password:
            errors['confirm_password'] = 'Las contraseñas no coinciden'
            
        if phone and len(phone) < 10:
            errors['phone'] = 'Ingresa un número de teléfono válido'
            
        if not terms:
            errors['terms'] = 'Debes aceptar los términos y condiciones'
        
        if errors:
            navbar_context = get_navbar_context(current_route='home.register')
            return render_template('register.html', errors=errors, **navbar_context)
        
        # Simulate user registration (replace with real registration logic)
        try:
            # In a real app, you would save to database here
            # For demo purposes, we'll just simulate success
            
            success = f'¡Cuenta creada exitosamente para {first_name} {last_name}! Ahora puedes iniciar sesión.'
            navbar_context = get_navbar_context(current_route='home.login')
            return render_template('login.html', success=success, **navbar_context)
            
        except Exception as e:
            error = 'Ocurrió un error al crear la cuenta. Por favor intenta nuevamente.'
            navbar_context = get_navbar_context(current_route='home.register')
            return render_template('register.html', error=error, **navbar_context)
    
    # GET request - show registration form
    navbar_context = get_navbar_context(current_route='home.register')
    return render_template('register.html', errors={}, **navbar_context)    

@bp.route('/logout')
def logout():
    # Clear the user session
    session.clear()
    # Redirect to the home page
    return redirect(url_for('home.home'))