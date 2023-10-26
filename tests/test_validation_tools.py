import pytest
from lib.validation_tools import ValidationTools



def test_init_validation_tools():
    instance = ValidationTools()
    assert isinstance(instance,ValidationTools)

def test_password_validator_truthy_result():
    instance = ValidationTools()
    assert instance.password_validator('Test1234!','!@£', 8) == True

def test_password_validator_false_result():
    instance = ValidationTools()
    assert instance.password_validator('Test1234','!@£', 8) == False