import json
import csv


def parse_books():
    with open('data/books.csv') as book:
        csvfile = csv.DictReader(book)
        booklist0 = [book_dict for book_dict in csvfile]

        booklist = []
        for book in booklist0:
            booklist.append({k.lower(): v for k, v in book.items()})
    return booklist


def parse_users():
    with open('data/users.json') as jsonfile:
        data = json.load(jsonfile)

    resultinglist = [{"name": user_object["name"],
                      "gender": user_object["gender"],
                      "address": user_object["address"],
                      "age": user_object["age"],
                      "books": []}
                     for user_object in data]

    return resultinglist


def redistribute_books(users, books):
    user_id = 0
    while len(books) > 0:
        users[user_id]["books"].append(books.pop())
        if user_id != len(users) - 1:
            user_id += 1
        else:
            user_id = 0
    return users


def make_output_json(userswithbooks):
    with open('result/outputfile.json', "w") as writer:
        json.dump(userswithbooks, writer, indent=4)


make_output_json(redistribute_books(parse_users(), parse_books()))