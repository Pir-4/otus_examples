import os.path

FILES_DIR = os.path.dirname(__file__)

def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

BOOKS_CSV_PATH = get_path(filename="books.csv")
USERS_JSON_PATH = get_path(filename="users.json")