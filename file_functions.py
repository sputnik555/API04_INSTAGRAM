import requests
import urllib.parse
import os.path
from pathlib import Path
from PIL import Image


def download_file(url, file_name, download_path):
    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(download_path / file_name, 'wb') as file:
        file.write(response.content)


def convert_image(file_name, download_path, converted_path, image_size):
    image = Image.open(download_path / file_name)
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
