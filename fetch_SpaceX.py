from main_functions import download_img
import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="This code download images from Apod NASA in your folder")
    parser.add_argument('--folder', type=str, default="images", help="Enter name of your exesting folder")
    parser.add_argument('--id', type=str, default="5eb87d42ffd86e000604b384", help="Enter id to access urls")
    args = parser.parse_args()
    folder = args.folder
    id_spaceX = args.id
    url_to_latest="https://api.spacexdata.com/v5/launches/latest"
    response_latest = requests.get(url_to_latest)
    response_latest.raise_for_status()
    links_latest = response_latest.json()["links"]["flickr"]["original"]
    if not links_latest:
        url_to_urls_by_id = f"https://api.spacexdata.com/v5/launches/{id_spaceX}"
        response = requests.get(url_to_urls_by_id)
        response.raise_for_status()
        path_to_urls = response.json()["links"]["flickr"]["original"]


        for img_count, url in enumerate(path_to_urls):
            filename = f"spaceX_{img_count}.jpg"
            download_img(url, filename, folder)  
    else:
        for img_count, url in enumerate(links_latest):
            filename = f"spaceX_{img_count}.jpg"
            download_img(url, filename, folder)


if __name__ == "__main__":
    main()