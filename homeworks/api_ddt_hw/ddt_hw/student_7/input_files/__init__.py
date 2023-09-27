import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


USERS = get_path('users.json')
BOOKS = get_path('books.csv')