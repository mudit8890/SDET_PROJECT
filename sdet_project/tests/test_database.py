import sys
sys.path.insert(0, '.')
from db.database import get_connection, clear_users
from etl.pipeline import transform, extract, load


def test_db_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()


def test_users_table_exists():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_name = 'users'
        )
    """)
    exists = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    assert exists is True


def test_insert_and_query_user(clean_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (id, name, email, username) VALUES (%s, %s, %s, %s)",
        (999, "Test User", "test@example.com", "testuser")
    )
    conn.commit()

    cursor.execute("SELECT name, email FROM users WHERE id = 999")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    assert row[0] == "Test User"
    assert row[1] == "test@example.com"


def test_clear_users(clean_db):
    users = transform(extract())
    load(users)
    clear_users()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    assert count == 0
