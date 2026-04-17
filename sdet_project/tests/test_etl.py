import sys
sys.path.insert(0, '.')
from etl.pipeline import extract, transform, load
from db.database import get_connection


def test_extract_returns_data():
    data = extract()
    assert len(data) > 0


def test_transform_keeps_required_fields():
    raw = extract()
    users = transform(raw)
    for user in users:
        assert "id" in user
        assert "name" in user
        assert "email" in user
        assert "username" in user


def test_transform_removes_extra_fields():
    raw = extract()
    users = transform(raw)
    for user in users:
        assert "address" not in user
        assert "phone" not in user


def test_load_inserts_into_db(clean_db):
    users = transform(extract())
    load(users)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    assert count == len(users)


def test_full_pipeline(clean_db):
    from etl.pipeline import run_pipeline
    users = run_pipeline()
    assert len(users) == 10
