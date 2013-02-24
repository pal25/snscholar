from snscholar.extensions import db
from snscholar.users.models import User

user_course_join = db.Table('user_course_join',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(63), nullable=False)
    instructor = db.Column(db.String(63), nullable=True)
    abbrev = db.Column(db.String(4), nullable=False)
    abbrevnum = db.Column(db.Integer(3), nullable=False)
    semester = db.Column(db.Enum('Spring', 'Summer', 'Fall'))
    year = db.Column(db.Integer(4), nullable=True)
    users = db.relationship('User', secondary=user_course_join, backref=db.backref('course', lazy='dynamic'))

    def __init__(self, title, instructor, abbrev, abbrevnum, semester, year):
        self.title = title
        self.instructor = instructor
        self.abbrev = abbrev
        self.abbrevnum = abbrevnum
        self.semester = semester
        self.year = year

    def __repr__(self):
        return '<Course: %r %r>' % self.abbrev, self.abbrevnum