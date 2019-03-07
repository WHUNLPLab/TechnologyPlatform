# -*- coding: utf-8 -*-
from flask import render_template

from . import ans_gen_blueprint

@ans_gen_blueprint.route('/')
def index():
    return render_template('main/ans_gen.html')

@ans_gen_blueprint.route('/demo')
def demo():
    return render_template('ans_gen/demo.html')

