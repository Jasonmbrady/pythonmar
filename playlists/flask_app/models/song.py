from flask_app.config.mysqlconnection import connectToMySQL

class Song:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.artist = data['artist']
        self.album = data['album']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']