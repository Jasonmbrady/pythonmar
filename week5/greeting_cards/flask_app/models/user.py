from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.card import Card

class User:
    db = "greeting_cards"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cards = []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (name, email) VALUES (%(name)s, %(email)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_one_with_cards(cls, data):
        query = "SELECT * FROM users LEFT JOIN cards ON users.id = cards.users_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        this_user = cls(results[0])
        for row in results:
            card = {
                "id": row['cards.id'],
                "name": row['cards.name'],
                "email": row['cards.email'],
                "text": row['text'],
                "created_at": row['cards.created_at'],
                "updated_at": row['cards.updated_at'],
            }
            this_user.cards.append(Card(card))
        return this_user