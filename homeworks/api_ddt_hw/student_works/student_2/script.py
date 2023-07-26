import csv
import json

with open('books.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    books = [row for row in csv_reader]

with open('users.json', 'r') as json_file:
    users = json.load(json_file)

num_users = len(users)
num_books = len(books)
books_per_user = num_books // num_users
remaining_books = num_books % num_users

result = []

book_index = 0
for user in users:
    user_data = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }

    for _ in range(books_per_user):
        user_data["books"].append({
            "Title": books[book_index]["Title"],
            "Author": books[book_index]["Author"],
            "Pages": int(books[book_index]["Pages"]),
            "Genre": books[book_index]["Genre"]
        })
        book_index += 1

    if remaining_books > 0:
        user_data["books"].append({
            "Title": books[book_index]["Title"],
            "Author": books[book_index]["Author"],
            "Pages": int(books[book_index]["Pages"]),
            "Genre": books[book_index]["Genre"]
        })
        book_index += 1
        remaining_books -= 1

    result.append(user_data)

with open('result.json', 'w') as result_file:
    json.dump(result, result_file, indent=4)