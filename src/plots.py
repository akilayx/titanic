import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.db.connection import get_db_connection


def run_sql(sql_path: Path) -> pd.DataFrame:
    with open(sql_path, "r", encoding="utf-8") as f:
        query = f.read()

    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df


def main():
    sql_dir = Path("sql")
    sql_files = sorted(sql_dir.glob("*.sql"))

    for sql_file in sql_files:
        print(f"\n=== Выполняется {sql_file.name} ===")

        df1 = run_sql(sql_file)

        print(df1.head())
        print("Колонки:", list(df1.columns))

        if df1.shape[1] == 1:
            plt.bar([df1.columns[0]], [df1.iloc[0, 0]])
            plt.ylabel(df1.columns[0])

        elif df1.shape[1] == 2:
            plt.bar(df1.iloc[:, 0], df1.iloc[:, 1])
            plt.xlabel(df1.columns[0])
            plt.ylabel(df1.columns[1])

        elif df1.shape[1] >= 3:
            plt.bar(df1.iloc[:, 1], df1.iloc[:, 2])
            plt.xlabel(df1.columns[1])
            plt.ylabel(df1.columns[2])

        plt.title(sql_file.name)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()



