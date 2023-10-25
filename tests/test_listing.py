from lib.listing import Listing



def test_listing_init():
    instance = Listing(1,1,True)
    assert instance.is_booked == True
