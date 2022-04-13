from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(userdata):
        is_valid = True
        # run tests
        if len(userdata['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        if userdata['password'] != userdata['confirm_pass']:
            flash("passwords do not match")
            is_valid = False
        if len(userdata['f_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(userdata['email']):
            flash("Please enter a valid email address")
            is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (f_name, l_name, email, password, created_at, updated_at) VALUES ( %(f_name)s,%(l_name)s,%(email)s,%(password)s, NOW(), NOW());"
        results = connectToMySQL("log_reg").query_db(query, data)
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("log_reg").query_db(query, data)
        return cls(results[0])
