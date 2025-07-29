from flask import render_template,current_app, session

from ..lesxon import bp
from ...home.src.navbar_helpers import get_navbar_context

# Ruta para la página principal
@bp.route('/lesxon/klines')
def klines():

    # Parameters html
    parameter = {}
    parameter['route1'] = 'klines'

    # Get navbar context
    navbar_context = get_navbar_context(
        current_route='lesxon.klines',
        user=session.get('user')
    )

    return render_template('lesxon_klines.html', **navbar_context, parameter=parameter)          
