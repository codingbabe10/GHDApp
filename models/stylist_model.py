from datetime import datetime

from app import db

class Stylist_Model(db.Model):

  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String)
  address = db.Column(db.String, nullable = False)
  phone_number = db.Column(db.Integer, nullable = False)
  email= db.Column(db.String, nullable = False)
  salon = db.relationship('SalonModel', back_populates = 'salon')

  def __repr__(self):
    return f'<Post: {self.body}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()