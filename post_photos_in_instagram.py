import os
import glob
import time
from instabot import Bot
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    pics = glob.glob('{}/*.jpg'.format(os.getenv('CONVERTED_FOLDER')))

    bot = Bot()
    bot.login(username=os.getenv('INSTAGRAM_LOGIN'), password=os.getenv('INSTAGRAM_PASSWORD'), use_cookie=False)

    for pic in pics:
        bot.upload_photo(pic)

        if bot.api.last_response.status_code != 200:
            print(bot.api.last_response)
        time.sleep(30)
