from flask import Blueprint

# Definición del Blueprint principal
bp = Blueprint('lesxon', __name__,
               static_folder='static/img',
               template_folder='templates')

# Routes
from .routes import viewRoutes
from .routes import downloadRoutes
from .routes import zipRoutes
from .routes import transactionsRoutes
from .routes import klinesRoutes
from .routes import supabaseRoutes
