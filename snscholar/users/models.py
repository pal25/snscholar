from snscholar.extensions import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    firstname = db.Column(db.String(64), nullable=True)
    lastname = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(256), nullable=False)
    level = db.Column(db.Enum('banned', 'new', 'pending', 'user', 'admin', 'dev'), nullable=False, default='new')

    def __init__(self, username, email, level):
        self.username = username
        self.email = email
        self.level = level

    def __repr__(self):
        return '<User: %r (Level: %r)>' % self.username, self.level