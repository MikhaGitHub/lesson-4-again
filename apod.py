import requests
from main_functions import get_extension_of_file, download_img
from dotenv import load_dotenv
import os
import argparse


def main():
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        parser = argparse.ArgumentParser(description="This code download images from Apod NASA in your folder")
        parser.add_argument('--count', type=int, default=26, help="enter limit of images")
        parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
        args = parser.parse_args()
        limit = args.count
        folder = args.folder
        
        
        params = {
            "count":limit,
            "api_key":api_key
        }


        full_url = f"https://api.nasa.gov/planetary/apod"

        response_apod = requests.get(full_url, params=params)
        response_apod.raise_for_status()
        for index_img, img in enumerate(response_apod.json()):
            url = img['url']
            response = requests.get(url)
            response.raise_for_status()
            extension = get_extension_of_file(url)
            filename = f'nasa_apod_{index_img}{extension[0]}'
            download_img(url,filename, folder)
    except requests.exceptions.HTTPError as err:
        print(f'Server is not available, Error HTTP:{err}')


if __name__ == "__main__":
     main()

