# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from marshmallow import Schema, fields
# ******************************OWN LIBRARIES*********************************

# ***********************************CODE*************************************
class BasicMovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    year = fields.Integer(required=False)
    oscar_winner = fields.Boolean(required=False)

class BasicDirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)

class BasicGenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    classification = fields.String(required=False)

class UpdateMovieSchema(Schema):
    name = fields.String()
    director_id = fields.String()
    year = fields.Integer()
    oscar_winner = fields.Boolean()

class UpdateDirectorSchema(Schema):
    name = fields.String()
    genre_id = fields.String()

class UpdateGenreSchema(Schema):
    name = fields.String()
    classification = fields.String()

class CompleteMovieSchema(BasicMovieSchema):
    director_id = fields.String(required=True, load_only=True)
    directors = fields.Nested(BasicDirectorSchema(), dump_only=True)
    genres = fields.List(fields.Nested(BasicGenreSchema()), dump_only=True)

class CompleteDirectorSchema(BasicDirectorSchema):
    genre_id = fields.String(required=True, load_only=True)
    movies = fields.List(fields.Nested(BasicMovieSchema()), dump_only=True)
    genres = fields.Nested(BasicGenreSchema(), dump_only=True)

class CompleteGenreSchema(BasicGenreSchema):
    movies = fields.List(fields.Nested(BasicMovieSchema()), dump_only=True)
    directors = fields.List(fields.Nested(BasicDirectorSchema()), dump_only=True)

class MovieGenreSchema(Schema):
    movies = fields.Nested(BasicMovieSchema())
    genres = fields.Nested(CompleteGenreSchema())

