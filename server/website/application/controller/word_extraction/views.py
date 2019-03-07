# -*- coding: utf-8 -*-
from flask import render_template

from . import word_extraction_blueprint


@word_extraction_blueprint.route('/')
def index():
    return render_template('main/word_extraction.html')


@word_extraction_blueprint.route('/demo')
def demo():
    return render_template('word_extraction/demo.html')
