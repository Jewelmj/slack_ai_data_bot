import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn


def run_query(sql):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows