# What are common pytest patterns that align with Python best practices?

Here are common pytest patterns that align with Python best practices

## 1. **Arrange-Act-Assert (AAA) Pattern**

Structure each test function into three clear sections:

```python
import pytest

def test_withdraw_raises_when_balance_is_insufficient():
    # Arrange
    account = BankAccount(balance=100)

    # Act & Assert
    with pytest.raises(InsufficientFundsError):
        account.withdraw(200)

    assert account.balance == 100
```

## 2. **`@pytest.fixture` for Shared Setup**

Use fixtures instead of `setUp`/`tearDown` — they compose better and can be shared across files:

```python
import pytest

@pytest.fixture
def db():
    database = Database(":memory:")
    database.create_tables()
    database.seed_test_data()
    yield database       # test runs here
    database.close()     # teardown runs after yield

def test_query_returns_results(db):
    results = db.query("SELECT * FROM users")
    assert len(results) > 0
```

## 3. **Descriptive Test Names**

Names should read like sentences describing expected behavior:

```python
def test_raises_value_error_when_email_is_missing_at_symbol():
    ...
```

Not:

```python
def test_email_bad():
    ...
```

## 4. **One Assertion Concept per Test**

Test one logical behavior per function — not a single assertion, but a single *concept*:

```python
# Good — tests one behavior
def test_sort_returns_list_ascending_by_default():
    result = sort([3, 1, 2])
    assert result == [1, 2, 3]

# Good — tests one behavior (returns a new list, does not mutate)
def test_sort_does_not_mutate_original_list():
    original = [3, 1, 2]
    sort(original)
    assert original == [3, 1, 2]
```

## 5. **Use `pytest.raises` as Context Manager**

Preferred over try/except for testing exceptions. Use the `match` parameter to assert the message:

```python
def test_parse_raises_on_invalid_input():
    with pytest.raises(ValueError, match="invalid"):
        parse("not_a_number")
```

## 6. **`@pytest.mark.parametrize` for Data-Driven Tests**

Avoid copy-pasting tests for multiple inputs:

```python
import pytest

@pytest.mark.parametrize("value, expected", [("0", 0), ("42", 42), ("-5", -5)])
def test_parse_integer(value, expected):
    assert parse(value) == expected
```

## 7. **Mock External Dependencies**

Isolate unit tests from I/O, networks, or databases using `unittest.mock.patch` (safe to use in pytest as a decorator — no `TestCase` class needed):

```python
from unittest.mock import patch

@patch("my_project.api.requests.get")
def test_fetch_user_returns_user_object(mock_get):
    mock_get.return_value.json.return_value = {"id": 1, "name": "Alice"}
    mock_get.return_value.status_code = 200

    user = fetch_user(1)
    assert user.name == "Alice"
    mock_get.assert_called_once_with("https://api.example.com/users/1")
```

## 8. **Test Edge Cases Explicitly**

Boundary conditions, empty inputs, and error paths — use a fixture to share the common object:

```python
import pytest

@pytest.fixture
def empty_list():
    return MyList()

def test_pop_raises_on_empty(empty_list):
    with pytest.raises(IndexError):
        empty_list.pop()

def test_len_is_zero(empty_list):
    assert len(empty_list) == 0

def test_iter_immediately_stops(empty_list):
    assert list(empty_list) == []
```

## 9. **Keep Tests Deterministic**

No random data, no reliance on system time or external state without freezing it:

```python
@freeze_time("2024-01-01")
def test_expired_subscription():
    sub = Subscription(expires="2023-12-31")
    assert sub.is_expired()
```

## 10. **Separate Test Files Mirroring Source**

Tests live in a `tests/` directory with a parallel structure. pytest does not require `__init__.py` files:

```
project/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   └── account.py
│   └── services/
│       └── payment.py
└── tests/
    ├── models/
    │   ├── test_user.py
    │   └── test_account.py
    └── services/
        └── test_payment.py
```
