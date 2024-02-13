# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask_smorest import Blueprint, abort
from flask.views import MethodView
# ******************************OWN LIBRARIES*********************************
from extensions import db
from src.models import MovieModel
from schemas import BasicMovieSchema, UpdateMovieSchema
# ***********************************CODE*************************************

blp = Blueprint("movies", __name__, description="All movies functionalities", url_prefix="/api_movies")

@blp.route("/movies")
class Movie(MethodView):
    @blp.response(200, BasicMovieSchema(many=True))
    def get(self):
        movies = MovieModel.query.all()
        return movies

    @blp.arguments(BasicMovieSchema)
    @blp.response(200, BasicMovieSchema)
    def post(self, movie_data):
        '''This endpoint creates a new
        movie into the database.'''
        movie = MovieModel(**movie_data)
        db.session.add(movie)
        db.session.commit()
        return movie


@blp.route("/movie/<string:movie_id>")
class MovieID(MethodView):
    @blp.response(200, BasicMovieSchema)
    def get(self, movie_id):
        '''This endpoint return a single
        Movie information searched by ID.'''
        movie = MovieModel.query.get_or_404(movie_id)
        return movie

    @blp.response(200, BasicMovieSchema)
    def delete(self, movie_id):
        '''This endpoint delete a movie
        from the database by ID.'''
        movie = MovieModel.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return movie

    @blp.arguments(UpdateMovieSchema)
    @blp.response(200, BasicMovieSchema)
    def put(self, movie_data, movie_id):
        '''This endpoint update a Movie
        founded by ID.'''
        movie = MovieModel.query.get_or_404(movie_id)
        for key, value in movie_data.items():
            setattr(movie, key, value)
        db.session.commit()
        return movie





