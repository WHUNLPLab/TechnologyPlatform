# -*- coding: utf-8 -*-
from flask import render_template
from . import ans_gen_blueprint


@ans_gen_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@ans_gen_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500