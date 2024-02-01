import json
import csv

from files_hw import JSON_FILE, JSON_FILE_W, CSV_FILE

# открываю json, записываю из него данные
result = []
with open(JSON_FILE, "r") as f:
    users = json.load(f)
    for i in users:
        result.append({"name": i['name'], "gender": i['gender'], "address": i['address'],
                       "age": i['age'], "Book": []})
        len(result)

# преобразую csv не с помощью DictReader чтобы сразу убрать
# Издательство и не писать потом больше строк прописывая заголовки
with open(CSV_FILE, newline='') as f2:
    reader = csv.reader(f2)
    array_dict = []
    # Извлекаю заголовок
    header = next(reader)[:4]
    # Итерируюсь по данным, делая из них словари
    for row in reader:
        csv_dict = dict(zip(header, row))  # делает словарь с ключом
        array_dict.append(csv_dict)  # словарь книг

user_count = len(result)  # кол-во пользователей

# распределяю книги по пользователям
counter = 0
for book in array_dict:
    current_user_index = counter % user_count  # вычисляю индекс текущего пользователя
    result[current_user_index]['Book'].append(book)  # добавляю книги пользователям
    counter += 1

with open(JSON_FILE_W, "w") as f:
    s = json.dumps(result, indent=4)  # записываю
    f.write(s)