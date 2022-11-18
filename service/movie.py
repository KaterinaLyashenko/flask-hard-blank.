from dao.movie import MovieDAO

class MovieService():
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.id = data.get("id")

        self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)
