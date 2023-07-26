from src.utils import json_load, csv_read_gen, json_dump
from configuration import INPUT_FILE_PATH, OUTPUT_FILE_PATH


def distribute_books(books_file, users_file):
    users = json_load(users_file)

    collected_books = {user["_id"]: [] for user in users}
    for i, book in enumerate(csv_read_gen(books_file)):
        user_id = users[i % len(users)]["_id"]

        collected_books[user_id].append({
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"],
        })

    return [{
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": collected_books[user["_id"]],
        } for user in users]


if __name__ == '__main__':
    books_file_path = INPUT_FILE_PATH + "books.csv"
    users_file_path = INPUT_FILE_PATH + "users.json"
    result_file_path = OUTPUT_FILE_PATH + "result.json"

    json_dump(
        distribute_books(books_file_path, users_file_path),
        result_file_path
    )