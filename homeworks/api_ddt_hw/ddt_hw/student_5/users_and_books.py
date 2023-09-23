import csv
import json

result = [] # результирующий список

# Открываем файл на чтение
with open("users.json", "r") as users_file:
    users = json.load(users_file)   # Чтение файла и преобразование данных JSON в объект Python
    for user in users:
        result.append(              # заполняем список result пользователями
            {'name': user['name'],
             'gender': user['gender'],
             'address': user['address'],
             'age': user['age'],
             'books': []
             }
        )

with open("books.csv", "r") as books_file:
    books = csv.DictReader(books_file)
    i = 0
    for book in books:
        result[i % len(result)]['books'].append(
            {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre']
            }
        )
        i += 1

# записываем результат в итоговый файл
with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)


"""
с 19 по 31 строку берем результирующий список result с юзерами, находим остаток от деления вычисляем соотв. индекс юзера
первый индекс юзера будет = 0, потом 1 и т.п. К result[0] мы добавляем 1 книгу, к result[1] добавляем 2 книгу и т.д.
Когда юзеры кончаются, к ним по новой добавляются книги по порядку. Т.е. возвращаемся к первому юзеру, когда перебрали
всех, и продолжаем им раздавать книги. Каждый раз при достижении конца списка мы возвращаемся в начало
Пример - 2 юзера и 3 книги. 0%2=0, тогда к юзеру result[0] добавляется 1 книга. потом 1%2=1, тогда к юзеру result[1]
добавляется 2 книга. 2%2 = 0, тогда к юзеру result[0] добавляется 3 книга
"""""