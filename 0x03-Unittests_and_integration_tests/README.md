# GitHub Org Client - Python Testing Project

This project explores **unit and integration testing** techniques in Python. It focuses on mocking external APIs, using fixtures, measuring code coverage, and building robust test suites using `unittest`, `parameterized`, and `mock`.

## 📁 Project Structure

- [`utils.py`](./utils.py): Helper functions including `get_json`, `access_nested_map`, and `memoize`.
- [`client.py`](./client.py): The main class `GithubOrgClient` which interacts with GitHub's REST API to fetch org and repo data.
- [`test_utils.py`](./test_utils.py): Unit tests for utility functions.
- [`test_client.py`](./test_client.py): Unit and integration tests for `GithubOrgClient`.
- [`fixtures.py`](./fixtures.py) Contains mocked payloads used for integration testing.

## 🧪 Features Tested

- `access_nested_map()` function for deeply nested dicts
- Mocking HTTP calls via `requests.get`
- Memoization with method-to-property transformation
- Patch decorators and context managers
- Integration test using real-world style data fixtures
- License filtering logic (`has_license`)
- Use of `@parameterized.expand` and `@parameterized_class`

## ✅ Requirements

- Python 3.7+
- `parameterized==0.7.4`
- `pycodestyle==2.5.0`

To install the dependencies:
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, run:
```bash
pip install parameterized==0.7.4 pycodestyle==2.5.0
```

## 🧼 Code Quality

To verify your code style (PEP 8):
```bash
pycodestyle .
```

## 🧠 Documentation Checklist

- All **modules**, **classes**, and **functions** include docstrings explaining their purpose.
- Type annotations are present on all functions.
- Example command to verify a docstring:
  ```bash
  python3 -c 'from client import GithubOrgClient; print(GithubOrgClient.__doc__)'
  ```

## 🚀 Running the Tests

To run all unit and integration tests:
```bash
python3 -m unittest discover
```

To run tests by file:
```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```

## 🔍 Additional Tips

- Be sure to include an executable header (`#!/usr/bin/env python3`) at the top of `.py` files.
- Add an empty newline at the end of each Python file.
- Use `memoize` to avoid redundant API calls.
- Validate mock calls with `assert_called_once_with(...)` and `PropertyMock` where appropriate.

## 💡 Author

Created as part of the ALX backend Python track.  
Maintained by: Eyuel

