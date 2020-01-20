from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.dto import BlogDto
from ..service.blog_service import get_posts, save_new_post

api = BlogDto.blog_api
_blog = BlogDto.blog_meta
_blog_create = BlogDto.blog_meta_create

@api.route('/')
class PostListResource(Resource):
    @api.doc('list_of_posts')
    @token_required
    @api.marshal_list_with(_blog)
    def get(self):
        """List all posts"""
        return get_posts()
    
    @api.expect(_blog_create, validate=True)
    @api.response(201, 'Post successfully created.')
    @api.doc('create a new topic')
    def post(self):
        """Creates a new post"""
        data = request.json
        return save_new_post(data=data)

