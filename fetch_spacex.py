import requests
from dotenv import load_dotenv
import file_functions

def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    json = response.json()
    images = json.get('links').get('flickr').get('original')

    for image in images:
        file_functions.download_file(image, image.split('/')[-1])
        file_functions.convert_image(image.split('/')[-1])


if __name__ == '__main__':
    load_dotenv()
    fetch_spacex_last_launch()
