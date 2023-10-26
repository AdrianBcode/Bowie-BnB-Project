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
        Accommodation(1,'The Glass Jewel', 1, 'img_1.jpg','Nestled atop the hills of Beverly Hills, California.','£2000 Per Night'),
        Accommodation(2, 'The Floating Oasis', 2, 'img_2.jpg','Beautiful floating mansion with a retractable roof, Maldives.','£4000 Per Night'),
        Accommodation(3, 'The Treehouse Retreat', 3, 'img_3.jpg','Hidden in the lush rainforests of Costa Rica.','£1800 Per Night'),
        Accommodation(4, 'The Ice Palace', 4, 'img_4.jpg','An opulent space with a roaring fireplace in Aspen.', '£2480 Per Night'),
        Accommodation(5, 'The Sky Cathedral', 5, 'img_5.jpg','Atop a towering skyscraper in the heart of Dubai. ','£1800 Per Night'),
        Accommodation(6, 'The Floating Chateau', 6, 'img_6.jpg','Afloat on Lake Geneva, Switzerland.','£5500 Per Night'),
        Accommodation(7, 'The Cave Dwelling', 7, 'img_7.jpg','Carved into the cliffs of Santorini, Greece','£6000 Per Night'),
        Accommodation(8, 'The Timeless Castle', 8, 'img_8.jpg','Amid the rolling vineyards of Tuscany, Italy.','£2200 Per Night'),
        Accommodation(9, 'The Opulent Aerie', 9, 'img_9.jpg','Perched atop a gleaming skyscraper in the heart of New York City.','£2200 Per Night'),
        Accommodation(10, 'The Bash Mansion', 10, 'img_10.jpg','Situated in the heart of the lively Soho, London.','£2200 Per Night')
    ]
