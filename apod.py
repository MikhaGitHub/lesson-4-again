import requests
from main_functions import get_extension_of_file, download_img
from dotenv import load_dotenv
import os
import argparse


def main():
    load_dotenv()
    api_key_nasa_apod = os.getenv("API_KEY_NASA")
    parser = argparse.ArgumentParser(description="This code download images from Apod NASA in your folder")
    parser.add_argument('--count', type=int, default=26, help="enter limit of images")
    parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
    args = parser.parse_args()
    limit = args.count
    folder = args.folder
        
        
    params = {
        "count":limit,
        "api_key":api_key_nasa_apod
    }


    full_url = f"https://api.nasa.gov/planetary/apod"

    apod_response = requests.get(full_url, params=params)
    apod_response.raise_for_status()
    for index_img, img in enumerate(apod_response.json()):
        url = img['url']
        extension = get_extension_of_file(url)
        filename = f'nasa_apod_{index_img}{extension[0]}'
        download_img(url,filename, folder)


if __name__ == "__main__":
     main()
