from flask import Blueprint, Response

frontend = Blueprint('frontend', __name__, url_prefix='/')

@frontend.route('/')
def index():
    return Response('index')