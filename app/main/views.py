from flask import render_template
from. import main
from ..models import User
from .. import db

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Pitchez'

    return render_template('auth/login.html', title = title)


