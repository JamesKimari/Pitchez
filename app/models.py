from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    password_lock = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'category', lazy = 'dynamic')

    def __repr__(self):
        return f'Pitch {self.name}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    pitch_content = db.Column(db.String())
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    published_at = db.Column(db.DateTime, default = datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    