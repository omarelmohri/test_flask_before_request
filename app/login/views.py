from . import login
from flask import session


@login.route('/')
def login():
    return 'FROM LOGIN = running before_request for : ' + str(session.get('pass', 0))
