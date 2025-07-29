from flask import render_template, current_app, request, flash, session
from datetime import datetime

from ..lesxon import bp
from ...home.src.navbar_helpers import get_navbar_context

# Ruta para la página principal
@bp.route('/lesxon/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        # Get form data
        symbol = request.form.get('symbol', '').strip().upper()
        start_date = request.form.get('start_date', '').strip()
        end_date = request.form.get('end_date', '').strip()
        transaction_type = request.form.get('transaction_type', '').strip()
        min_amount = request.form.get('min_amount', '').strip()
        max_amount = request.form.get('max_amount', '').strip()
        
        # Validation
        errors = {}
        
        if symbol and len(symbol) < 3:
            errors['symbol'] = 'El símbolo debe tener al menos 3 caracteres'
            
        if start_date and end_date:
            try:
                start_dt = datetime.strptime(start_date, '%Y-%m-%d')
                end_dt = datetime.strptime(end_date, '%Y-%m-%d')
                if start_dt > end_dt:
                    errors['end_date'] = 'La fecha fin debe ser posterior a la fecha inicio'
            except ValueError:
                errors['start_date'] = 'Formato de fecha inválido'
                
        if min_amount:
            try:
                min_val = float(min_amount)
                if min_val < 0:
                    errors['min_amount'] = 'El monto mínimo no puede ser negativo'
            except ValueError:
                errors['min_amount'] = 'Ingresa un monto válido'
                
        if max_amount:
            try:
                max_val = float(max_amount)
                if max_val < 0:
                    errors['max_amount'] = 'El monto máximo no puede ser negativo'
                if min_amount and float(min_amount) > max_val:
                    errors['max_amount'] = 'El monto máximo debe ser mayor al mínimo'
            except ValueError:
                errors['max_amount'] = 'Ingresa un monto válido'
        
        if errors:
            navbar_context = get_navbar_context(
                current_route='lesxon.transactions',
                user=session.get('user')
            )
            return render_template('lesxon_transactions.html', errors=errors, **navbar_context)
        
        # Simulate search results (replace with real database query)
        transactions = [
            [
                '<span class="text-muted">2024-07-26 10:30:00</span>',
                f'<span class="badge badge-primary">{symbol or "BTCUSDT"}</span>',
                '<span class="badge badge-success"><i class="fas fa-arrow-up mr-1"></i>Compra</span>',
                '<span class="font-weight-bold text-success">$1,500.00</span>',
                '<span class="text-muted">$62,500.00</span>',
                '<div class="btn-group btn-group-sm" role="group">' +
                '<button class="btn btn-outline-primary" title="Ver detalles"><i class="fas fa-eye"></i></button>' +
                '<button class="btn btn-outline-info" title="Exportar"><i class="fas fa-download"></i></button>' +
                '</div>'
            ],
            [
                '<span class="text-muted">2024-07-25 15:45:00</span>',
                f'<span class="badge badge-primary">{symbol or "ETHUSDT"}</span>',
                '<span class="badge badge-danger"><i class="fas fa-arrow-down mr-1"></i>Venta</span>',
                '<span class="font-weight-bold text-danger">$950.00</span>',
                '<span class="text-muted">$3,100.00</span>',
                '<div class="btn-group btn-group-sm" role="group">' +
                '<button class="btn btn-outline-primary" title="Ver detalles"><i class="fas fa-eye"></i></button>' +
                '<button class="btn btn-outline-info" title="Exportar"><i class="fas fa-download"></i></button>' +
                '</div>'
            ]
        ]
        
        total_transactions = 150  # Simulated total
        page = 1
        per_page = 10

        success = f'Búsqueda completada. Se encontraron {len(transactions)} resultados.'
        navbar_context = get_navbar_context(
            current_route='lesxon.transactions',
            user=session.get('user')
        )
        return render_template(
            'lesxon_transactions.html', 
            success=success, 
            transactions=transactions,
            total_transactions=total_transactions,
            page=page,
            per_page=per_page,
            **navbar_context
        )

    # GET request - show transactions page
    navbar_context = get_navbar_context(
        current_route='lesxon.transactions',
        user=session.get('user')
    )
    return render_template('lesxon_transactions.html', **navbar_context)          
