# Model class
class Accommodation:
    def __init__(self, id, place_name, host_id, img_path, description, price):
        self.id = id
        self.place_name = place_name
        self.host_id = host_id
        self.img_path = img_path
        self.description = description
        self.price = price
        
        
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Accommodation({self.id}, {self.host_id}, {self.place_name}, {self.img_path}, {self.description}, {self.price})"