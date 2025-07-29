from flask import render_template,current_app, session
import datetime

from ..lesxon import bp
from ...home.src.navbar_helpers import get_navbar_context

# Ruta para la página principal
@bp.route('/lesxon/download')
def download():

    # Parameters html
    parameter = {}
    parameter['route1'] = 'download'

    # Get navbar context
    navbar_context = get_navbar_context(
        current_route='lesxon.download',
        user=session.get('user')
    )

    # TODO: Replace with actual data from Supabase or other DB
    download_history = [
        {
            "id": "1",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": "K-Lines",
            "symbol": "BTCUSDT",
            "format": "CSV",
            "size": "2.5 MB",
            "status": "Completado",
            "filename": "btc_klines_20240115.csv"
        },
        {
            "id": "2",
            "date": (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"),
            "type": "Trades",
            "symbol": "ETHUSDT",
            "format": "JSON",
            "size": "1.8 MB",
            "status": "Completado",
            "filename": "eth_trades_20240115.json"
        },
        {
            "id": "3",
            "date": (datetime.datetime.now() - datetime.timedelta(hours=2)).strftime("%Y-%m-%d %H:%M"),
            "type": "Ticker",
            "symbol": "ADAUSDT",
            "format": "XLSX",
            "size": "0.5 MB",
            "status": "Error",
            "filename": "ada_ticker_20240115.xlsx"
        }
    ]

    return render_template('lesxon_download.html', **navbar_context, parameter=parameter, download_history=download_history)          
