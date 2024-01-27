import json
import csv

from csv import DictReader
from files import JSON_FILE, JSON_FILE_W
from files import CSV_FILE

booksDict = {}
booksClean = []

users = {}
userClean = []

key_include_user_columns = {"name", "gender", "address", "age"}
key_include_books_columns = {"Title", "Author", "Pages", "Genre"}


def with_keys(d, keys):
    return {x: d[x] for x in d if x in keys}


with open(CSV_FILE, newline="") as f:
    reader = DictReader(f)
    booksDict = list(reader)

for book in booksDict:
    bookItem = with_keys(book, key_include_books_columns)
    booksClean.append(bookItem)

# print("=== Books ====")
# for i in booksClean:
#     print(i)


with open(JSON_FILE, "r") as f:
    userlist = json.loads(f.read())
    users = list(userlist)


for user in users:
    userItem = with_keys(user, key_include_user_columns)
    userClean.append(userItem)


# print("=== Users ====")
for i in userClean:
    i.update({"books": [i for i in booksClean]})


with open(JSON_FILE_W, "w") as f:
    s = json.dumps(userClean, indent=4)
    f.write(s)