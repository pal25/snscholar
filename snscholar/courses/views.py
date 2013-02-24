from flask import Blueprint, Response
from snscholar.courses.controller import get_course

course = Blueprint('course', __name__, url_prefix='/course')


@course.route('/')
def index():
    return Response('works!')

@course.route('/id/<int:id>')
def view_course(id):
    course = get_course(id)