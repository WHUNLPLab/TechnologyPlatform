# -*- coding: utf-8 -*-
from flask import render_template

from . import intention_blueprint


@intention_blueprint.route('/')
def index():
    return render_template('main/intention.html')


@intention_blueprint.route('/demo')
def demo():
    return render_template('intention/demo.html')
