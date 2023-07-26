import csv
import json

from . import CSV_FILE_PATH, JSON_FILE_PATH


def func():
    with open(JSON_FILE_PATH) as f:
        users = json.load(f)

    users_data = []
    for item in range(len(users)):
        user = {
            "name": users[item]['name'],
            "gender": users[item]['gender'],
            "address": users[item]['address'],
            "age": users[item]['age'],
            "books": []
        }
        users_data.append(user)

    books_data = []
    with open(CSV_FILE_PATH, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row.pop('Publisher')
            row['Pages'] = int(row['Pages'])
            books_data.append(row)

    i, j = 0, 0
    while i < len(books_data):
        if j < len(users_data):
            users_data[j]['books'].append(books_data[i])
            j += 1
        else:
            j = 0
        i += 1

    with open("result.json", "w") as f:
        f.write(json.dumps(users_data, indent=4))


func()