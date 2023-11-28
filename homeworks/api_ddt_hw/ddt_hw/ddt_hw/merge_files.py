import csv, json

from data import USERS_FILE_PATH, BOOKS_FILE_PATH

result = []

"Создание списка словарей пользователей"
with open(USERS_FILE_PATH, "r") as u_file:
    user_file = json.load(u_file)
    u_list = []
    for u in user_file:
        name = u["name"]
        gender = u["gender"]
        address = u["address"]
        age = u["age"]
        u_item = {"name": name, "gender": gender, "address": address, "age": age}
        u_list.append(u_item)

"Создание списка словарей книг"
with open(BOOKS_FILE_PATH, newline='') as b_file:
    books_file = csv.DictReader(b_file)
    b_list = []
    for b in books_file:
        title = b["Title"]
        author = b["Author"]
        pages = b["Pages"]
        genre = b["Genre"]
        b_item = {"title": title, "author": author, "pages": pages, "genre": genre}
        b_list.append(b_item)

"Распределение книг между пользователями"
x = (len(b_list) // len(u_list))
a = 0
b = x
for i in u_list:
    if u_list.index(i) < (len(b_list) % len(u_list)):
        b += 1
    b_list_user = b_list[a:b]
    i.update({"books": b_list_user})
    if b <= len(b_list):
        a = b
        b += x
result.append(u_list)

"Запись в json-файл"
with open("result.json", "w") as f:
    s = json.dumps(result, indent=4)
    f.write(s + "\n")