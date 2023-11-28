import json
import csv


def get_books_from_csv(file_name: str) -> list:
    books_list = []
    books_keys = ["Title", "Author", "Pages", "Genre"]

    with open(file_name, "r") as csv_file:
        for row in csv.DictReader(csv_file):
            data = {key: value for key, value in row.items() if key in books_keys}
            if "Pages" in data:
                data["Pages"] = int(data["Pages"])
            data = {key.lower(): data.pop(key) for key in books_keys}
            books_list.append(data)

    return books_list


def get_users_from_json(file_name: str) -> list:
    users_list = []
    users_keys = ["name", "gender", "address", "age"]

    with open(file_name, "r") as json_file:
        users_original = json.load(json_file)

    for user in users_original:
        data = {key: value for key, value in user.items() if key in users_keys}
        data = {key: data.pop(key) for key in users_keys}
        users_list.append(data)

    return users_list


def assign_books_to_users(books_list: list, users_list: list) -> list:
    result_list = []
    books_per_user = len(books_list) // len(users_list)
    remaining_books = len(books_list) % len(users_list)

    for i, user in enumerate(users_list):
        user_books = books_list[i * books_per_user : (i + 1) * books_per_user]

        if i < remaining_books:
            user_books.append(books_list[len(users_list) * books_per_user + i])

        user["books"] = user_books
        result_list.append(user)

    return result_list


def export_json_to_file(result_list: list) -> None:
    with open("result.json", "w") as file:
        json.dump(result_list, file, indent=4)
        file.write("\n")


def main():
    json_file_name = "users.json"
    csv_file_name = "books.csv"

    books_processed = get_books_from_csv(csv_file_name)
    users_processed = get_users_from_json(json_file_name)

    result = assign_books_to_users(books_processed, users_processed)
    export_json_to_file(result)


if __name__ == "__main__":
    main()