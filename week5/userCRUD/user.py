from mysqlconnection import connectToMySQL

class User:
    db = "usersCRUD"
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (f_name, l_name, email) VALUES ( %(f_name)s, %(l_name)s, %(email)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results