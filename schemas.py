from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  email = fields.Str(required = True)
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  first_name = fields.Str()
  last_name = fields.Str()
  # token = fields.Str( load_only = True )

class UserLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )

class PostSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  timestamp = fields.DateTime(dump_only = True)

class PostSchemaNested(PostSchema):
  user = fields.Nested(UserSchema, dump_only = True)

class UserSchemaNested(UserSchema):
  posts = fields.List(fields.Nested(PostSchema), dump_only=True)
  # followed = fields.List(fields.Nested(UserSchema))
  followed = fields.Function(lambda user: {followed.id: UserSchema().dump(followed) for followed in user.followed} )



















class StylistSchema(Schema):
  id = fields.Str(dump_only = True)
  name = fields.Str(required = True)
  email = fields.Str(required = True)
  phone_number = fields.Str()
  address = fields.Str()
  
  # token = fields.Str( load_only = True )



class SalonSchema(Schema):
  id = fields.Str(dump_only = True)
  name = fields.Str(required = True)
  email = fields.Str(required = True)
  phone_number = fields.Str()
  address = fields.Str()






# class SalonSchema(Schema):
#   id = fields.Str(dump_only = True)
#   name = fields.Str(required = True)
#   address = fields.Str(required = True)                      

class SalonSchemaNested(SalonSchema):
  stylist = fields.Nested(UserSchema, dump_only = True)



class StylistSchemaNested(StylistSchema):
  salons = fields.List(fields.Nested(SalonSchema), dump_only=True)
  # followed = fields.List(fields.Nested(UserSchema))
  followed = fields.Function(lambda user: {followed.id: SalonSchema().dump(followed) for followed in user.followed} )



