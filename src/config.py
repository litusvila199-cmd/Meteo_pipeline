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


db = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_PORT": os.getenv("DB_PORT"),
    "DB_NAME": os.getenv("DB_NAME"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASSWORD": os.getenv("DB_PASSWORD"),
}