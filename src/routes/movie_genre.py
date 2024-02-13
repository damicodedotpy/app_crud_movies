# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask_smorest import Blueprint
from flask.views import MethodView
from flask_restful import marshal_with
# ******************************OWN LIBRARIES*********************************
from extensions import db
from src.models import MovieModel, GenreModel
from schemas import MovieGenreSchema, CompleteGenreSchema, BasicGenreSchema, BasicMovieSchema, CompleteMovieSchema
# ***********************************CODE*************************************
blp = Blueprint("movie_genre", __name__, description="All movie_genre functionalities", url_prefix="/api_movies")

@blp.route("/movie_genre/<string:movie_id>")
class Genres(MethodView):
    @blp.response(200, CompleteMovieSchema)
    def get(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)
        return movie

@blp.route("/movie_genre/<string:movie_id>/<string:genre_id>")
class MovieGenre(MethodView):
    @blp.response(200, CompleteGenreSchema)
    def post(self, movie_id, genre_id):
        movie = MovieModel.query.get_or_404(movie_id)
        genre = GenreModel.query.get_or_404(genre_id)

        movie.genres.append(genre)
        db.session.add(movie)
        db.session.commit()
        return genre

    @blp.response(200, CompleteGenreSchema)
    def delete(self, movie_id, genre_id):
        movie = MovieModel.query.get_or_404(movie_id)
        genre = GenreModel.query.get_or_404(genre_id)

        movie.genres.remove(genre)

        db.session.add(movie)
        db.session.commit()
        return genre





