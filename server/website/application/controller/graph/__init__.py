from flask import Blueprint

graph_blueprint = Blueprint('graph_blueprint', __name__, url_prefix='/graph')

from . import views, errors