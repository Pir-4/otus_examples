import json
from csv import DictReader

with open("users.json", "r") as json_file:
    users = json.load(json_file)


users_list = [
    {
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': []
    }
    for user in users
]

with open("books.csv", newline="") as csvfile:
    reader = DictReader(csvfile)
    books = list(reader)

books_list = [
    {
        'title': book['Title'],
        'author': book['Author'],
        'pages': book['Pages'],
        'genre': book['Genre'],
    }
    for book in books
]

n = 0
users_count = len(users_list)

for book in books_list:
    user = users_list[n]
    user['books'].append(book)
    n = (n + 1) % users_count

with open("result.json", "w") as file:
    res = json.dumps(users_list, indent=4)
    file.write(res)

