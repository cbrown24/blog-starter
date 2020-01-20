from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.dto import BlogDto
from ..service.topic_service import get_topics, save_new_topic

api = BlogDto.api
_topic = BlogDto.topic_meta
_topic_create = BlogDto.topic_crate_meta

@api.route('/')
class TopicListResource(Resource):
    @api.doc('list_of_topics')
    @token_required
    @api.marshal_list_with(_topic)
    def get(self):
        """List all topics"""
        return get_topics()
    
    @api.expect(_topic_create, validate=True)
    @api.response(201, 'Topic successfully created.')
    @api.doc('create a new topic')
    @token_required
    def post(self):
        """Creates a new Topic"""
        data = request.json
        return save_new_topic(data=data)

