import os
import requests
import urllib.parse
import os.path
from PIL import Image


def download_file(url, file_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()

    if not os.path.exists(os.getenv("DOWNLOAD_FOLDER")):
        os.makedirs(os.getenv("DOWNLOAD_FOLDER"))

    with open(os.getenv("DOWNLOAD_FOLDER") + '\\' + file_name, 'wb') as file:
        file.write(response.content)


def convert_image(file_name):
    if not os.path.exists(os.getenv("CONVERTED_FOLDER")):
        os.makedirs(os.getenv("CONVERTED_FOLDER"))

    image = Image.open(os.getenv("DOWNLOAD_FOLDER") + '\\' + file_name)
    image.thumbnail((1080, 1080))
    image.save(os.getenv("CONVERTED_FOLDER") + '\\' + os.path.splitext(file_name)[-2] + '.jpg', format='JPEG')


def get_url_tail(url):
    url_path = urllib.parse.urlparse(url).path
    return os.path.split(url_path)[-1]


def get_file_extension(url):
    return os.path.splitext(urllib.parse.urlparse(url).path)[-1]
