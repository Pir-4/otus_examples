import json
from copy import deepcopy
from csv import DictReader
from csv_and_json_files import CSV_FILE, JSON_FILE, JSON_RESULT_FILE


def get_books_from_csv():
    """"чтение CSV файла"""

    with open(CSV_FILE, "r") as f:
        books = DictReader(f)
        read_csv = []
        for row in books:
            read_csv.append(row)
    return read_csv


def create_book_list(read_csv):
    """"формирование списка книг"""
    book_list = []
    for i in read_csv:
        book_result = {
            key: value
            for key, value in i.items()
            if key in ("Title", "Author", "Pages", "Genre")
        }
        book_result["title"] = book_result.pop("Title")
        book_result["author"] = book_result.pop("Author")
        book_result["pages"] = int(book_result.pop("Pages"))
        book_result["genre"] = book_result.pop("Genre")
        book_list.append(book_result)

    return book_list


def get_users_from_json():
    """"чтение JSON файла"""

    with open(JSON_FILE, "r") as f:
        users_total = json.loads(f.read())
    return users_total


def create_users_list(users_total):
    """"формирование списка пользователей"""
    users_list = []
    for users in users_total:
        users_result = {
            key: value
            for key, value in users.items()
            if key in ("name", "gender", "address", "age")
        }
        users_result["books"] = []
        users_list.append(users_result)
    return users_list


def books_to_users(books_list, users_list):
    """"раздача книг пользователям"""
    result_list = deepcopy(users_list)
    users_numbers = len(users_list)

    for index, book in enumerate(books_list):
        i = index % users_numbers
        user = result_list[i]
        user['books'].append(book)
    return result_list


def add_result_json(result_list):
    """"запись результата в итоговый Json"""
    with open(JSON_RESULT_FILE, "w") as file:
        json.dump(result_list, file, indent=4)
        file.write("\n")


def main():
    read_csv = get_books_from_csv()
    books_processed = create_book_list(read_csv)
    read_json = get_users_from_json()
    users_processed = create_users_list(read_json)
    result = books_to_users(books_processed, users_processed)
    add_result_json(result)


if __name__ == "__main__":
    main()