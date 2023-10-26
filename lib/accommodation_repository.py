from lib.accommodation import *

class AccommodationRepository:
    def __init__(self, connection):
        self.connection = connection

    
    def all(self):
        rows = self.connection.execute("SELECT * FROM accommodations;")
        return [
            Accommodation(row['id'],row['place_name'],row['description'],row['price'],row['host_id'],row['img_path']) for row in rows
        ]
    
    def create(self, accommodation):
        self.connection.execute(
            "INSERT INTO accommodations (place_name, host_id, img_path, description, price) VALUES (%s, %s, %s, %s)",
            [accommodation.place_name, accommodation.host_id, accommodation.img_path, accommodation.description,accommodation.price]
        )
    
    def find(self, place_name):
        rows = self.connection.execute(
            "SELECT * from accommodations WHERE place_name = %s",[place_name])
        row = rows[0]
        return Accommodation(row['id'],row['place_name'],row['description'],row['price'],row['host_id'],row['img_path'])