import os
import glob
import time
import file_functions
from instabot import Bot
from dotenv import load_dotenv


IMAGE_SIZE = 1080


def convert_images(download_folder, converted_folder, image_size):
    pics = glob.glob('{}/*'.format(download_folder))
    for pic_path in pics:
        filename = file_functions.get_url_tail(pic_path)
        file_functions.convert_image(filename, download_folder, converted_folder, image_size)


def upload_instagram(converted_path, login, password):
    bot = Bot()
    bot.login(username=login, password=password, use_cookie=False)

    pics = glob.glob('{}/*.jpg'.format(converted_path))
    for pic in pics:
        bot.upload_photo(pic)

        if bot.api.last_response.status_code != 200:
            print(bot.api.last_response)
        time.sleep(30)


if __name__ == '__main__':
    load_dotenv()
    download_path = file_functions.make_dir(os.getenv('DOWNLOAD_FOLDER'))
    converted_path = file_functions.make_dir(os.getenv('CONVERTED_FOLDER'))

    convert_images(download_path, converted_path, IMAGE_SIZE)
    upload_instagram(converted_path, os.getenv('INSTAGRAM_LOGIN'), os.getenv('INSTAGRAM_PASSWORD'))
