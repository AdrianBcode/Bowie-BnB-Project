from lib.accommodation import * 

'''
When I construct an Accommodation with
with id, place_name, start_date, end_date,
and host_id they are reflected in the instance properties
'''

def test_accommodation_constructs():
    accommodation = Accommodation(1, "Goldeneye", "20/12/23", "27/12/23", 7)
    assert accommodation.id == 1
    assert accommodation.place_name == "Goldeneye"
    assert accommodation.start_date == "20/12/23"
    assert accommodation.end_date == "27/12/23"
    assert accommodation.host_id == 7