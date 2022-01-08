import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_href(self, path):
        """Метод для получения ссылки на загрузку файла"""
        upload_link = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {'path': path, 'overwrite': 'true'}
        response = requests.get(upload_link, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self, file_path: str, filename):
        """Метод загружает файл на яндекс диск"""
        href = self._get_href(path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return "Success"
        else:
            return 'Fail'


if __name__ == '__main__':
    path_to_file = 'Музыка/test_file.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, 'test_file.txt')
    print(result)
