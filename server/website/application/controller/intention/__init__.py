from flask import Blueprint

intention_blueprint = Blueprint('intention_blueprint', __name__, url_prefix='/intention')

from . import views, errors