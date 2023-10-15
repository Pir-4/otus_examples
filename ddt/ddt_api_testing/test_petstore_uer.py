import pytest

from .pets_tore_api_user import PetStoreApiUser


@pytest.fixture(scope='function')
def base_request():
    return PetStoreApiUser()


def test_create_user(base_request):
    data = {
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    user_id = base_request.create_user(**data)
    assert user_id

    expected_body = {
        'id': user_id,
        **data
    }
    user_info = base_request.get('user', data['username'])
    for key, value in expected_body.items():
        assert user_info[key] == value, (
            f'[{key}] Actual value: {user_info[key]}, expected: {value}'
        )

