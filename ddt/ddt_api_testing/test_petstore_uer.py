import pytest

from .pets_tore_api_user import PetStoreApiUser


@pytest.fixture(scope='function')
def pet_store_api_user():
    return PetStoreApiUser()


def test_create_user(pet_store_api_user):
    data = {
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    user_id = pet_store_api_user.create_user(**data)
    assert user_id

    expected_body = {
        'id': user_id,
        **data
    }
    user_info = pet_store_api_user.get('user', data['username'])
    for key, value in expected_body.items():
        assert user_info[key] == value, (
            f'[{key}] Actual value: {user_info[key]}, expected: {value}'
        )


def test_create_user_list(pet_store_api_user):
    data = [
        {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
    ]
    response = pet_store_api_user.create_with_list(data)
    assert response == 'ok'

