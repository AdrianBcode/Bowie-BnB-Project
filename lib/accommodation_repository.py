from lib.accommodation import *

class AccommodationRepository:
    def __init__(self, connection):
        self.connection = connection

    
    def all(self):
        rows = self.connection.execute("SELECT * FROM accommodations;")
        return [
            Accommodation(row['id'], row['place_name'], row['start_date'], row['end_date'], row['host_id']) for row in rows
        ]
    
    def create(self, accommodation):
        self.connection.execute(
            "INSERT INTO accommodations (place_name, start_date, end_date, host_id) VALUES (%s, %s, %s, %s)",
            [accommodation.place_name, accommodation.start_date, accommodation.end_date, accommodation.host_id]
        )