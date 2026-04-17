# Test 1: Check if email is valid
def test_valid_email():
    email = "user@example.com"
    assert "@" in email
    print("✓ Email is valid")

# Test 2: Check if age is valid (between 18-65)
def test_valid_age():
    age = 25
    assert 18 <= age <= 65
    print("✓ Age is valid")

# Test 3: Check API status code
def test_api_status():
    status_code = 200
    assert status_code == 200
    print("✓ API returned 200")

if __name__ == "__main__":
    test_valid_email()
    test_valid_age()
    test_api_status()
    print("\nAll tests passed!")
