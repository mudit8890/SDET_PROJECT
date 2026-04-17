import requests
import sys
sys.path.insert(0, '.')
from config.config import API_URL


def test_api_returns_200():
    response = requests.get(f"{API_URL}/users")
    assert response.status_code == 200


def test_api_returns_list():
    response = requests.get(f"{API_URL}/users")
    data = response.json()
    assert isinstance(data, list)


def test_api_returns_10_users():
    response = requests.get(f"{API_URL}/users")
    data = response.json()
    assert len(data) == 10


def test_user_has_required_fields():
    response = requests.get(f"{API_URL}/users")
    user = response.json()[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "username" in user


def test_user_email_format():
    response = requests.get(f"{API_URL}/users")
    for user in response.json():
        assert "@" in user["email"]
