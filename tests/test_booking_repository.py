from lib.booking_repository import BookingRepository



def test_booking_repository_init():
    instance = BookingRepository()
    assert isinstance(instance,BookingRepository)