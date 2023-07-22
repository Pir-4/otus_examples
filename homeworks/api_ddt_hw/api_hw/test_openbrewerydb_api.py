import pytest
import random

from .base_resuests import BaseRequest


@pytest.fixture(scope='session')
def openbrewerydb_request(openbrewerydb_url):
    return BaseRequest(openbrewerydb_url)


@pytest.mark.parametrize('per_page', [
    pytest.param(random.randint(1, 10), id='per_page')
])
def test_get_list_pages(openbrewerydb_request, per_page):
    response = openbrewerydb_request.get(params={"per_page": {per_page}})
    assert response.is_success
    assert len(response.body) == per_page, (
        f'Unexpected number {per_page} of breweries in list'
    )


@pytest.mark.parametrize('city', [
    'San Diego',
    "Jung-gu",
    "Goyang-si",
    "Worcester"
])
def test_filter_by_city(openbrewerydb_request, city):
    response = openbrewerydb_request.get(
        params={'by_city': city, "per_page": 5}
    )
    assert response.is_success
    body = response.body
    assert body
    for item in body:
        assert item['city'] == city, (
            f'Unexpected city {city} on item {item}'
        )


@pytest.mark.parametrize('state, expected', [
    ('new_york', 'New York'),
    ('minnesota', 'Minnesota'),
    ('texas', 'Texas')
])
def test_filter_by_state(openbrewerydb_request, state, expected):
    response = openbrewerydb_request.get(
        params={'by_state': state, "per_page": 5}
    )
    assert response.is_success
    body = response.body
    assert body
    for item in body:
        assert item['state'] == expected, (
            f'Unexpected state {expected} on item {item}'
        )


@pytest.mark.parametrize('size', [
    pytest.param(1, id='default'),
    pytest.param(50, id='max_valid_value')
])
def test_returned_number(openbrewerydb_request, size):
    response = openbrewerydb_request.get('random', params={'size': size})
    assert response.is_success
    assert len(response.body) == size


@pytest.mark.parametrize('query', [
    'brew'
])
def test_search(openbrewerydb_request, query):
    params = {'query': query}
    response = openbrewerydb_request.get('search', params=params)
    assert response.is_success
    for item in response.body:
        assert query in item['name'].lower(), (
            f'Unexpected search result {item} by query {query}'
        )
