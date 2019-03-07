from flask import Blueprint

reading_comp_blueprint = Blueprint('reading_comp_blueprint', __name__, url_prefix='/reading_comp')

from . import views, errors