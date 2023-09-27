import os

"""Takes paths of files"""


def get_files_path(file_name):
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, file_name)


BOOKS_FOR_PEOPLE_FILE_R = get_files_path("books.csv")
USERS_FILE = get_files_path("users.json")

JSON_FILE_FOR_WRITE = get_files_path("ready_users.json")