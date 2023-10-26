# Model class
class Accommodation:
    def __init__(self, id, place_name, host_id, img_path, description, price):
        self.id = id
        self.place_name = place_name
        self.description = description
        self.price = price
        self.host_id = host_id
        self.img_path = img_path
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.place_name}, {self.description}, {self.price}, {self.host_id}, {self.img_path})"