from lib.accommodation import *
from lib.accommodation_repository import *

'''
When I call #all I get all
properties in the accommodations table
'''

def test_all(db_connection):
    db_connection.seed("seeds/bowie_bnb_seed.sql")
    repository = AccommodationRepository(db_connection)
    assert repository.all() == [
        Accommodation(1, "Goldeneye", "20/12/23", "27/12/23", 7)
    ]
