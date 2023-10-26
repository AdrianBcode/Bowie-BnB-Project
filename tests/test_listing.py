from lib.listing import Listing



def test_listing_init():
    instance = Listing(1,1,'01/01/2023','01/01/2024',True)
    assert instance.is_booked == True
