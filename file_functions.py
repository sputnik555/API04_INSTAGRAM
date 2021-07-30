import requests
import urllib.parse
import os.path
from pathlib import Path
from PIL import Image


def download_file(url, file_name, download_folder):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    download_path = make_dir(download_folder)

    with open(download_path / file_name, 'wb') as file:
        file.write(response.content)


def convert_image(file_name, download_folder, converted_folder, image_size):
    converted_path = make_dir(converted_folder)
    image = Image.open(Path(download_folder) / file_name)
    image.thumbnail((image_size, image_size))
    image.save(converted_path / '{}.jpg'.format(os.path.splitext(file_name)[-2]), format='JPEG')


def get_url_tail(url):
    url_path = urllib.parse.urlparse(url).path
    unquote_url_path = urllib.parse.unquote(url_path)
    return os.path.split(unquote_url_path)[-1]


def get_file_extension(url):
    unquoted_url = urllib.parse.unquote(url)
    return os.path.splitext(urllib.parse.urlparse(unquoted_url).path)[-1]


def make_dir(dir_name):
    new_path = Path(dir_name)
    new_path.mkdir(exist_ok=True)
    return new_path
