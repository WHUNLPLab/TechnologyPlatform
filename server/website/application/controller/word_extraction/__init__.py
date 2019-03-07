from flask import Blueprint

word_extraction_blueprint = Blueprint('word_extraction_blueprint', __name__, url_prefix='/word_extraction')

from . import views, errors