from lib.listing import Listing
from lib.accommodation import Accommodation
import pandas

class ListingsRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_unbooked_unrequested_listings(self, start_date,end_date):
        rows = self.connection.execute(f"""SELECT
	*
FROM
	accommodations
	JOIN listings ON listings.accommodation_id = accommodations.id
	JOIN users ON accommodations.host_id = users.id
WHERE (listings.user_id IS NULL
	AND listings.is_booked = FALSE AND start_date >= '{start_date}' AND end_date <= '{end_date}' )
    """)
        return [
            Accommodation(row['accommodation_id'],row['place_name'],row['host_id'],row['img_path'],row['description'],row['price']) for row in rows
        ]
    
    def find_unbooked_requested_listings(self):
        rows = self.connection.execute("""SELECT
	*
FROM
	accommodations
	JOIN listings ON listings.accommodation_id = accommodations.id
	JOIN users ON accommodations.host_id = users.id
WHERE (listings.user_id IS NOT NULL
	AND listings.is_booked = FALSE)
    """)
        return [
            Accommodation(row['accommodation_id'],row['place_name'],row['host_id'],row['img_path'],row['description'],row['price']) for row in rows
        ]
    
    def find_booked_listings(self):
        rows = self.connection.execute("""SELECT
	*
FROM
	accommodations
	JOIN listings ON listings.accommodation_id = accommodations.id
	JOIN users ON accommodations.host_id = users.id
WHERE (listings.user_id IS NOT NULL
	AND listings.is_booked = TRUE)
    """)
        return [
            Accommodation(row['accommodation_id'],row['place_name'],row['host_id'],row['img_path'],row['description'],row['price']) for row in rows
        ]

    def create_listing(self,user_id,place_name,start_date,end_date,img_path,description,price):
        self.connection.execute(
            "INSERT INTO listings (user_id, accomodation_id, is_booked, start_date, end_date) VALUES (%s, %s, %s, %s, %s)",
            [listing.user_id, listing.accomodation_id, listing.is_booked, listing.start_date,listing.end_date])
        

    def update_listing(self):
        pass

    def delete_listing(self):
        pass

    def find_dates_blocked(self, accomodation):
        rows = self.connection.execute(
            "SELECT * FROM listings WHERE accommodation_id = %s AND is_booked = %s", [accomodation, True])
        data = [Listing(row['user_id'],row['accommodation_id'],row['start_date'],row['end_date'],row['is_booked']) for row in rows]
        dates_list = []
        for  d in data:
            print(d.start_date)
            print(d.end_date)
            print(d.is_booked)

            dates = pandas.date_range(d.start_date,d.end_date).strftime("%Y-%m-%d").tolist()
            disable_dates = dates_list + dates    
        return disable_dates