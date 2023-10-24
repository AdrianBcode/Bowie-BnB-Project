import pytest
from lib.validation_tools import ValidationTools



def test_init_validation_tools():
    instance = ValidationTools('value')
    assert instance.value == 'value'