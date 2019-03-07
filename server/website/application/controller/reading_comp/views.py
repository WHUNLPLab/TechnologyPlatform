# -*- coding: utf-8 -*-
from flask import render_template

from application.controller.intention import intention_blueprint
from . import reading_comp_blueprint


@reading_comp_blueprint.route('/')
def index():
    return render_template('main/reading_comp.html')

@reading_comp_blueprint.route('/demo')
def demo():
    return render_template('reading_comp/demo.html')

