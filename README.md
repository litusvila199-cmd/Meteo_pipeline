# 🌦️ Weather ETL Pipeline

An ETL pipeline built with Python that extracts weather data from multiple cities, transforms it using Pandas, and loads the results into both a CSV file and a PostgreSQL database.

---

## Features

- Extract weather data from multiple cities.
- Transform and clean the data.
- Save the processed data as a CSV file.
- Load the data into PostgreSQL.

---

## Technologies

- Python
- Pandas
- Requests
- SQLAlchemy
- PostgreSQL
- python-dotenv

---

## Project Structure

```text
weather-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── config.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

```bash
git clone https://github.com/your-username/weather-pipeline.git

cd weather-pipeline

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file with your API URLs and PostgreSQL credentials.

Example:

```env
URL_BARCELONA=...
URL_MADRID=...
URL_PARIS=...
URL_LONDRES=...
URL_BERLIN=...

DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather_db
DB_USER=litus
DB_PASSWORD=your_password
```

---

## Run

```bash
python src/load.py
```

---

## Output

The pipeline generates:

- `data/processed/weather.csv`
- PostgreSQL table `weather`

---
