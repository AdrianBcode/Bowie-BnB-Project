from lib.listings_repository import ListingsRepository



def test_listings_repository_init():
    instance = ListingsRepository()
    assert isinstance(instance,ListingsRepository)