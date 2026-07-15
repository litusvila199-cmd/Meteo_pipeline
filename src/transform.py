import json
from pathlib import Path

import pandas as pd


def transform_weather():
    files = Path("data/raw").glob("*.json")

    dfs = []

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        hourly = data["hourly"]

        df = pd.DataFrame(hourly)

        # Transformaciones
        df["time"] = pd.to_datetime(df["time"])
        df["city"] = file.stem.capitalize()

        df.rename(
            columns={
                "temperature_2m": "temperature",
                "relative_humidity_2m": "humidity",
                "wind_speed_10m": "wind_speed",
            },
            inplace=True,
        )

        # Guardamos el DataFrame de esa ciudad
        dfs.append(df)

    # Unimos todos los DataFrames
    df_final = pd.concat(dfs, ignore_index=True)

    return df_final


def main():
    df = transform_weather()

    print(df.head())
    print()
    df.info()


if __name__ == "__main__":
    main()
