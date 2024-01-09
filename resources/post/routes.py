from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import PostModel
from schemas import PostSchema, PostSchemaNested

from . import bp
# post routes

@bp.route('/<post_id>')
class Post(MethodView):

  @bp.response(200, PostSchemaNested)
  def get(self, post_id):
    post = PostModel.query.get(post_id)
    if post:
      return post 
    abort(400, message='Invalid Post')

  @jwt_required
  @bp.arguments(PostSchema)
  def put(self, post_data, post_id):
    post = PostModel.query.get(post_id)
    if post and post.user_id == get_jwt_identity():
      post.body = post_data['body']
      post.commit()   
      return {'message': 'post updated'}, 201
    return {'message': "Invalid Post Id"}, 400
    
  @jwt_required()
  def delete(self, post_id):
    post = PostModel.query.get(post_id)
    if post and post.user_id == get_jwt_identity():
      post.delete()
      return {"message": "Post Deleted"}, 202
    return {'message':"Invalid Post or User"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchema(many = True))
  def get(self):
    return PostModel.query.all()
  
  @jwt_required()
  @bp.arguments(PostSchema)
  def post(self, post_data):
    try:
      post = PostModel()
      post.user_id = get_jwt_identity() 
      post.body = post_data['body']
      post.commit()
      return { 'message': "Post Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401