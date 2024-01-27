import csv

from files import CSV_FILE_PATH


def open_books_file():
    with open(CSV_FILE_PATH, newline='') as books_csv_file:
        row = csv.DictReader(books_csv_file)

        result_key = ['Title', 'Author', 'Pages', 'Genre']
        books_with_req_keys = []

        for book in row:
            book_data = {key.lower(): value for key, value in book.items() if key in result_key}
            books_with_req_keys.append(book_data)

    return books_with_req_keys