from pathlib import Path
import os
import requests


def download_img(url,filename, folder, payload=None):
    response = requests.get(url, params=payload, stream=True)
    response.raise_for_status()
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    with open(filepath, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def get_extension_of_file(url):
    extension_file = os.path.splitext(url)
    url = extension_file[0]
    extension = extension_file[1]
    return extension, url