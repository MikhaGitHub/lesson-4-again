from main_functions import download_img
import requests
import argparse

def main():
    try:
        parser = argparse.ArgumentParser(description="This code download images from Apod NASA in your folder")
        parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
        args = parser.parse_args()
        folder = args.folder
        json_latest="https://api.spacexdata.com/v5/launches/latest"
        response_latest = requests.get(json_latest)
        response_latest.raise_for_status()
        links_latest = response_latest.json()["links"]["flickr"]["original"]
        if not links_latest:
            json_spacex = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
            response = requests.get(json_spacex)
            response.raise_for_status()
            access_json_urls = response.json()["links"]["flickr"]["original"]


            for img_count, url in enumerate(access_json_urls):
                filename = f"spaceX_{img_count}.jpg"
                download_img(url, filename, folder)
        else:
            for img_count, url in enumerate(links_latest):
                filename = f"spaceX_{img_count}.jpg"
                download_img(url, filename, folder)
    except requests.exceptions.HTTPError as err:
        print(f'Server is not available, Error HTTP:{err}')


if __name__ == "__main__":
    main()