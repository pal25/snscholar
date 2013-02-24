from flask import request, current_app, session
from flask.ext.principal import Identity, identity_loaded, identity_changed, RoleNeed
from snscholar.users.models import User
from snscholar.extensions import db

import urllib
import re

def get_sso_username(sso_url='https://login.case.edu/cas/'):
    username = None
    if request.args.get('ticket'):
        ticket = request.args['ticket']
        validation_url = sso_url + "validate" + '?service=' + urllib.quote(_get_sso_service_url()) + '&ticket=' + urllib.quote(ticket)
        r = urllib.urlopen(validation_url).readlines()
        if len(r) == 2 and re.match("yes", r[0]) is not None:
            username = r[1].strip()
    return username


def get_sso_url(sso_url='https://login.case.edu/cas/'):
    # No valid ticket; redirect the browser to the login page to get one
    login_url = sso_url + 'login' + '?service=' + urllib.quote(_get_sso_service_url())
    return login_url


def _get_sso_service_url():
    if request.environ['PATH_INFO']:
        value = 'http://' + request.environ['HTTP_HOST'] + request.environ['PATH_INFO']
        value = re.sub(r'ticket=[^&]*&?', '', value)
        value = re.sub(r'\?&?$|&$', '', value)
        return value
    return None


def get_identity(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.username))
    else:
        user = User(username, username+'@case.edu', 'new')
        db.session.add(user)
        db.session.commit()
        identity_changed.send(current_app._get_current_object(), identity=Identity(user.username))


@identity_loaded.connect
def set_identity(sender, identity):
    user = User.query.filter_by(username=identity.name).first()
    identity.user = user.username
    identity.provides.add(RoleNeed(user.level))


def set_request(form):
    if 'identity.name' in session:
        username = session['identity.name']
        user = User.query.filter_by(username=username).first()
        if user.level == 'new':
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.level = 'pending'
            db.session.commit()
            return True
    return False