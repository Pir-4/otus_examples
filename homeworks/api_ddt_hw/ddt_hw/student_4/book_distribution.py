import csv
import json


def book_distribution():
    # чтение csv файла, формирование списка с книгами (берем не все поля из исходного файла)
    with open("books.csv", "r") as f:
        books = csv.DictReader(f)
        new_books = []
        for i in books:
            book_res = {
                key: value
                for key, value in i.items()
                if key in ("Title", "Author", "Genre", "Pages")
            }
            new_books.append(book_res)

    # чтение json файла
    with open("users.json", "r") as f:
        users = json.load(f)

    # формирование списка с юзерами
    users_result = []

    for user in users:
        user_res = {
            key: value
            for key, value in user.items()
            if key in ("name", "gender", "address", "age", "books")
        }
        user_res["books"] = []
        users_result.append(user_res)

    # раздача книг юзерам
    while new_books:
        for user_res in users_result:
            if new_books:
                user_res["books"].append(new_books.pop())
            else:
                break

    # сохранение результатов в итоговый файл
    with open("result.json", "w") as f:
        json.dump(users_result, f, indent=4)


book_distribution()