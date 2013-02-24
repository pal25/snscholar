from snscholar.extensions import db
from snscholar.users.models import User
from snscholar.courses.models import Course


book_course_join = db.Table('book_course_join',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)


book_user_join = db.Table('book_user_join',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(63), nullalbe=False)
    isbn = db.Column()
    users = db.relationship('User', secondary=book_user_join, backref=db.backref('book', lazy='dynamic'))
    courses = db.relationship('Course', secondary=book_course_join, backref=db.backref('book', lazy='dynamic'))