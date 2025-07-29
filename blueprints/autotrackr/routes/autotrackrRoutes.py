from flask import render_template, current_app, session
from ..autotrackr import bp
from ...home.src.navbar_helpers import get_navbar_context

@bp.route('/autotrackr/service_orders')
def service_orders():
    parameter = {'route1': 'Service Orders'}
    navbar_context = get_navbar_context(
        current_route='autotrackr.service_orders',
        user=session.get('user')
    )
    return render_template('autotrackr_service_orders.html', **navbar_context, parameter=parameter)

@bp.route('/autotrackr/erm_model')
def erm_model():
    parameter = {'route1': 'ERM Model'}
    navbar_context = get_navbar_context(
        current_route='autotrackr.erm_model',
        user=session.get('user')
    )
    return render_template('autotrackr_erm_model.html', **navbar_context, parameter=parameter)

@bp.route('/autotrackr/supabase')
def supabase():
    parameter = {'route1': 'Supabase'}
    navbar_context = get_navbar_context(
        current_route='autotrackr.supabase',
        user=session.get('user')
    )
    return render_template('autotrackr_supabase.html', **navbar_context, parameter=parameter) 