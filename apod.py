
from main_functions import get_extension_of_file, downloading_img


def give_URL_APOD(api_key):
    from main import requests
    
    params = {
         "count":50
    }


    full_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    response_APOD = requests.get(full_url, params=params)
    response_APOD.raise_for_status()
    for index_img, img in enumerate(response_APOD.json()):
        url = img['url']
        directory = "images"
        response = requests.get(url)
        response.raise_for_status()
        extension = get_extension_of_file(url)
        filename = f'nasa_apod_{index_img}{extension[0]}'
        downloading_img(url,filename, directory)

