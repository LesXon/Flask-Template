from flask import render_template,current_app, session
from ..lesxon import bp
from ...home.src.navbar_helpers import get_navbar_context

@bp.route('/lesxon/view')
def lesxon_view():

    # Parameters html
    parameter = {}
    parameter['route1'] = 'LesXon View'

    # Get navbar context
    navbar_context = get_navbar_context(
        current_route='lesxon.view',
        user=session.get('user')
    )

    # return render_template('lesxon_view.html',parameter=parameter)
    return render_template('lesxon_view.html', **navbar_context, parameter=parameter)            
