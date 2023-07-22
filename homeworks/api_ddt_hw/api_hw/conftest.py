import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru')
    parser.addoption('--status_code', default=200)


@pytest.fixture
def dog_url():
    return 'https://dog.ceo/api'


@pytest.fixture
def openbrewerydb_url_():
    return 'https://api.openbrewerydb.org/breweries'


@pytest.fixture
def jsonplaceholder_url():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status_code"))