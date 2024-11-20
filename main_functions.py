
from pathlib import Path


def downloading_img(url,filename, directory):
    from main import requests
    Path(f"/{directory}").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    
    with open(f'{directory}/{filename}', 'wb') as file:
        file.write(response.content)


def get_extension_of_file(url):
    from main import os
    extension_file = os.path.splitext(url)
    url = extension_file[0]
    extension = extension_file[1]
    return extension, url