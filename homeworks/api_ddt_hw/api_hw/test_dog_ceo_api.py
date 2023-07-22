import pytest
from .base_resuests import BaseRequest, BaseResponse


class DogResponse(BaseResponse):
    @property
    def is_success(self):
        return super().is_success and self.body.get('status') == 'success'

    @property
    def result(self):
        return self.body.get('message')


@pytest.fixture(scope='session')
def dog_requests(dog_url):
    return BaseRequest(dog_url, response_type=DogResponse)


def test_get_breeds_list(dog_requests):
    dog_response = dog_requests.get('breeds/list/all')
    assert dog_response.is_success


@pytest.mark.parametrize('breed', [
    'sharpei',
    'saluki',
    'redbone',
])
def test_get_breed_random_image(dog_requests, breed):
    dog_response = dog_requests.get(f'breed/{breed}/images/random')
    assert dog_response.is_success
    image_name = dog_response.result
    assert breed in image_name, f'Unexpected breed {breed} in random image'


def test_images_extension(dog_requests):
    dog_response = dog_requests.get('breed/hound/afghan/images')
    assert dog_response.is_success
    images = dog_response.result
    for image in images:
        assert str(image).endswith('.jpg'), (
            f'Unexpected image extension "{image}", expected only .jpg'
        )


@pytest.mark.parametrize('count', [
    pytest.param(0, id="zero"),
    pytest.param(1, id='min_valid_value'),
    pytest.param(50, id='max_valid_value'),
])
def test_amount_images_all_dogs(dog_requests, count):
    dog_response = dog_requests.get(f'breeds/image/random/{count}')
    assert dog_response.is_success
    assert len(dog_response.result) == count


@pytest.mark.parametrize('input_amount, expected_amount', [
    pytest.param(51, 50, id="out_of_range"),
    pytest.param(1.5, 1, id='float'),
    pytest.param('a', 1, id='letter'),
])
def test_error_amount_returned_images_all_dogs(
        dog_requests, input_amount, expected_amount):
    dog_response = dog_requests.get(
        f'breeds/image/random/{input_amount}'
    )
    assert dog_response.is_success
    assert len(dog_response.result) == expected_amount
