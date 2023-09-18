from pytest import fixture


@fixture
def config():
    def setup_env():
        global PORT
        PORT = 8080

    return setup_env
