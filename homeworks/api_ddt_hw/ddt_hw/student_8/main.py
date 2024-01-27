from csv import DictReader
import os
import json
import itertools


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


with open(get_path('books.csv'), newline='') as f:
    book_list = list(DictReader(f))
desired_attributes = ["Title", "Author", "Pages", "Genre"]
filtered_books_list = [{key: book[key] for key in desired_attributes} for book in book_list]


with open(get_path('users.json'), "r") as f:
    users_list = json.load(f)
desired_attributes = ["name", "gender", "address", "age"]
filtered_users_list = [{key: user[key] for key in desired_attributes} for user in users_list]

cycle_iterator_users = itertools.cycle(filtered_users_list)

for book in filtered_books_list:
    user = next(cycle_iterator_users)
    if "books" not in user:
        user["books"] = []
    user["books"].append(book)

with open(get_path('result.json'), "w") as f:
    s = json.dumps(filtered_users_list, indent=4)
    f.write(s)

