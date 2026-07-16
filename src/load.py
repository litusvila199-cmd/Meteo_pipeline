from transform import transform_weather
from config import db 
from sqlalchemy import create_engine

def save_csv(df):
    df.to_csv("data/processed/weather.csv", index=False)

    print("Datos guardados correctamente en data/processed/weather.csv")

def save_postgres(df):
    conection_string = (
        f"postgresql://{db['DB_USER']}:{db['DB_PASSWORD']}@{db['DB_HOST']}:{db['DB_PORT']}/{db['DB_NAME']}"
    ) 

    engine = create_engine(conection_string)

    df.to_sql(
        name="weather",
        con=engine,
        if_exists="replace",
        index=False
    )

    engine.dispose()

    print("Datos guardados correctamente en PostgreSQL.")

       


def load_weather(df):
    save_csv(df)
    save_postgres(df)


if __name__ == "__main__":
    df = transform_weather()
    load_weather(df)        