import pytest

from home_owner import HomeOwner
from house import House


@pytest.fixture
def house():
    return House('Landhaus')


@pytest.fixture
def owner(house):
    return HomeOwner('Ron', house)


def test_owner(owner):
    assert owner.name == 'Ron'


def test_print(owner, capsys):
    print(owner)
    captured = capsys.readouterr()
    assert captured.out == 'Ron besitzt ein Landhaus\n'
