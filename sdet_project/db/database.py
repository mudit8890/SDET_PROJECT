import psycopg2
from config.config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id        INTEGER PRIMARY KEY,
            name      VARCHAR(100),
            email     VARCHAR(100),
            username  VARCHAR(100)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database setup complete.")


def clear_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    cursor.close()
    conn.close()
