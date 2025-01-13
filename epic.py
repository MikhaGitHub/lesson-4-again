from main_functions import download_img
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import os
import argparse

def main():
    try:
        load_dotenv()
        parser = argparse.ArgumentParser(description="This code download images from Apod NASA in your folder")
        parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
        args = parser.parse_args()
        folder = args.folder
        api_key = os.getenv("API_KEY")
        payload = {
            "api_key": api_key,
        }
        base_url = f"https://api.nasa.gov/EPIC/api/natural/"
        json_response = requests.get(base_url, params=payload)
        json_response.raise_for_status()
        for img_count, img in enumerate(json_response.json()):
            img_identifier = img["image"]
            img_date = str(img["date"])
            img_date_split = img_date.split()[0]
            symbol = '-'
            for string in img_date_split:
                if string == symbol:
                    url_date = img_date_split.replace(string, '/')
                    url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{img_identifier}.png'
                    filename = f'epic_{img_count}.png'
                    Path(f"/{folder}").mkdir(parents=True, exist_ok=True)
                    response = requests.get(url, params=payload)
                    response.raise_for_status()
    
                    with open(f'{folder}/{filename}', 'wb') as file:
                        file.write(response.content)

    except requests.exceptions.HTTPError as err:
        print(f'Server is not available, Error HTTP:{err}')


if __name__ == "__main__":
     main()