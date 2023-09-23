import csv
import json

books_file = 'books.csv'
users_file = 'users.json'
result_file = 'result.json'


def get_books():
    try:
        with open(books_file, "r", encoding="utf-8") as f:
            books_raw = csv.DictReader(f)
            books = [dict(filter(lambda key: key[0] != "Publisher", row.items())) for row in books_raw]
            return books
    except (Exception, IOError) as e:
        print(e)


def get_users():
    try:
        with open(users_file, "r", encoding="utf-8") as f:
            users_raw = json.loads(f.read())
            keys = ("name", "gender", "address", "age")
            # users = [dict(filter(lambda key: key[0] in keys, row.items())) for row in users_raw]
            # list(map(lambda d: d.update({"books": []}), users))
            users = []
            for user_data in users_raw:
                user = {key: val for key, val in user_data.items() if key in keys}
                users.append(
                    user | {'books': []}
                )
            return users
    except (Exception, IOError) as e:
        print(e)


def distribute_books(users, books):
    if isinstance(users, list) and isinstance(books, list):
        i = 0
        while i < len(books):
            for user in users:
                user["books"].append(books[i])
                i += 1
                if i == len(books):
                    break
        return users


def write_result(result):
    if isinstance(result, list):
        try:
            with open(result_file, "w", encoding="utf-8") as f:
                f.write(json.dumps(result, indent=4, ensure_ascii=False))
            print(f'Файл {result_file} создан')
        except (Exception, IOError) as e:
            print(e)
    else:
        print(f'Файл {result_file} не создан')


def main():
    r = distribute_books(get_users(), get_books())
    write_result(r)


if __name__ == '__main__':
    main()