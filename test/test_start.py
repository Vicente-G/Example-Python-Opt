from os import path

from pytest import fixture
from werkzeug.datastructures import FileStorage

from src.start import main


@fixture
def result():
    test_folder = "/".join(__file__.split("/")[:-1])
    filename = path.join(test_folder, "data/test.dat")
    with open(filename) as file:
        content = file.read()
        data = FileStorage(stream=file)
        data.read = lambda: bytes(content, "utf-8")
    return main(data)


def test_solve_success(result):
    assert "status" in result
    assert str(result["status"]) == "ok"


def test_objective_value(result):
    assert "result" in result
    assert "objective" in result["result"]
    assert result["result"]["objective"] == 2 / 3


def test_result_values(result):
    assert "x[1]" in result["result"]
    assert result["result"]["x[1]"] == 1 / 3
    assert "x[2]" in result["result"]
    assert result["result"]["x[2]"] == 0.0
