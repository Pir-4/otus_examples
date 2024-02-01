import json
import csv
from csv import DictReader
from files_hw import JSON_FILE, CSV_FILE

# открываю json, записываю из него данные
result = []
with open(JSON_FILE, "r") as f:
    users = json.load(f)
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "book": []})
#        len(result)

# преобразую csv не с помощью DictReader чтобы сразу убрать
with open(CSV_FILE, newline='') as f2:
    reader = DictReader(f2)
    array_dict = []

    # Итерируюсь по данным, делая из них словари
    for row in reader:
        array_dict.append(row)  # словарь книг
        # print("array_dict", array_dict)

user_count = len(result)  # кол-во пользователей

# распределяю книги по пользователям
counter = 0
for book in array_dict:
    current_user_index = counter % user_count  # вычисляю индекс текущего пользователя
    result[current_user_index]['book'].append(  # добавляю книги пользователям
        {
            'title': book['Title'],
            'author': book['Author'],
            'pages': book['Pages'],
            'genre': book['Genre']
        }
    )
    counter += 1

with open('result.json', "w") as f:
    s = json.dumps(result, indent=4)  # записываю в файл результаты
    f.write(s)
