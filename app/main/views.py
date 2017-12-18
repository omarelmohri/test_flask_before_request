from . import main
from flask import session


@main.route('/')
def index():
    counts = str(session.get('pass', 0))
    return counts


@main.route('count')
def count():
    return 'running before_request for : ' + str(session.get('pass', 0))
