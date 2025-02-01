from main_functions import download_img
import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Скачивает изображения из запусков SpaceX.")
    parser.add_argument('--folder', default="images", help="Папка для сохранения изображений.")
    parser.add_argument('--id', default="5eb87d42ffd86e000604b384", help="ID запуска SpaceX (если не последний).")
    args = parser.parse_args()

    url_latest = "https://api.spacexdata.com/v5/launches/latest"
    try:
        response = requests.get(url_latest)
        response.raise_for_status()
        links = response.json()["links"]["flickr"]["original"]
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных последнего запуска: {e}")
        return

    if not links:
        url = f"https://api.spacexdata.com/v5/launches/{args.id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            links = response.json()["links"]["flickr"]["original"]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении данных для ID запуска {args.id}: {e}")
            return

    for count, url in enumerate(links):
        filename = f"spaceX_{count}.jpg"
        download_img(url, filename, args.folder)

if __name__ == "__main__":
    main()