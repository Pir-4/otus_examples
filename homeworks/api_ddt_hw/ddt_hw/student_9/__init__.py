import os

def get_pah(fail_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder,fail_name)


csv_file = get_pah("books.csv")
json_file = get_pah("users.json")
result_json_file = get_pah("result.json")