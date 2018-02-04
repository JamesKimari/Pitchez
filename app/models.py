from . import db

class User(db.Model):
    __table__name = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'