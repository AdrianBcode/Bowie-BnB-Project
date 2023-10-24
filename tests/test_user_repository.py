'''
When I call #all I get all users
in users table
'''

def test_all(db_connection):
    db_connection.seed("seeds/bowie_bnb_seed.sql")
    repository = UserRepository(db_connection)
    assert 