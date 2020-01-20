from .. import db, flask_bcrypt
import datetime


class Topic(db.Model):
    """ topic Model for storing topic related details """
    __tablename__ = "topic"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.String(255))
    created_on = db.Column(db.DateTime)
    name = db.Column(db.String(100))
    body = db.Column(db.String(800))
    posts = db.relationship('Blog')