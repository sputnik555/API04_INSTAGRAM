import requests
import file_functions
import os
from requests import HTTPError
from dotenv import load_dotenv


def fetch_spacex_last_launch(download_path):
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']

    for image in image_links:
        file_name = file_functions.get_url_tail(image)
        file_functions.download_file(image, file_name, download_path)


if __name__ == '__main__':
    load_dotenv()
    download_path = file_functions.make_dir(os.getenv('DOWNLOAD_FOLDER'))
    try:
        fetch_spacex_last_launch(download_path)
    except HTTPError:
        print('Ошибка загрузки файлов')
