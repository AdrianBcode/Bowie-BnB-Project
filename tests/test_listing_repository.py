from lib.listings_repository import ListingsRepository



def test_listings_repository_init():
    instance = ListingsRepository()
    assert isinstance(instance,ListingsRepository)


def test_listing_adds_new_listing(db_connection):
    db_connection.seed("seeds/bowie_bnb_seed.sql")
    repository = ListingsRepository(db_connection)
    listing = listing(None, 2, 3, True, '10/10/2023','10/11/2023')
    result = repository.create_listing(listing)
    assert result == [
        listing(1, 1, 1, True,'10/10/2023','10/11/2023'),
        listing(2, 2, 3, True, '10/10/2023','10/11/2023')]
