from api_testing.base_request import BaseRequest, BASE_URL_PETSTORE


class PetStoreApiUser(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_PETSTORE)

    def create_user(
            self, username, firstName, lastName, email,
            password, phone, userStatus
    ):
        data = {
            "id": 0,
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": userStatus
        }
        return self.post('user', '', data, is_json=True)

    def get_user(self, user_name):
        return self.get('user', user_name)

    def delete_user(self, user_name):
        return self.delete('user', user_name)

    def create_with_list(self, list_of_users):
        return self.post(
            'user', 'createWithList', list_of_users, is_json=True
        )
