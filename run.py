from app import create_app
from flask import session


app = create_app('default')


@app.before_request
def before_request():
    # run before request
    # track using flask session
    if session.get('pass', False):
        session['pass'] += 1
    else:
        session['pass'] = 1
    pass
