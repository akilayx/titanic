from src.db.connection import get_db_connection

# Создаём соединение с PostgreSQL
conn = get_db_connection()

# Создаём курсор для выполнения запросов
cur = conn.cursor()

# Проверяем соединение: имя базы и пользователь
cur.execute("SELECT current_database(), current_user;")
print(cur.fetchone())

# Закрываем курсор и соединение
cur.close()
conn.close()
