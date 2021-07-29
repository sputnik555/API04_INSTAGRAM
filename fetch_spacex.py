import requests
import file_functions
import os
from dotenv import load_dotenv


IMAGE_SIZE = 1080


def fetch_spacex_last_launch(download_folder, converted_folder, image_size):
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    images_links = response.json().get('links').get('flickr').get('original')

    for image in images_links:
        file_name = file_functions.get_url_tail(image)
        file_functions.download_file(image, file_name, download_folder)
        file_functions.convert_image(file_name, download_folder, converted_folder, image_size)


if __name__ == '__main__':
    load_dotenv()
    converted_folder = os.getenv('CONVERTED_FOLDER')
    download_folder = os.getenv('DOWNLOAD_FOLDER')
    fetch_spacex_last_launch(download_folder, converted_folder, IMAGE_SIZE)
