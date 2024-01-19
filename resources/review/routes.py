from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort


from schemas import ReviewSchema, ReviewSchemaNested

from . import bp
# review routes

@bp.route('/<review_id>')
class Review(MethodView):

  @bp.response(200, ReviewSchemaNested)
  def get(self, review_id):
    review = reviewModel.query.get(review_id)
    if review:
      return review 
    abort(400, message='Invalid review')

  @jwt_required
  @bp.arguments(ReviewSchema)
  def put(self, review_data, review_id):
    review = reviewModel.query.get(review_id)
    if review and review.user_id == get_jwt_identity():
      review.body = review_data['body']
      review.commit()   
      return {'message': 'review updated'}, 201
    return {'message': "Invalid review Id"}, 400
    
  @jwt_required()
  def delete(self, review_id):
    review = reviewModel.query.get(review_id)
    if review and review.user_id == get_jwt_identity():
      review.delete()
      return {"message": "review Deleted"}, 202
    return {'message':"Invalid review or User"}, 400

@bp.route('/')
class reviewList(MethodView):

  @bp.response(200, ReviewSchema(many = True))
  def get(self):
    return reviewModel.query.all()
  
  @jwt_required()
  @bp.arguments(ReviewSchema)
  def post(self, review_data):
    try:
      review = reviewModel()
      review.user_id = get_jwt_identity() 
      review.body = review_data['body']
      review.commit()
      return { 'message': "review Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401