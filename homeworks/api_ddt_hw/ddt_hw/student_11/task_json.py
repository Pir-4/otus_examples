import csv
import json
import os

project_directory = os.getcwd()
csv_file_path = 'data/books.csv'
json_file_path = 'data/users.json'
json_result = 'data/reference.json'

absolute_path_csv = os.path.join(project_directory, csv_file_path)
absolute_path_json = os.path.join(project_directory, json_file_path)
absolute_path_result_json = os.path.join(project_directory, json_result)

with open(absolute_path_csv, 'r', encoding='utf-8') as books_file:
    books_reader = csv.reader(books_file)
    books_data = list(books_reader)

with open(absolute_path_json, 'r', encoding='utf-8') as users_file:
    users_data = json.load(users_file)

books_per_user = (len(books_data) - 1) // len(users_data)
extra_books = (len(books_data) - 1) % len(users_data)

users = []

with open(absolute_path_csv, 'r', encoding='utf-8') as books_file:
    books_reader = csv.reader(books_file)
    next(books_reader)

    for i, user in enumerate(users_data):
        books = []
        count_books = books_per_user + (i < extra_books)

        for j in range(count_books):
            row = next(books_reader)
            book = {
                "title": row[0],
                "author": row[1],
                "pages": int(row[3]),
                "genre": row[2]
            }
            books.append(book)

        user_with_book = {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": books
        }

        users.append(user_with_book)
with open(absolute_path_result_json, 'w', encoding='utf-8') as result_file:
    json.dump(users, result_file, ensure_ascii=False, indent=4)