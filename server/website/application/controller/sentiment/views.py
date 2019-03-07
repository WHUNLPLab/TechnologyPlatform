# -*- coding: utf-8 -*-
from flask import render_template

from . import sentiment_blueprint


@sentiment_blueprint.route('/')
def index():
    return render_template('main/sentiment.html')

@sentiment_blueprint.route('/demo')
def demo():
    return render_template('sentiment/demo.html')