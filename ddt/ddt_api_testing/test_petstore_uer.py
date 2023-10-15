import pytest

from api_testing.base_request import BaseRequest

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'


@pytest.fixture(scope='function')
def base_request():
    return BaseRequest(BASE_URL_PETSTORE)


def test_create_user(base_request):
    data = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    response = base_request.post('user', '', data)
    assert response['message'] == str(data['id'])
