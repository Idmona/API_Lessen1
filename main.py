import requests


def get_weather():
    locations = ["Лондон", "Шереметьево", "Череповец"]

    params = {
        "n": "",
        "q": "",
        "T": "",
        "lang": "ru",
        "m": "",
        "M": "",
        "3": ""
    }
    url_template = "https://wttr.in/{}"

    for location in locations:
        response = requests.get(url_template.format(location), params=params)

        if response.status_code == 200:
            print(response.text)

        else:
            print(f"Не удалось получить погоду для {location}")


if __name__ == "__main__":
    get_weather()
