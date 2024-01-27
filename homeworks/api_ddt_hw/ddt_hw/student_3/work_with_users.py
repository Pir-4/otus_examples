import json

from files import JSON_FILE_PATH


def open_users_file():
    with open(JSON_FILE_PATH, 'r') as users_json_file:
        users = json.load(users_json_file)
        result_key = ['name', 'gender', 'address', 'age']
        users_with_req_keys = []

        for user in users:
            user_data = {key: value for key, value in user.items() if key in result_key}
            user_data.update({'books': []})
            users_with_req_keys.append(user_data)

    return users_with_req_keys