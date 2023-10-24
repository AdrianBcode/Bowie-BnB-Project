from lib.user import *

'''
When I construct a User with
id, name, email, and password
they are reflected in the instance properties
'''

def test_user_contructs():
    user = User(1, "Angie", "Angie@example.com", "changes")
    assert user.id == 1
    assert user.name == "Angie"
    assert user.email == "Angie@example.com"
    assert user.password == "changes"

