from flask import Blueprint, redirect, url_for, flash, render_template
from snscholar.extensions import pending_permission, user_permission, new_permission
from snscholar.users.controller import get_sso_username, get_sso_url, get_identity, set_request
from snscholar.users.forms import UserAccessForm

user = Blueprint('user', __name__, url_prefix='/u')

@user.route('/login')
def login():
    if not new_permission.can():
        username = get_sso_username()
        if username is None:
            return redirect(get_sso_url())
        else:
            get_identity(username)
            return redirect(url_for('user.index'))

    return redirect(url_for('user.index'))


@user.route('/request', methods=('GET', 'POST'))
def access():
    if pending_permission.can():
        flash('Already requested')
        return redirect(url_for('user.index'))
    elif new_permission.can():
        form = UserAccessForm()
        if form.validate_on_submit():
            success = set_request(form)
            if success:
                flash('Request Success!')
            else:
                flash('Request Failed!')
            return redirect(url_for('user.index'))
        else:
            return render_template('GenericForm.html', form=form)
    else:
        return redirect(url_for('user.index'))


@user.route('/')
def index():
    if user_permission.can() or pending_permission.can():
        return render_template('layout.html')
    elif new_permission.can():
        return redirect(url_for('user.access'))

    return redirect(url_for('user.login'))
