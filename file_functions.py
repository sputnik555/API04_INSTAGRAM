import os
import requests
import urllib.parse
import os.path
from pathlib import Path
from PIL import Image


IMAGE_SIZE = 1080


def download_file(url, file_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    download_path = Path(os.getenv("DOWNLOAD_FOLDER"))
    if not download_path.exists():
        download_path.mkdir()

    with open(download_path / file_name, 'wb') as file:
        file.write(response.content)


def convert_image(file_name):
    converted_path = Path(os.getenv("CONVERTED_FOLDER"))
    if not converted_path.exists():
        converted_path.mkdir()

    image = Image.open(Path(os.getenv("DOWNLOAD_FOLDER")) / file_name)
    image.thumbnail((IMAGE_SIZE, IMAGE_SIZE))
    image.save(converted_path / (os.path.splitext(file_name)[-2] + '.jpg'), format='JPEG')


def get_url_tail(url):
    url_path = urllib.parse.urlparse(url).path
    return os.path.split(url_path)[-1]


def get_file_extension(url):
    return os.path.splitext(urllib.parse.urlparse(url).path)[-1]
