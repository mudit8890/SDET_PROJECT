# Simple Data Validation Tests

# Test 1: User data should have all fields
def test_user_data():
    user = {"id": 1, "name": "John", "email": "john@example.com"}
    assert user["id"] == 1
    assert user["name"] == "John"
    assert user["email"] == "john@example.com"
    print("✓ Test 1: User data correct")

# Test 2: Order amount should be positive
def test_order_amount():
    order_amount = 100
    assert order_amount > 0
    print("✓ Test 2: Order amount positive")

# Test 3: Email should have @
def test_email_format():
    email = "user@example.com"
    assert "@" in email
    print("✓ Test 3: Email format correct")

if __name__ == "__main__":
    test_user_data()
    test_order_amount()
    test_email_format()
    print("\n✅ All 3 data validation tests passed!")
