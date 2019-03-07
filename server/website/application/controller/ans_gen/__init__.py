from flask import Blueprint

ans_gen_blueprint = Blueprint('ans_gen_blueprint', __name__, url_prefix='/ans_gen')

from . import views, errors