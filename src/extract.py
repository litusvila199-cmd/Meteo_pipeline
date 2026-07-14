import requests
import json
from config import cities



def get_weather(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_raw_data(city, data):
    filename = f"data/raw/{city.lower()}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():

    for city, url in cities.items():
        try:

            data = get_weather(url)
            save_raw_data(city, data)
            print(f"{city} guardado.")
        except requests.RequestException as e:
            print(f"Error en {city}: {e}")

                
if __name__ == "__main__":
    main()               