import csv
import json
from typing import Union


class GetEqualNumberBooks:
    def __init__(self, json_file_name: str, csv_file_name: str):
        self.books_list = self.read_csv(csv_file_name)
        self.users_list = self.read_json(json_file_name)

    def read_csv(self, file_name):
        with open(file_name, newline='') as f:
            return [row for row in csv.DictReader(f)]

    def read_json(self, file_name):
        with open(file_name) as f:
            return json.load(f)

    def give_equal_to_users(self):
        result = []
        users_cnt = len(self.users_list)
        for param in self.users_list:
            result.append({'name': param['name'],
                           'gender': param['gender'],
                           'address': param['address'],
                           'age': param['age'],
                           'books': []
                           })
        for num, book in enumerate(self.books_list):
            if num + 1 > users_cnt:
                num = num % users_cnt
            result[num]['books'].append(book)
        return result

    def write_to_json(self, result: Union[dict, list]):
        with open('result.json', 'w') as f:
            json.dump(result, f, indent=4)
        print('Файл успешно создан')