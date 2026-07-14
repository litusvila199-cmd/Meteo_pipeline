from dotenv import load_dotenv
import os 

load_dotenv()

cities = {
    "Barcelona": os.getenv("URL_BARCELONA"),
    "Madrid": os.getenv("URL_MADRID"),
    "Paris": os.getenv("URL_PARIS"),
    "Londres": os.getenv("URL_LONDRES"),
    "Berlin": os.getenv("URL_BERLIN"),
}