# ******************************PYTHON LIBRARIES******************************
import os
# ******************************EXTERNAL LIBRARIES****************************
from flask import Flask
# ******************************OWN LIBRARIES*********************************
import src.models
from extensions import db, migrate
from config import AppConfiguration
from src.routes.movies import blp as MoviesBlueprint
from src.routes.directors import blp as DirectorsBlueprint
from src.routes.genres import blp as GenresBlueprint
from src.routes.movie_genre import blp as MovieGenreBlueprint
# ***********************************CODE*************************************
def create_app():

    #FLASK INSTANCE
    app = Flask(__name__)

    #FLASK CONFIGURATION
    app.config.from_object(AppConfiguration)

    #EXTENSIONS INITIALIZATION
    db.init_app(app)
    migrate.init_app(app, db)

    #DATABASE CREATION
    with app.app_context():
        db.create_all()

    #ENDPOINTS
    app.register_blueprint(MoviesBlueprint)
    app.register_blueprint(DirectorsBlueprint)
    app.register_blueprint(GenresBlueprint)
    app.register_blueprint(MovieGenreBlueprint)

    return app