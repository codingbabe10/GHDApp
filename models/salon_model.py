from datetime import datetime

from app import db

class Salon_Model(db.Model):

  __tablename__ = 'salons'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String, nullable=False)
  address = db.Column(db.String, nullable = False)
  phone_number = db.Column(db.String, nullable = False)
  email= db.Column(db.String, nullable = False)
  stylist = db.relationship('StylistModel', back_populates = 'salon')

  def __repr__(self):
    return f'<Post: {self.name}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()