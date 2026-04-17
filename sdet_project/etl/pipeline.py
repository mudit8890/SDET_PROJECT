import requests
from db.database import get_connection
from config.config import API_URL


def extract():
    """Fetch users from the API."""
    response = requests.get(f"{API_URL}/users")
    response.raise_for_status()
    return response.json()


def transform(users):
    """Keep only the fields we need."""
    return [
        {
            "id":       user["id"],
            "name":     user["name"],
            "email":    user["email"],
            "username": user["username"]
        }
        for user in users
    ]


def load(users):
    """Insert users into PostgreSQL."""
    conn = get_connection()
    cursor = conn.cursor()

    for user in users:
        cursor.execute("""
            INSERT INTO users (id, name, email, username)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (user["id"], user["name"], user["email"], user["username"]))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Loaded {len(users)} users into database.")


def run_pipeline():
    """Run the full ETL pipeline."""
    print("Extracting...")
    raw = extract()

    print("Transforming...")
    users = transform(raw)

    print("Loading...")
    load(users)

    print("Pipeline complete.")
    return users
