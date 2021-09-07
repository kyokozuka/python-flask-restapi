from dataclasses import dataclass

from src.infrastracture.database import db

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    
    email: str = db.Column(db.String(128), primary_key=True)
    first_name: str = db.Column(db.String(128))
    last_name: str = db.Column(db.String(128))
    first_name_kana: str = db.Column(db.String(128))
    last_name_kana: str = db.Column(db.String(128))
    gender: int = db.Column(db.Integer)
    address: str = db.Column(db.String(255))
    
    def __repr__(self):
        return '<User %r>' % self.email