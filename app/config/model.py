from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    avatar = db.Column(db.String(100), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"('id': {self.id}, 'username': {self.username}, 'email': {self.email},'name': {self.name},'avatar': {self.avatar})"