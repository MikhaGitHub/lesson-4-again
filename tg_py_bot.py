import telegram
import os
import time
import random
import argparse
from dotenv import load_dotenv

def main():
    load_dotenv()
    secret_token_bot = os.getenv("TOKEN_BOT")
    bot = telegram.Bot(token=secret_token_bot)

    parser = argparse.ArgumentParser()
    parser.add_argument("--publication_frequency",type=int, default=4*3600,  help="display in which hours need to pulicate photos")
    parser.add_argument("--choice_photo", type=str, help="enter the name of file")

    args = parser.parse_args()
    frequency = args.publication_frequency * 3600

    while True:
        if args.choice_photo is None:
            for item in os.walk("images"):
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

if __name__ == "__main__":
    main()