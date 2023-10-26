from lib.user import *

# Repository class

class UserRepository:
    def __init__(self,connection):
        self.connection = connection

    def create(self, username,email,password):
        self.connection.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            [username,email,password]
        )

    def all(self):
        rows = self.connection.execute("SELECT * FROM users;")
        return [
            User(row['id'], row['name'], row['email'], row['password']) for row in rows
        ]
    
    def find(self, email):
        rows = self.connection.execute(
            "SELECT * from users WHERE email = %s",[email])
        row = rows[0]
        return User(row['id'], row['name'], row['email'], row['password'])