# -*- coding: utf-8 -*-
from flask import render_template

from . import dialogue_blueprint


@dialogue_blueprint.route('/')
def graph():
    return render_template('main/dialogue.html')

@dialogue_blueprint.route('/demo')
def demo():
    return render_template('dialogue/demo.html')