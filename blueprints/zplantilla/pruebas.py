from flask import Blueprint

# Definición del Blueprint principal
bp = Blueprint('pruebas', __name__,
               static_folder='static',
               template_folder='templates')

# Routes
from .routes import pruebasRoutes
from .routes import route1Routes