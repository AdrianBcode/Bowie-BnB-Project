class Listing:
    def __init__(self, user_id: int, accommodation_id: int, is_booked: bool):
        self.user_id = user_id
        self.accommodation_id = accommodation_id
        self.is_booked = is_booked