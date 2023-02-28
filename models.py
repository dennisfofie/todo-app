from app import db
from datetime import datetime

# create database
class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return "<Title> {}".format(self.title)