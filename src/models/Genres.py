# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************

# ******************************OWN LIBRARIES*********************************
from extensions import db
# ***********************************CODE*************************************
class GenreModel(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(), unique=True, nullable=False)
    classification = db.Column(db.String())

    movies = db.relationship("MovieModel", back_populates="genres", secondary="movie_genre")
    directors = db.relationship("DirectorModel", back_populates="genres", lazy="dynamic")
