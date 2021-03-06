from flask_app.config.mysqlconnection import connectToMySQL

class Card:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']