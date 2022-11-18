from flask_restx import Resource, Namespace

from container import director_dao
from dao.model.director import DirectorSchema

director_ns = Namespace('director')
director_schema = DirectorSchema()
director_schemas = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_dao.get_all()
        return director_schemas.dump(all_directors), 200

@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did):
        director = director_dao.det_one(did)
        return director_schema.dump(director), 200