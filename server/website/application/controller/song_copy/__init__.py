from flask import Blueprint

song_copy_blueprint = Blueprint('song_copy_blueprint', __name__, url_prefix='/song_copy')

from . import views, errors