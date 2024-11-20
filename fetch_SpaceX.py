
from main_functions import downloading_img


def fetch_spacex_last_launch():
    from main import requests
    json_latest="https://api.spacexdata.com/v5/launches/latest"
    response_latest = requests.get(json_latest)
    response_latest.raise_for_status()
    # json_urls = response.json()
    urls_latest = response_latest.json()["links"]["flickr"]["original"]
    if not urls_latest:
        json_SpaceX = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
        response = requests.get(json_SpaceX)
        response.raise_for_status()
        acess_json_urls = response.json()["links"]["flickr"]["original"]

        for img_count, img_url in enumerate(acess_json_urls):
            directory = "images"
            filename = f"spaceX_{img_count}.jpg"
            url = img_url
            downloading_img(url, filename, directory)
    else:
        for img_count, img_url in enumerate(urls_latest):
            directory = "images"
            filename = f"spaceX_{img_count}.jpg"
            url = img_url
            downloading_img(url, filename, directory)