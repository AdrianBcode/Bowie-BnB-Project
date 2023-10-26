from lib.user import *
from lib.user_repository import *

'''
When I call #all I get
all users in users table
'''

def test_all(db_connection):
    db_connection.seed("seeds/bowie_bnb_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, "Angie", "Angie@example.com", "changes"),
        User(2,'Magie', 'magie56@example.com', 'september1'),
        User(3, 'Carol', 'ccarol.12@example.com', 'christmas'),
        User(4, 'Severus', 'severus.09@example.com', 'snape123'),
        User(5, 'Thomas', 'tom123@example.com', 'cooawl'),
        User(6, 'Joe', 'howyoudoing@example.com', 'friends'),
        User(7, 'Freddie', 'queens6@example.com', 'ilovemusic'),
        User(8, 'David', 'davi.d@example.com', 'password'),
        User(9, 'Karen', 'karen.mc0@example.com', 'mchammer'),
        User(10, 'Zack', 'zack.finley@example.com', 'traveller'),
        User(11, 'Monica', 'monica123@example.com', 'beverly321')
    ]

def test_create_user(db_connection):
    db_connection.seed("seeds/bowie_bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.create('George','george@none.none','12345678!')
    assert User(12,'George','george@none.none','12345678!') in repository.all()