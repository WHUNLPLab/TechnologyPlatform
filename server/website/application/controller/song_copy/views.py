# -*- coding: utf-8 -*-
from flask import render_template

from . import song_copy_blueprint


@song_copy_blueprint.route('/')
def graph():
    return render_template('main/song_copy.html')

