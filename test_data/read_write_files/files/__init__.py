import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


TXT_FILE = get_path('poem.txt')
CSV_FILE = get_path('users.csv')
JSON_FILE = get_path('users.json')
YAML_FILE = get_path('config.yaml')

TXT_FILE_W = get_path('poem_w.txt')
CSV_FILE_W = get_path('users_w.csv')
JSON_FILE_W = get_path('users_w.json')
YAML_FILE_W = get_path('config_w.yaml')

