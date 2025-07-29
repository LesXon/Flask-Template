from flask import render_template,current_app

from ..pruebas import bp

# Ruta para la página principal
@bp.route('/route1')
def home():
    # Parameters html
    parameter = {}
    parameter['route1'] = 'Plantilla Estándar para Blueprints'

    return render_template('route1.html', parameter=parameter)          
