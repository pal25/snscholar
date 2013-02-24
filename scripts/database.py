from flask.ext.script import Manager

from snscholar import create_app
from snscholar.extensions import db
from snscholar.users.models import User
from snscholar.courses.models import Course, user_course_join
from snscholar.books.models import Book, book_course_join, book_user_join


manager = Manager(create_app())
app = create_app()

@manager.command
def create_tables():
    db.drop_all()
    db.create_all()


@manager.command
def create_user():
    user = User('pal25', 'pal25@case.edu', 'dev')
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    manager.run()

