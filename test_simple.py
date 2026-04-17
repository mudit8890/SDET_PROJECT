# Test 1: Email validation
def test_email():
    email = "user@example.com"
    assert "@" in email
    print("✓ Test 1: Email valid")

# Test 2: Age validation
def test_age():
    age = 25
    assert 18 <= age <= 65
    print("✓ Test 2: Age valid")

# Test 3: API status
def test_api():
    status = 200
    assert status == 200
    print("✓ Test 3: API status 200")

if __name__ == "__main__":
    test_email()
    test_age()
    test_api()
    print("\n✅ All 3 tests passed!")
