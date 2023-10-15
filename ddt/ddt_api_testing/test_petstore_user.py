import pytest
import os

from .pets_tore_api_user import PetStoreApiUser
from .gen_params import (
    gen_users, get_list_of_users, get_list_of_users_from_csv_file,
    get_param_list_error_users
)


USERS_FILE_NAME = os.getenv('USERS_FILE_NAME', 'users.csv')
USERS_ERROR_FILE_NAME = os.getenv('USERS_ERROR_FILE_NAME', 'users_error.csv')


@pytest.fixture(scope='function')
def pet_store_api_user():
    return PetStoreApiUser()


@pytest.mark.parametrize('data', gen_users(2))
def test_create_user(pet_store_api_user, data):
    user_id = pet_store_api_user.create_user(**data)
    assert user_id

    expected_body = {
        **data,
        'id': user_id,
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
    pytest.param(
        get_list_of_users_from_csv_file(USERS_FILE_NAME, 5),
        id='5 users from csv file'
    ),
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


@pytest.mark.parametrize('user_data, error_message',
        get_param_list_error_users(USERS_ERROR_FILE_NAME, 3),
)
def test_create_error_user(pet_store_api_user, user_data, error_message):
    err_msg = pet_store_api_user.create_user(**user_data, expected_error=True)
    assert err_msg == error_message
