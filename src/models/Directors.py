# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************

# ******************************OWN LIBRARIES*********************************
from extensions import db
# ***********************************CODE*************************************
class DirectorModel(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(), unique=True, nullable=False)
    genre_id = db.Column(db.String(), db.ForeignKey("genres.id"), nullable=False)

    genres = db.relationship("GenreModel", back_populates="directors")
    movies = db.relationship("MovieModel", back_populates="directors", lazy="dynamic", cascade="all, delete")
