from marshmallow import Schema, fields

class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  email = fields.Str(required = True)
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )
  first_name = fields.Str()
  last_name = fields.Str()

class UserLogin(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True )

class ReviewSchema(Schema):
  id = fields.Str(dump_only = True)
  body = fields.Str(required = True)
  timestamp = fields.DateTime(dump_only = True)

class ReviewSchemaNested(ReviewSchema):
  user = fields.Nested(UserSchema, dump_only = True)

class UserSchemaNested(UserSchema):
  reviews = fields.List(fields.Nested(ReviewSchema), dump_only=True)