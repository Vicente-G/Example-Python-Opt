from pytest import fixture

from src.example import main


@fixture
def data():
    return main()


def test_property(data):
    assert "hello" in data


def test_property_value(data):
    assert data["hello"] == "world"
