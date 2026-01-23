import os
from pathlib import Path
from dotenv import load_dotenv
import pcycopg2

# Абсолютный путь к .env
BASE_DIR = Path(__file__).resolve().parent.parent.parent
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)

# Берём переменные из .env
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# print("DB_HOST:", DB_HOST)
# print("DB_USER:", DB_USER)
# print("DB_PASSWORD:", "есть" if DB_PASSWORD else "пусто")

def get_db_connection():
    if None in (DB_HOST, DB_PORT, DB_NAME, DB_USER):
        raise ValueError("Одна из переменных окружения не задана!")

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn



