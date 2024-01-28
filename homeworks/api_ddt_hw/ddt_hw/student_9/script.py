from files import csv_file
import csv
import json
from files import json_file
from files import result_json_file

#Функция, которая делает словарь из книг
with open(csv_file,newline="") as some_file:
    chitatel = csv.reader(some_file)
    zagolovki = next(chitatel)

    knigi = []

    for i in chitatel:
        knigi.append(dict(zip(zagolovki, i)))


# Выводит словарь из юзеров
with open(json_file, "r") as f:
    users = json.loads(f.read())


# Из библиотеки людей достам нужную инфу

pipls = []
for user in users:
    pipls.append({
        "name": user.get('name'),
        "gender": user.get("gender"),
        "address": user.get("address"),
        "age": user.get("age"),
        "books":[]
    })



# Раздача книг
while len(knigi) > 0:
    for pipl in pipls:
        if len(knigi) != 0 :
            pipl["books"].append({
                "title" : knigi[0].get("Title"),
                "author": knigi[0].get("Author"),
                "pages": knigi[0].get("Pages"),
                "genre": knigi[0].get("Genre")
            })
            knigi.pop(0)



with open(result_json_file, "w") as f:
    h = json.dumps(pipls, indent=4)
    f.write(h)