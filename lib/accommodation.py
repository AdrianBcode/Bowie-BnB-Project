# Model class
class Accommodation:
    def __init__(self, id, place_name, start_date, end_date, host_id):
        self.id = id
        self.place_name = place_name
        self.start_date = start_date
        self.end_date = end_date
        self.host_id = host_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.place_name}, {self.start_date}, {self.end_date}, {self.host_id})"