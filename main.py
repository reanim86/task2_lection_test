import configparser
import requests

def get_folder(name_folder):
    """
    Функция создает папку куда будем загружать фото, на вход принимаем имя папки
    """
    config = configparser.ConfigParser()
    config.read('token.ini')
    ya_token = config['DEFAULT']['ya_token']
    url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {ya_token}'
    }
    params_ya = {
        'path': name_folder
    }
    response = requests.put(url=url_ya, headers=headers, params=params_ya)
    return response.status_code

if __name__ == '__main__':
    get_folder('test1')
