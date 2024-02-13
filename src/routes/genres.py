# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask_smorest import Blueprint
from flask.views import MethodView
# ******************************OWN LIBRARIES*********************************
from extensions import db
from src.models import GenreModel
from schemas import BasicGenreSchema, UpdateGenreSchema, CompleteGenreSchema, BasicDirectorSchema
# ***********************************CODE*************************************

blp = Blueprint("genres", __name__, description="All the genres functionalites", url_prefix="/api_movies")

@blp.route("/genres")
class Genre(MethodView):
    @blp.response(200, BasicGenreSchema(many=True))
    def get(self):
        '''This endpoint returns all the genres
        information in the database.'''
        genres = GenreModel.query.all()
        return genres

    @blp.arguments(BasicGenreSchema)
    @blp.response(200, BasicGenreSchema)
    def post(self, genre_data):
        genre = GenreModel(**genre_data)
        db.session.add(genre)
        db.session.commit()
        return genre

@blp.route("/genre/<string:genre_id>")
class GenreID(MethodView):
    @blp.response(200, CompleteGenreSchema)
    def get(self, genre_id):
        '''This endpoint returns a single
        genre information searched by ID.'''
        genre = GenreModel.query.get_or_404(genre_id)
        return genre

    @blp.arguments(UpdateGenreSchema)
    @blp.response(200, CompleteGenreSchema)
    def put(self, genre_data, genre_id):
        '''This endpoint updates a single
        genre information.'''
        genre = GenreModel.query.get_or_404(genre_id)
        for key, value in genre_data.items():
            setattr(genre, key, value)
        db.session.commit()
        return genre

    @blp.response(200, CompleteGenreSchema)
    def delete(self, genre_id):
        '''This endpoint cant exist, in real
        life we cant delete a genre and its
        movies and directors, just change its
        name and features'''
        genre = GenreModel.query.get_or_404(genre_id)
        db.session.delete(genre)
        db.session.commit()
        return genre
