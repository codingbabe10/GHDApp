from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from flask_smorest import abort

from models import stylist_Model
from schemas import stylistchema, StylistchemaNested

from . import bp
# stylist routes

@bp.route('/<stylist_id>')
class Stylist(MethodView):

  @bp.response(200, StylistSchemaNested)
  def get(self, stylist_id):
    stylist = StylistModel.query.get(stylist_id)
    if stylist:
      return stylist 
    abort(400, message='Invalid stylist')

  @jwt_required
  @bp.arguments(StylistSchema)
  def put(self, stylist_data, stylist_id):
    stylist = StylistModel.query.get(stylist_id)
    if stylist and stylist.user_id == get_jwt_identity():
      stylist.body = stylist_data['body']
      stylist.commit()   
      return {'message': 'stylist updated'}, 201
    return {'message': "Invalid stylist Id"}, 400
    
  @jwt_required()
  def delete(self, stylist_id):
    stylist = StylistModel.query.get(stylist_id)
    if stylist and stylist.user_id == get_jwt_identity():
      stylist.delete()
      return {"message": "stylist Deleted"}, 202
    return {'message':"Invalid stylist or User"}, 400

@bp.route('/')
class stylistList(MethodView):

  @bp.response(200, StylistSchemaNested(many = True))
  def get(self):
    return StylistModel.query.all()
  
  @jwt_required()
  @bp.arguments(StylistSchema)
  def stylist(self, stylist_data):
    try:
      stylist = StylistModel()
      stylist.user_id = get_jwt_identity() 
      stylist.body = stylist_data['body']
      stylist.commit()
      return { 'message': "stylist Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401