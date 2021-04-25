import json
import pickle


def load_json(file_path, file_format='rt', encoding='utf-8'):
    try:
        with open(file_path, file_format, encoding=encoding) as f:
            data = json.load(f)
            data = data if data and isinstance(data, dict) else {}
        return data
    except FileNotFoundError:
        return {}


def load_pickle(file_path, file_format='rb', encoding=None):
    try:
        with open(file_path, file_format, encoding=encoding) as f:
            data = pickle.load(f)
            data = data if data else None
            return data
    except FileNotFoundError:
        return None


def load_txt(file_path, file_format='rt', encoding=None):
    try:
        with open(file_path, file_format, encoding=encoding) as f:
            data = f.read()
            data = data if data else None
            return data
    except FileNotFoundError:
        return None


def load_bin(file_path, file_format='rb'):
    try:
        with open(file_path, file_format) as f:
            data = f.read()
            data = data if data else None
            return data
    except FileNotFoundError:
        return None


def save_json(data, file_path, file_format='wt', encoding='utf-8'):
    with open(file_path, file_format, encoding=encoding) as f:
        json.dump(data, f)


def save_pickle(data, file_path, file_format='wb', encoding=None):
    with open(file_path, file_format, encoding=encoding) as f:
        pickle.dump(data, f)


def save_txt(data, file_path, file_format='wt', encoding=None):
    with open(file_path, file_format, encoding=encoding) as f:
        f.write(data)


def save_bin(data, file_path, file_format='wb'):
    with open(file_path, file_format) as f:
        f.write(data)
