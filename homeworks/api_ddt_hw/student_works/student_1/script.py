from __init__ import USERS_JSON_PATH, BOOKS_CSV_PATH
import json
from csv import DictReader

with open(USERS_JSON_PATH, "r") as f_users:
    new_users = []
    for user in json.load(f_users):
        new_users.append(
            {
                "name": user.get("name"),
                "gender": user.get("gender"),
                "address": user.get("address"),
                "age": user.get("age"),
                "books": []
            }
        )

with open(BOOKS_CSV_PATH, "r") as f_books:
    new_book = []
    for book in list(DictReader(f_books)):
        new_book.append({
            "title": book.get("Title"),
            "author": book.get("Author"),
            "pages": book.get("Pages"),
            "genre": book.get("Genre"),
            })

while new_book:
    for user in new_users:
        if len(new_book) > 0:
            user['books'].append(new_book.pop())

with open("result.json", "w") as result_file:
    result_file.write(json.dumps(new_users, indent=4))