from .. import db, flask_bcrypt
import datetime
from flask import request
from ..service.auth_helper import Auth

class Blog(db.Model):
    """ User Model for storing blog post related details """
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.String(255), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(100), unique=False)
    body = db.Column(db.String(800), unique=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))


    def __init__(self ,*args, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
        try:
            self.created_by = Auth.get_logged_in_user(request)[0]['data']['user_id']
        except (IndexError, KeyError):
            self.created_by = 'unknown'
        self.created_on = datetime.datetime.utcnow()

    def __repr__(self):
        return '<id:{self.id} title: {self.title}>'.format(self=self)

