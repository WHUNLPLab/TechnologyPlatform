# -*- coding: utf-8 -*-
from flask import render_template
from . import song_copy_blueprint


@song_copy_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@song_copy_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500