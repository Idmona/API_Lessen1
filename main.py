import requests


def get_weather(location):
    params = {
        "n": "",
        "q": "",
        "T": "",
        "lang": "ru",
        "m": "",
        "M": "",
        "3": ""
    }
    url = f"https://wttr.in/{location}"
    response = requests.get(url, params=params)
    return response.text if response.ok else f"Не удалось получить погоду для {location}"


def main():
    locations = ["Лондон", "Шереметьево", "Череповец"]
    for location in locations:
        print(get_weather(location))


if __name__ == "__main__":
    main()
