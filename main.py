import requests
import os
import glob
import time
from dotenv import load_dotenv
from urllib.parse import urlsplit
from PIL import Image
from instabot import Bot

DOWNLOAD_FOLDER = 'images'
CONVERTED_FOLDER = 'converted_images'

def download_file(url,file_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    with open(DOWNLOAD_FOLDER + '\\' + file_name, 'wb') as file:
        file.write(response.content)


def convert_image(file_name):
    if not os.path.exists(CONVERTED_FOLDER):
        os.makedirs(CONVERTED_FOLDER)

    image = Image.open(DOWNLOAD_FOLDER + '\\' + file_name)
    print('до ' + str(image.size))
    image.thumbnail((1080,1080))
    print('после ' + str(image.size))
    image.save(CONVERTED_FOLDER + '\\' + os.path.splitext(file_name)[-2] + '.jpg', format='JPEG')


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    json = response.json()
    images = json.get('links').get('flickr').get('original')

    for image in images:
        download_file(image, image.split('/')[-1])
        convert_image(image.split('/')[-1])


def get_file_extension(url):
    return os.path.splitext(urlsplit(url).path)[-1]


def download_image_byid(id):
    url = r'http://hubblesite.org/api/v3/image/{}'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    json = response.json()
    image = json.get('image_files')[-1]
    file_url = 'https:' + image.get('file_url')
    file_name = str(id) + get_file_extension(file_url)
    download_file(file_url, file_name)
    convert_image(file_name)

if __name__ == '__main__':
    load_dotenv()
    fetch_spacex_last_launch()
    # response = requests.get('https://hubblesite.org/api/v3/images/printshop')
    # response.raise_for_status()
    # json = response.json()
    # count = 0
    # for image in json:
    #     download_image_byid(image['id'])

    # pics = glob.glob(CONVERTED_FOLDER + "/*.jpg")
    #
    # bot = Bot()
    # bot.login(username='hubblephotos_', password='240989aA', use_cookie=False)
    #
    # for pic in pics:
    #   bot.upload_photo(pic)
    #
    #   if bot.api.last_response.status_code != 200:
    #       print(bot.api.last_response)
    #   time.sleep(30)