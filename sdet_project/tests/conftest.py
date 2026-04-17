import pytest
import sys
sys.path.insert(0, '.')
from db.database import setup_database, clear_users


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    """Create tables once before all tests."""
    setup_database()


@pytest.fixture
def clean_db():
    """Clear users table before each test that needs it."""
    clear_users()
    yield
    clear_users()
