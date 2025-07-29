from flask import render_template,current_app, session

from ..lesxon import bp
from ...home.src.navbar_helpers import get_navbar_context

# Ruta para la página principal
@bp.route('/lesxon/zip')
def zip():

    # Parameters html
    parameter = {}
    parameter['route1'] = 'zip'

    # Get navbar context
    navbar_context = get_navbar_context(
        current_route='lesxon.zip',
        user=session.get('user')
    )

    return render_template('lesxon_zip.html', **navbar_context, parameter=parameter)          
