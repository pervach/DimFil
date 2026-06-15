
import pandas as pd
import requests

def load_csv(file_path, sep=',', encoding='utf-8'):
    return pd.read_csv(file_path, sep=sep, encoding=encoding)

def load_json(file_path):
    return pd.read_json(file_path)

def load_api(url):
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())
