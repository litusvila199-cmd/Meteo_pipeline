import pandas as pd
import json

with open("data/raw/barcelona.json", "r", encoding="utf-8") as f:
    data = json.load(f)

hourly = data["hourly"]

df = pd.DataFrame(hourly)

print(df.head())

df["time"] = pd.to_datetime(df["time"])

print(df.info())
