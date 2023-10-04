import pytest
import requests


BASE_URL = 'https://jsonplaceholder.typicode.com'
TEST_USER_ID = 1


@pytest.fixture
def posts_url():
    return f'{BASE_URL}/posts'


@pytest.mark.parametrize('post_id', [1, 2, 3, 4, 5, -1])
def test_get_post_by_id(posts_url, post_id):
    response = requests.get(f'{posts_url}/{post_id}')
    assert response.status_code == 200
    assert response.json()['id'] == post_id
    assert response.text
    post_info = response.json()
    assert post_info['userId'] == TEST_USER_ID
    assert post_info['title']
    assert post_info['body']


@pytest.mark.parametrize('title, body', [
    pytest.param('Test title', 'Test body', id='valid'),
])
def test_create_post_by_post(posts_url, title, body):
    update_body = {
        'userId': TEST_USER_ID,
        'title': title,
        'body': body,
    }
    response = requests.post(posts_url, json=update_body)
    assert response.status_code == 201
    new_post_id = response.json()['id']

    # response = requests.get(f'{posts_url}/{new_post_id}')
    # assert response.status_code == 200
    actual_post_info = response.json()
    assert actual_post_info['id'] == new_post_id
    assert actual_post_info['userId'] == TEST_USER_ID
    assert actual_post_info['title'] == title
    assert actual_post_info['body'] == body


@pytest.mark.parametrize('post_id', [1])
def test_delete_post_by_id(posts_url, post_id):
    response = requests.delete(f'{posts_url}/{post_id}')
    assert response.status_code == 200
    assert response.text == '{}'
    # response = requests.get(f'{posts_url}/{post_id}')
    # assert response.status_code == 404
