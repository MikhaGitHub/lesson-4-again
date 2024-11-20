from main_functions import downloading_img


def get_url_from_Epic(api_key):
    from main import requests
    epic_json = f"https://api.nasa.gov/EPIC/api/natural/?api_key={api_key}"
    epic_json_response = requests.get(epic_json)
    epic_json_response.raise_for_status()
    for img_count, img in enumerate(epic_json_response.json()):
        img_identifier = img["image"]
        img_date = str(img["date"])
        img_date_split = img_date.split()[0]
        symbol = '-'
        for string in img_date_split:
            if string == symbol:
                url_date = img_date_split.replace(string, '/')

        url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{img_identifier}.png?api_key={api_key}'
        print(url)
        filename = f'epic_{img_count}.png'
        directory = "images"
        downloading_img(url,filename,directory)