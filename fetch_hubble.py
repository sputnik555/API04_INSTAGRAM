import requests
import os
from urllib.parse import urlsplit
from dotenv import load_dotenv
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
    try:
        image.save(os.getenv("CONVERTED_FOLDER") + '\\' + os.path.splitext(file_name)[-2] + '.jpg', format='JPEG')
    except:
        pass

def download_image_by_id(id):
    url = r'http://hubblesite.org/api/v3/image/{}'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    json = response.json()
    image = json.get('image_files')[-1]
    file_url = 'https:' + image.get('file_url')
    file_name = str(id) + get_file_extension(file_url)
    try:
        download_file(file_url, file_name)
        convert_image(file_name)
    except:
        pass


def get_file_extension(url):
    return os.path.splitext(urlsplit(url).path)[-1]


if __name__ == '__main__':
    load_dotenv()
    response = requests.get('https://hubblesite.org/api/v3/images/holiday_cards')
    response.raise_for_status()
    json = response.json()
    for image in json:
        download_image_by_id(image['id'])
