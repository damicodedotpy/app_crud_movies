# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# ******************************OWN LIBRARIES*********************************
from extensions import db
from src.models import DirectorModel
from schemas import BasicDirectorSchema, UpdateDirectorSchema, CompleteDirectorSchema
# ***********************************CODE*************************************

blp = Blueprint("directors", __name__, description="All directors functionalities", url_prefix="/api_movies")

@blp.route("/directors")
class Director(MethodView):
    @blp.response(200, BasicDirectorSchema(many=True))
    def get(self):
        '''This endpoint returns all the
        directors information in the
        database.'''
        directors = DirectorModel.query.all()
        return directors

    @blp.arguments(BasicDirectorSchema)
    @blp.response(200, BasicDirectorSchema)
    def post(self, director_data):
        '''This endpoint creates a new
        director into the database.'''
        director = DirectorModel(**director_data)
        db.session.add(director)
        db.session.commit()
        return director


@blp.route("/director/<string:director_id>")
class DirectorID(MethodView):
    @blp.response(200, CompleteDirectorSchema)
    def get(self, director_id):
        '''This endpoint takes a director ID and
        returns a single director information
        from the database.'''
        director = DirectorModel.query.get_or_404(director_id)
        return director

    @blp.arguments(UpdateDirectorSchema)
    @blp.response(200, BasicDirectorSchema)
    def put(self, director_data, director_id):
        '''This endpoint updates a director's
        information into the database.'''
        director = DirectorModel.query.get_or_404(director_id)
        for key, value in director_data.items():
            setattr(director, key, value)
        db.session.commit()
        return director

    @blp.response(200, BasicDirectorSchema)
    def delete(self, director_id):
        '''This endpoint delete a director's
        information from the database.'''
        director = DirectorModel.query.get_or_404(director_id)
        db.session.delete(director)
        db.session.commit()
        return director


