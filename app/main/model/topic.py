from .. import db, flask_bcrypt
import datetime
from flask import request
from ..service.auth_helper import Auth


class Topic(db.Model):
    """ topic Model for storing topic related details """
    __tablename__ = "topic"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.String(255))
    created_on = db.Column(db.DateTime)
    name = db.Column(db.String(100))
    body = db.Column(db.String(800))
    posts = db.relationship('Blog')

    def __init__(self ,*args, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
        try:
            self.created_by = Auth.get_logged_in_user(request)[0]['data']['user_id']
        except (IndexError, KeyError):
            self.created_by = 'unknown'
        self.created_on = datetime.datetime.utcnow()

    def __repr__(self):
        return '<id:{self.id} title: {self.name}>'.format(self=self)