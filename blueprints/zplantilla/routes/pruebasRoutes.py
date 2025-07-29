from flask import render_template, current_app, request, flash, redirect, url_for
from ..pruebas import bp

@bp.route('/pruebas')
def pruebas():
    # Parameters html
    parameter = {}
    parameter['pruebas'] = 'Demostración de Componentes UI'

    return render_template('pruebas.html', parameter=parameter)            

@bp.route('/test')
def test():
    return render_template('test.html')

@bp.route('/test2')
def test2():
    return render_template('test2.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        copy = request.form.get('copy') == '1'
        
        # Validation
        errors = {}
        
        if not name:
            errors['name'] = 'El nombre es requerido'
        elif len(name) < 2:
            errors['name'] = 'El nombre debe tener al menos 2 caracteres'
            
        if not email:
            errors['email'] = 'El correo electrónico es requerido'
        elif '@' not in email or '.' not in email.split('@')[-1]:
            errors['email'] = 'Ingresa un correo electrónico válido'
            
        if phone and len(phone) < 10:
            errors['phone'] = 'Ingresa un número de teléfono válido'
            
        if not subject:
            errors['subject'] = 'Selecciona un asunto'
            
        if not message:
            errors['message'] = 'El mensaje es requerido'
        elif len(message) < 10:
            errors['message'] = 'El mensaje debe tener al menos 10 caracteres'
        
        if errors:
            return render_template('contact_form.html', errors=errors)
        
        # Simulate sending email (replace with real email sending logic)
        try:
            # In a real app, you would send email here
            # For demo purposes, we'll just simulate success
            
            success = f'¡Gracias {name}! Tu mensaje ha sido enviado correctamente. Te responderemos pronto.'
            return render_template('contact_form.html', success=success)
            
        except Exception as e:
            error = 'Ocurrió un error al enviar el mensaje. Por favor intenta nuevamente.'
            return render_template('contact_form.html', error=error)
    
    # GET request - show contact form
    return render_template('contact_form.html')