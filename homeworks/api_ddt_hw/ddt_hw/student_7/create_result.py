import os
import csv
import json


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def distribute_books(books_data, users_data):
    books_copy = books_data.copy()
    total_books = len(books_copy)
    total_users = len(users_data)
    books_per_user, remaining_books = divmod(total_books, total_users)
    result_data = []

    for user in users_data:
        user_books = []

        for _ in range(books_per_user):
            user_books.append(books_copy.pop(0))

        if remaining_books > 0:
            user_books.append(books_copy.pop(0))
            remaining_books -= 1

        user_info = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": user_books
        }

        result_data.append(user_info)

    return result_data


if __name__ == "__main__":
    books_file = get_path('books.csv')
    reference_file = get_path('reference.json')
    users_file = get_path('users.json')

    books_data = read_csv(books_file)
    reference_data = read_json(reference_file)
    users_data = read_json(users_file)

    result_data = distribute_books(books_data, users_data)

    with open('result.json', 'w') as result_file:
        json.dump(result_data, result_file, indent=2)