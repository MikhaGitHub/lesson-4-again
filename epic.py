from main_functions import download_img
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import os
import argparse
from datetime import datetime

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="This code download images from Apod NASA in your folder")
    parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
    args = parser.parse_args()
    folder = args.folder
    api_key_epic = os.getenv("API_KEY_NASA")
    payload = {
        "api_key": api_key_epic,
    }
    base_url = f"https://api.nasa.gov/EPIC/api/natural/"
    response = requests.get(base_url, params=payload)
    response.raise_for_status()
    for img_count, img in enumerate(response.json()):
        img_identifier = img["image"]
        img_date = str(img["date"])
        img_date_split = img_date.split()[0]
        parts = img_date_split.split('-')
        url_date = "/".join(parts)
        url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{img_identifier}.png'
        filename = f'epic_{img_count}.png'
        download_img(url, filename, folder, payload)


if __name__ == "__main__":
     main()