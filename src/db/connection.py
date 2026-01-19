import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # загружаем .env

def get_db_connection():
    """
    Возвращает соединение с PostgreSQL
    """
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
# Пример использования
# conn = get_db_connection()        