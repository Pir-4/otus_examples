import json
import work_with_users
import work_with_books

from files import RESULT_FILE_PATH


def get_result_dict():
    users = work_with_users.open_users_file()
    books = work_with_books.open_books_file()

    stop = False
    book_index = 0

    while not stop:
        for user in users:
            try:
                book = books[book_index]
                user['books'].append(book)
                print(f"{book['title']} added to {user['name']}'s books")
                book_index += 1
            except IndexError:
                stop = True
                break

    return users


def get_result_file():
    users = get_result_dict()
    with open(RESULT_FILE_PATH, 'w') as result_json_file:
        result = json.dumps(users, indent=4)
        result_json_file.write(result)