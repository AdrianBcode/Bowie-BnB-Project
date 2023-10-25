from lib.booking import Booking



def test_booking_init():
    instance = Booking(1,1,True)
    assert instance.is_booked == True
