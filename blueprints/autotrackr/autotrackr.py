from flask import Blueprint

bp = Blueprint('autotrackr', __name__,
               static_folder='static',
               template_folder='templates')

from .routes import autotrackrRoutes 