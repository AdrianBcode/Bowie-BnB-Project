from lib.listing import Listing

class ListingsRepository:
    def __init__(self):
        pass

    def find_unbooked_unrequested_listings(self):
        rows = self.connection.execute("""SELECT
	*
FROM
	accommodations
	JOIN listings ON listings.accommodation_id = accommodations.id
	JOIN users ON accommodations.host_id = users.id
WHERE (listings.user_id IS NULL
	AND listings.is_booked = FALSE)
    """)
        return [
            Listing(row['id'],row['accommodation_id'],) for row in rows
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
            Listing(row['id'],row['accommodation_id'],) for row in rows
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
            Listing(row['id'],row['accommodation_id'],) for row in rows
        ]

    def create_listing(self):
        pass

    def update_listing(self):
        pass

    def delete_listing(self):
        pass