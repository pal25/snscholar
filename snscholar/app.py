import os

from flask import Flask, render_template
from snscholar.extensions import db, principal
from snscholar.config import DeveloperConfig
from snscholar.users import user
from snscholar.frontend import frontend


__all__ = ['create_app'] # For import *


DEFAULT_BLUEPRINTS = (
    user,
    frontend,
    )


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DeveloperConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config):
    """Configure app from object, parameter and env."""

    if config is not None:
        app.config.from_object(config)
    else:
        app.config.from_object(DeveloperConfig)
        # Override setting by env var without touching codes.
    app.config.from_envvar('%s_APP_CONFIG' % DeveloperConfig.PROJECT.upper(), silent=True)


def configure_extensions(app):
    db.init_app(app)            #Flask-SQLAlchemy
    principal.init_app(app)     #Flask-Principal


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_hook(app):
    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/forbidden_page.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/page_not_found.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/server_error.html'), 500