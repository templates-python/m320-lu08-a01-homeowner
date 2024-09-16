import pytest

from house import House


@pytest.fixture
def house():
    return House('Stadthaus')

def test_house(house):
    assert house.type == 'Stadthaus'
