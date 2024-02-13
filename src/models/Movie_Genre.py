# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************

# ******************************OWN LIBRARIES*********************************
from extensions import db
# ***********************************CODE*************************************
class MovieGenreModel(db.Model):
    __tablename__ = "movie_genre"

    id = db.Column(db.Integer(), primary_key=True)
    movie_id = db.Column(db.Integer(), db.ForeignKey("movies.id"))
    genre_id = db.Column(db.Integer(), db.ForeignKey("genres.id"))