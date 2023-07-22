import pytest
import random
from jsonschema import validate

from .base_resuests import BaseRequest

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"},
    },
    "required": ["id", "title", "body", "userId"]
}


@pytest.fixture(scope='session')
def jsonplaceholder_request(jsonplaceholder_url):
    return BaseRequest(jsonplaceholder_url)


@pytest.mark.parametrize('id, expected_id', [
    (10000, 10000),
    (-1, -1,),
    (0, 0)
])
@pytest.mark.parametrize('title, expected_title', [
    ('title', 'title'),
    ('', ''),
    (100, 100),
    ('&', '&')
])
def test_creating_resource(
        jsonplaceholder_request, id, expected_id, title, expected_title
):
    body = {'title': title, 'body': 'creating resourse', 'userId': id}
    response = jsonplaceholder_request.post('posts', body=body)
    assert response.is_success
    assert response.body['body'] == 'creating resourse'
    assert response.body['title'] == expected_title
    assert response.body['userId'] == expected_id


@pytest.mark.parametrize('user_id', [
    pytest.param(random.randint(1, 20), id='random_user_id')
])
@pytest.mark.parametrize('body, expected_body', [
    pytest.param('updated body', 'updated body', id='latin'),
    pytest.param('тело изменено', 'тело изменено', id='cyrillic'),
    pytest.param(100, 100, id='number_int')
])
def test_updating_body(jsonplaceholder_request, user_id, body, expected_body):
    body = {'body': body, 'userId': user_id}
    response = jsonplaceholder_request.put('posts/1', body=body)
    assert response.is_success
    assert response.body['body'] == expected_body
    assert response.body['userId'] == user_id


@pytest.mark.parametrize('user_id', [
    pytest.param(random.randint(1, 20), id='random_user_id')
])
def test_json_schema(jsonplaceholder_request, user_id):
    response = jsonplaceholder_request.get('posts')
    assert response.is_success
    user_body = response.body[user_id]
    validate(instance=user_body, schema=USER_SCHEMA)


@pytest.mark.parametrize('userId', [
    pytest.param(-1, id="negative"),
    pytest.param(0, id='zero'),
    pytest.param('a', id='letter'),
    pytest.param(11, id='out_of_range'),
])
def test_api_empty_response(jsonplaceholder_request, userId):
    response = jsonplaceholder_request.get('posts', params={'userId': userId})
    assert response.is_success
    assert not response.body
