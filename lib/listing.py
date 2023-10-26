class Listing:
    def __init__(self, user_id: int, accommodation_id: int,start_date: str, end_date: str, is_booked: bool,):
        self.user_id = user_id
        self.accommodation_id = accommodation_id
        self.start_date = start_date
        self.end_date = end_date
        self.is_booked = is_booked