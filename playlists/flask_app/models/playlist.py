from turtle import onscreenclick
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
class Playlist:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.created_by = user.User.get_one_by_id({"id": data['user_id']})

    @classmethod
    def create(cls, data):
        query = "INSERT INTO playlists (name, user_id) VALUES (%(name)s, %(user_id)s);"
        return connectToMySQL("playlist").query_db(query, data)
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM playlists WHERE id = %(id)s;"
        results = connectToMySQL("playlist").query_db(query, data)
        return cls(results[0])