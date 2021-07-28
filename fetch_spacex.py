import requests
from dotenv import load_dotenv
import file_functions


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    images_links = response.json().get('links').get('flickr').get('original')

    for image in images_links:
        file_name = file_functions.get_url_tail(image)
        file_functions.download_file(image, file_name)
        file_functions.convert_image(file_name)


if __name__ == '__main__':
    load_dotenv()
    fetch_spacex_last_launch()
