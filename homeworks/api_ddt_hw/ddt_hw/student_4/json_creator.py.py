import csv
import json

# Считываем файлы
with open('input_data/books.csv', newline='') as f1, open('input_data/users.json', "r") as f2:
    books_array = list(csv.DictReader(f1))
    users_list = json.load(f2)

# Распределяем книги равномерно
amount_of_books_per_user = round(len(books_array) / len(users_list)) - 1
count = 0
arr = []
for count in range(round(len(books_array)/amount_of_books_per_user)-1):
    arr.append(books_array[count:count + amount_of_books_per_user])
    count += amount_of_books_per_user
remainder_of_books = len(books_array) - len(arr)*amount_of_books_per_user # Остаток книг

# Добавляем по 1 книге с конца books_array равное остатку (remainder_of_books)
end_of_list = books_array[-remainder_of_books:]
end_of_list = end_of_list.__iter__()
for count_arr in range(len(arr) - remainder_of_books, len(arr)):
    arr[count_arr] = [*arr[count_arr], end_of_list.__next__()]

# Формируем массив словарей
books = []
for book_id in range(len(arr)-1):
    elem_os_set = {
        "name": users_list[book_id]['name'],
        "gender": users_list[book_id]['gender'],
        "address": users_list[book_id]['address'],
        "age": users_list[book_id]['age'],
        "books": arr[book_id]
        }
    books.append(elem_os_set)

# Выполняем запись в json
with open('output_data/library.json', "w") as f:
    s = json.dumps(books, indent=4)
    f.write(s)