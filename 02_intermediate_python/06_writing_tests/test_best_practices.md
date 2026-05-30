# What are common unittest patterns that align with Python best practices?

Here are common unittest patterns that align with Python best practices

## 1. **Arrange-Act-Assert (AAA) Pattern**

Structure each test method into three clear sections:

```python
def test_withdraw_insufficient_balance(self):
    # Arrange
    account = BankAccount(balance=100)
    
    # Act
    with self.assertRaises(InsufficientFundsError):
        account.withdraw(200)
    
    # Assert
    self.assertEqual(account.balance, 100)
```

## 2. **`setUp` and `tearDown` for Fixtures**

Avoid repeating setup logic across tests:

```python
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.create_tables()
        self.db.seed_test_data()
    
    def tearDown(self):
        self.db.close()
```

## 3. **Descriptive Test Names**

Names should read like sentences describing expected behavior:

```python
def test_raises_value_error_when_email_is_missing_at_symbol(self):
    ...
```

Not:

```python
def test_email_bad(self):
    ...
```

## 4. **One Assertion Concept per Test**

Test one logical behavior per method — not a single assertion, but a single *concept*:

```python
# Good — tests one behavior
def test_sort_returns_list_ascending_by_default(self):
    result = sort([3, 1, 2])
    self.assertEqual(result, [1, 2, 3])

# Good — tests one behavior (returning new list, not mutating)
def test_sort_does_not_mutate_original_list(self):
    original = [3, 1, 2]
    result = sort(original)
    self.assertEqual(original, [3, 1, 2])
```

## 5. **Use `assertRaises` as Context Manager**

Preferred over try/except for testing exceptions:

```python
with self.assertRaises(ValueError) as ctx:
    parse("not_a_number")

self.assertIn("invalid", str(ctx.exception))
```

## 6. **`subTest` for Data-Driven Tests**

Avoid copy-pasting tests for multiple inputs:

```python
def test_parse_integer(self):
    for value, expected in [("0", 0), ("42", 42), ("-5", -5)]:
        with self.subTest(value=value):
            self.assertEqual(parse(value), expected)
```

## 7. **Mock External Dependencies**

Isolate unit tests from I/O, networks, or databases:

```python
@patch("my_project.api.requests.get")
def test_fetch_user_returns_user_object(self, mock_get):
    mock_get.return_value.json.return_value = {"id": 1, "name": "Alice"}
    mock_get.return_value.status_code = 200
    
    user = fetch_user(1)
    self.assertEqual(user.name, "Alice")
    mock_get.assert_called_once_with("https://api.example.com/users/1")
```

## 8. **Test Edge Cases Explicitly**

Boundary conditions, empty inputs, and error paths:

```python
class TestEmptyList(unittest.TestCase):
    def setUp(self):
        self.list = MyList()
    
    def test_pop_raises_on_empty(self):
        with self.assertRaises(IndexError):
            self.list.pop()
    
    def test_len_is_zero(self):
        self.assertEqual(len(self.list), 0)
    
    def test_iter_immediately_stops(self):
        self.assertEqual(list(self.list), [])
```

## 9. **Keep Tests Deterministic**

No random data, no reliance on system time or external state without freezing it:

```python
@freeze_time("2024-01-01")
def test_expired_subscription(self):
    sub = Subscription(expires="2023-12-31")
    self.assertTrue(sub.is_expired())
```

## 10. **Separate Test Files Mirroring Source**

Tests live in a `tests/` directory with a parallel structure:

```
project/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   └── account.py
│   └── services/
│       └── payment.py
└── tests/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   ├── test_user.py
    │   └── test_account.py
    └── services/
        ├── __init__.py
        └── test_payment.py
```
