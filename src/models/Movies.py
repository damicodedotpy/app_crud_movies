# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************

# ******************************OWN LIBRARIES*********************************
from extensions import db
# ***********************************CODE*************************************

class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(), unique=True, nullable=False)
    director_id = db.Column(db.String(), db.ForeignKey("directors.id"), nullable=False)
    year = db.Column(db.Integer())
    oscar_winner = db.Column(db.Boolean())

    directors = db.relationship("DirectorModel", back_populates="movies")
    genres = db.relationship("GenreModel", back_populates="movies", secondary="movie_genre")

