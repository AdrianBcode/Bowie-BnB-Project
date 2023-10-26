from lib.accommodation import * 

'''
When I construct an Accommodation with
with id, place_name, start_date, end_date,
and host_id they are reflected in the instance properties
'''

def test_accommodation_constructs():
    accommodation = Accommodation(1, "Goldeneye", 7, " ", "Perfect for super villians!", "£2000 per night")
    assert accommodation.id == 1
    assert accommodation.place_name == "Goldeneye"
    assert accommodation.host_id == 7
    assert accommodation.img_path == " "
    assert accommodation.description == "Perfect for super villians!"
    assert accommodation.price == "£2000 per night"
    