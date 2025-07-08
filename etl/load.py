from etl.transform import transform
import sqlite3
import os

def load():
    df = transform()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "..", "data", "weather_data.db")
    conn = sqlite3.connect(db_path)
    print("Trying to connect to DB at:", os.path.normpath(db_path))
    df.to_sql("weather", conn, if_exists="append", index=False)
    conn.close()

if __name__ == "__main__":
    load()
