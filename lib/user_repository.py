from lib.user import *

# Repository class

class UserRepository:
    def __init__(self,connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM users;")
        return [
            User(row['id'], row['name'], row['email'], row['password']) for row in rows
        ]
        # print()
        # print(f'!!!!!!!!!!!!{rows}')
        # return False #[User(1, "Angie", "Angie@example.com", "changes")]