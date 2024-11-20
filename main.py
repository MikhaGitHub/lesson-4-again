import requests
from dotenv import load_dotenv
import os
from main_functions import downloading_img
from fetch_SpaceX import fetch_spacex_last_launch
from apod import give_URL_APOD
from epic import get_url_from_Epic
from tg_py_bot import send_photos_tg


def get_first_img_url():
    url = "https://img-cdn.pixlr.com/image-generator/history/65bb506dcb310754719cf81f/ede935de-1138-4f66-8ed7-44bd16efc709/medium.webp"
    filename = 'hubble.jpeg'
    directory = "images"
    downloading_img(url, filename, directory)


def main():
    load_dotenv()
    secret_key = os.getenv("API_KEY")
    secret_token_bot = os.getenv("TOKEN_BOT")

    print(get_url_from_Epic(secret_key))

    fetch_spacex_last_launch()
    get_first_img_url()
    give_URL_APOD(secret_key)
    send_photos_tg(secret_token_bot)


if __name__ == "__main__":
    main()
