import os
import json
import csv
from copy import deepcopy


USERS_FILE_NAME = 'users.json'
BOOKS_FILE_NAME = 'books.csv'
RESULT_FILE_NAME = 'result.json'


def get_full_file_path(path_ending):
    base_path = os.getcwd()
    full_file_path = os.path.join(base_path, path_ending)
    return full_file_path


def read_json_file(path_ending):
    full_file_path = get_full_file_path(path_ending)
    with open(full_file_path, "r") as json_file:
        json_result = json.load(json_file)
    return json_result


def write_json_file(path_ending, json_data, indent=4):
    full_file_path = get_full_file_path(path_ending)
    with open(full_file_path, "w") as json_file:
        json_object = json.dumps(json_data, indent=indent)
        json_file.write(json_object)


def read_csv_file(path_ending):
    full_file_path = get_full_file_path(path_ending)
    csv_result = []
    with open(full_file_path, "r") as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            csv_result.append(row)
    return csv_result


def filter_fields_of_list_of_dict(list_of_dict, save_fields):
    result = []
    for dict_item in list_of_dict:
        new_book = {
            key.lower(): value for key, value in dict_item.items()
            if key in save_fields
        }
        result.append(new_book)
    return result


def convert_fields_to_int(list_of_dict, list_of_fields):
    result = []
    for dict_item in list_of_dict:
        tmp_item = {
            key: int(value) if key in list_of_fields else value
            for key, value in dict_item.items()
        }
        result.append(tmp_item)
    return result


def add_books_to_users(books, users):
    result_users = deepcopy(users)
    list_size = len(users)
    for index, book in enumerate(books):
        list_index = index % list_size
        user = result_users[list_index]
        if not user.get('books'):
            user['books'] = []
        user['books'].append(book)
    return result_users


if __name__ == '__main__':
    users = read_json_file(USERS_FILE_NAME)
    books = read_csv_file(BOOKS_FILE_NAME)

    new_users = filter_fields_of_list_of_dict(
        users, ['name', 'gender', 'address', 'age']
    )
    new_books = filter_fields_of_list_of_dict(
        books, ['Title', 'Author', 'Pages', 'Genre']
    )

    new_books = convert_fields_to_int(new_books, ['pages'])

    final_users = add_books_to_users(new_books, new_users)

    write_json_file(RESULT_FILE_NAME, final_users)
    pass