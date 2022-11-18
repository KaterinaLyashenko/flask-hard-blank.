from flask_restx import Resource, Namespace

from container import genre_dao
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_dao.get_all()
        return genre_schemas.dump(all_genres), 200

@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_dao.get_one(gid)
        return genre_schema.dump(genre), 200
