from flask_smorest import Blueprint

bp = Blueprint('salons', __name__, description='Ops on salons', url_prefix='/salon')

from . import routes