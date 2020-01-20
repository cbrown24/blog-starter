from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class BlogDto:
    api = Namespace('topic', description='blog topic related operations')
    blog_api = Namespace('posts', description='blog topic related operations')
    blog_meta = api.model('blog_meta', {
        'created_by': fields.String(required=True, description="The creator of the blog post"),
        'created_on': fields.DateTime(required=True, description="The time the blog post was created"),
        'title': fields.String(required=True, description="The title of the blog post"),
        'body': fields.String(required=True, description="The body of the blog post"),
        'topic_id': fields.Integer(required=True, description="The body of the blog post"),
    })
    blog_meta_create = api.model('blog_meta_create', {
        'title': fields.String(required=True, description="The title of the blog post"),
        'body': fields.String(required=True, description="The body of the blog post"),
        'topic_id': fields.Integer(required=True, description="The body of the blog post"),
    })
    topic_meta = api.model('topic_meta', {
        'name': fields.String(required=True, description='The name of the topic'),
        'created_by': fields.String(required=True, description="The creator of the blog post"),
        'created_on': fields.DateTime(required=True, description="The time the blog post was created"),
        'posts': fields.List(fields.Nested(blog_meta), required=False),
        'id': fields.Integer(required=False)
    })
    topic_crate_meta = api.model('topic_create_meta', {
        'name': fields.String(required=True, description='The name of the topic'),
    })