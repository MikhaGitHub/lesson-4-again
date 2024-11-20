import telegram
import os
import time
import random
import argparse

def send_photos_tg(secret_token_bot):
    bot = telegram.Bot(token=secret_token_bot)
    print(bot.get_me())

    bot.send_document(chat_id="@spaceX_imgs", document=open("images/nasa_apod_1.jpg", 'rb'))

    parser = argparse.ArgumentParser()
    parser.add_argument("publication_frequency",nargs='?',type=int, default=4*3600,  help="display in which hours need to pulicate photos")
    parser.add_argument("choice_photo", nargs='?', type=str, help="enter the name of file")

    args = parser.parse_args()

    frequency = args.publication_frequency * 3600

    while True:
        if args.choice_photo is None:
            for item in os.walk("images"):
                print('args.choice _photo is None!!!!')
                files = item[2]
                random.shuffle(files)
                for file in files:
                    bot.send_document(chat_id="@spaceX_imgs", document=open(f"images/{file}", 'rb'))
                    time.sleep(frequency)
        else:
            for item in os.walk("images"):
                files = item[2]
                if args.choice_photo in files:
                    bot.send_document(chat_id="@spaceX_imgs", document=open(f"images/{args.choice_photo}", 'rb'))
                    time.sleep(frequency)