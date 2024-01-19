from flask_smorest import Blueprint

bp = Blueprint('reviews', __name__, description='Ops on reviews', url_prefix='/review')

from . import routes