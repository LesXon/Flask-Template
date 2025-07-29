from flask import Blueprint

# Definición del Blueprint principal
bp = Blueprint('home', __name__,
               static_folder='static/img',
               template_folder='templates')

# Routes
from .routes import homeRoutes
