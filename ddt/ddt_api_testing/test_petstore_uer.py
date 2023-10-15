import pytest

from .pets_tore_api_user import PetStoreApiUser
from .gen_params import get_list_of_users


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


@pytest.mark.parametrize('list_of_users', [
    pytest.param(get_list_of_users(size=5), id='5 users'),
])
def test_create_user_list(pet_store_api_user, list_of_users):
    response = pet_store_api_user.create_with_list(list_of_users)
    assert response == 'ok'
    for user_info in list_of_users:
        user_name = user_info['username']
        user_info.pop('id')
        user_info = pet_store_api_user.get('user', user_name)
        for key, value in user_info.items():
            assert user_info[key] == value, (
                f'[{key}] Actual value: {user_info[key]}, expected: {value}'
            )


@pytest.mark.parametrize('list_of_users', [
    pytest.param(get_list_of_users_from_file(), id='5 users'),
])
def test_create_user_array(pet_store_api_user, list_of_users):
    response = pet_store_api_user.create_with_list(list_of_users)
    assert response == 'ok'
    for user_info in list_of_users:
        user_name = user_info['username']
        user_info.pop('id')
        user_info = pet_store_api_user.get('user', user_name)
        for key, value in user_info.items():
            assert user_info[key] == value, (
                f'[{key}] Actual value: {user_info[key]}, expected: {value}'
            )

