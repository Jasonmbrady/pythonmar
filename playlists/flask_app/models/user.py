from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import playlist
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.playlists = []

    @staticmethod
    def validate_user(user_form):
        is_valid = True
        if len(user_form['first_name']) < 1:
            flash("First Name is required")
            is_valid = False
        if len(user_form['last_name']) < 1:
            flash("Last Name is required")
            is_valid = False
        if not EMAIL_REGEX.match(user_form['email']):
            flash("Invalid email address")
            is_valid = False
        if len(user_form['password']) < 8:
            flash("Passwords must be at least 8 characters")
            is_valid = False
        if user_form['password'] != user_form['confirm_pass']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL("playlist").query_db(query, data)

    @classmethod
    def get_one_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("playlist").query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return False
    
    @classmethod
    def get_one_with_playlists(cls, data):
        query = "SELECT * FROM users LEFT JOIN playlists ON playlists.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL("playlist").query_db(query, data)
        this_user = cls(results[0])
        if results[0]['playlists.id']:
            for row in results:
                p = {
                    "id": row['playlists.id'],
                    "name": row['name'],
                    "created_at": row['playlists.created_at'],
                    "updated_at": row['playlists.updated_at'],
                    "user_id": row['id']
                }
                this_user.playlists.append(playlist.Playlist(p))
        return this_user

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("playlist").query_db(query, data)
        return cls(results[0])
