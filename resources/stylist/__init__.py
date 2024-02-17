from flask_smorest import Blueprint

bp = Blueprint('stylists', __name__, description='Ops on stylists', url_prefix='/stylist')

from . import routes