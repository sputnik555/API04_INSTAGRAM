import os
import glob
import time
import file_functions
from instabot import Bot
from dotenv import load_dotenv


IMAGE_SIZE = 1080


if __name__ == '__main__':
    load_dotenv()
    download_folder = os.getenv('DOWNLOAD_FOLDER')
    converted_folder = os.getenv('CONVERTED_FOLDER')
    bot = Bot()
    bot.login(username=os.getenv('INSTAGRAM_LOGIN'), password=os.getenv('INSTAGRAM_PASSWORD'), use_cookie=False)

    pics = glob.glob('{}/*'.format(download_folder))
    for pic_path in pics:
        filename = file_functions.get_url_tail(pic_path)
        file_functions.convert_image(filename, download_folder, converted_folder, IMAGE_SIZE)



    pics = glob.glob('{}/*.jpg'.format(os.getenv('CONVERTED_FOLDER')))
    for pic in pics:
        bot.upload_photo(pic)

        if bot.api.last_response.status_code != 200:
            print(bot.api.last_response)
        time.sleep(30)
