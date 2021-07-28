import requests
from dotenv import load_dotenv
import file_functions


def download_image_by_id(id):
    url = r'http://hubblesite.org/api/v3/image/{}'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    image = response.json().get('image_files')[-1]
    file_url = 'https:' + image.get('file_url')
    file_name = str(id) + file_functions.get_file_extension(file_url)
    try:
        file_functions.download_file(file_url, file_name)
        file_functions.convert_image(file_name)
    except Exception:
        pass


if __name__ == '__main__':
    load_dotenv()
    response = requests.get('https://hubblesite.org/api/v3/images/holiday_cards')
    response.raise_for_status()
    images = response.json()
    for image in images:
        download_image_by_id(image['id'])
