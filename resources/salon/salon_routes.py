from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from flask_smorest import abort

from models import Salon_Model
from schemas import Salonchema, SalonchemaNested

from . import bp
# salon routes

@bp.route('/<salon_id>')
class Salon(MethodView):

  @bp.response(200, SalonSchemaNested)
  def get(self, salon_id):
    salon = SalonModel.query.get(salon_id)
    if salon:
      return salon 
    abort(400, message='Invalid salon')

  @jwt_required
  @bp.arguments(SalonSchema)
  def put(self, salon_data, salon_id):
    salon = SalonModel.query.get(salon_id)
    if salon and salon.user_id == get_jwt_identity():
      salon.body = salon_data['body']
      salon.commit()   
      return {'message': 'salon updated'}, 201
    return {'message': "Invalid salon Id"}, 400
    
  @jwt_required()
  def delete(self, salon_id):
    salon = SalonModel.query.get(salon_id)
    if salon and salon.user_id == get_jwt_identity():
      salon.delete()
      return {"message": "salon Deleted"}, 202
    return {'message':"Invalid salon or User"}, 400

@bp.route('/')
class salonList(MethodView):

  @bp.response(200, SalonSchemaNested(many = True))
  def get(self):
    return SalonModel.query.all()
  
  @jwt_required()
  @bp.arguments(SalonSchema)
  def salon(self, salon_data):
    try:
      salon = SalonModel()
      salon.user_id = get_jwt_identity() 
      salon.body = salon_data['body']
      salon.commit()
      return { 'message': "salon Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401