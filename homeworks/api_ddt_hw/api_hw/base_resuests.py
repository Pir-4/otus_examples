import requests
import pprint


class BaseResponse:
    def __init__(self, request):
        self._request = request
        self.status_code = request.status_code

    @property
    def is_success(self):
        return self._request.ok

    @property
    def body(self):
        return self._request.json()


class BaseRequest:
    def __init__(self, base_url, response_type=BaseResponse):
        self.base_url = base_url
        self._response_type = response_type

    def _request(self, url, request_type, data=None):
        if request_type == 'GET':
            response = requests.get(url)
        elif request_type == 'POST':
            response = requests.post(url, data=data)
        else:
            response = requests.delete(url)

        # log part
        pprint.pprint(f'{request_type} example')
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        pprint.pprint(response.json())
        pprint.pprint('**********')
        return response

    def get(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = self._request(url, 'GET')
        return self._response_type(response)

    # def post(self, endpoint, endpoint_id, body):
    #     url = f'{self.base_url}/{endpoint}/{endpoint_id}'
    #     response = self._request(url, 'POST', data=body)
    #     return response.json()['message']
    #
    # def delete(self, endpoint, endpoint_id):
    #     url = f'{self.base_url}/{endpoint}/{endpoint_id}'
    #     response = self._request(url, 'DELETE')
    #     return response.json()['message']
