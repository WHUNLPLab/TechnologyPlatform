from flask import Blueprint

dialogue_blueprint = Blueprint('dialogue_blueprint', __name__, url_prefix='/dialogue')

from . import views, errors