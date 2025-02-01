import telegram
import os
import time
import random
import argparse
from dotenv import load_dotenv

        

def main():
    load_dotenv(".env")
    secret_token_bot_tg = os.getenv("TOKEN_BOT_TG")
    bot = telegram.Bot(token=secret_token_bot_tg)

    parser = argparse.ArgumentParser()
    parser.add_argument("--publication_frequency",type=int, default=4*3600,  help="display in which hours need to pulicate photos")
    parser.add_argument("--choice_photo", type=str, help="enter the name of file")
    parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
    parser.add_argument('--chat_id', type=str, default="@spaceX_imgs", help="Enter your chat id")

    args = parser.parse_args()
    frequency = args.publication_frequency * 1
    folder = args.folder
    chat_id = args.chat_id

    while True:
        if not args.choice_photo:
            for root, _, files in os.walk(folder):
                random.shuffle(files)
                for file in files:
                    filepath = os.path.join(root, file)
                    with open(filepath, "rb") as f:
                        bot.send_document(chat_id=chat_id, document=f)

        else:
            filepath = os.path.join(folder, args.choice_photo)
            if os.path.exists(filepath):
                with open(filepath, "rb") as f:
                    bot.send_document(chat_id=chat_id, document=f)
                    break

        time.sleep(frequency)

if __name__ == "__main__":
    main()