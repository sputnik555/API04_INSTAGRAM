import requests
import os
from dotenv import load_dotenv
import file_functions


IMAGE_SIZE = 1080


def download_image_by_id(id, download_folder, converted_folder, image_size):
    url = r'http://hubblesite.org/api/v3/image/{}'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    image = response.json().get('image_files')[-1]
    file_url = 'https:{}'.format(image.get('file_url'))
    file_name = f'{str(id)}{file_functions.get_file_extension(file_url)}'
    file_functions.download_file(file_url, file_name, download_folder)
    file_functions.convert_image(file_name, download_folder, converted_folder, image_size)


if __name__ == '__main__':
    load_dotenv()
    converted_folder = os.getenv('CONVERTED_FOLDER')
    download_folder = os.getenv('DOWNLOAD_FOLDER')
    response = requests.get('https://hubblesite.org/api/v3/images/holiday_cards')
    response.raise_for_status()
    images = response.json()
    for image in images:
        try:
            download_image_by_id(image['id'], download_folder, converted_folder, IMAGE_SIZE)
        except:
            print('Ошибка при загрузке/конвертации файла файла')
