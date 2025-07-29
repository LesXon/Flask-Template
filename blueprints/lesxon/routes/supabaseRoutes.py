from flask import render_template,current_app, session

from ..lesxon import bp
from ...home.src.navbar_helpers import get_navbar_context

# Ruta para la página principal
@bp.route('/lesxon/supabase')
def supabase():

    # Parameters html
    parameter = {}
    parameter['route1'] = 'supabase'

    # Get navbar context
    navbar_context = get_navbar_context(
        current_route='lesxon.supabase',
        user=session.get('user')
    )

    return render_template('lesxon_supabase.html', **navbar_context, parameter=parameter)          
