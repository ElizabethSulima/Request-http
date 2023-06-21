import requests
import os

class YaUploader:

    host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def authorization(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'v1/disk/resources/upload/'
        request_url = self.host + url
        params = {
            'path': 'file.docx',
            'overwrite': True
        }
        resp = requests.get(request_url, headers=self.authorization(), params=params).json()
        upload_link = resp.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'), headers=self.authorization())
        print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.abspath("C:/Users/Lenovo/Desktop/Requests/test_1.txt")
    token = 'OAuth '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


