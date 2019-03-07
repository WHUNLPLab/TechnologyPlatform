from flask import Blueprint

sentiment_blueprint = Blueprint('sentiment_blueprint', __name__, url_prefix='/sentiment')

from . import views, errors