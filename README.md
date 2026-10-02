# SauceDemo UI Autotests

UI autotests for [SauceDemo](https://www.saucedemo.com/) implemented with Python, Selenium, and pytest.


## Test coverage

- Login with the standard user and verification that the products page is opened and products are displayed.
- Logout for valid SauceDemo users with verification that the login page is displayed after logout.


## Requirements

- Python 3.10 or newer
- Google Chrome

Tests run locally in Google Chrome. No Docker or additional services are required.
ChromeDriver is managed automatically by Selenium.

## Installation

Clone the repository:

```bash
git clone https://github.com/DariaGorskaya/saucedemo-autotests.git
```
```bash
cd saucedemo-autotests
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```


## Running tests

Run all tests:

```bash
python -m pytest
```

Run only the login test:

```bash
python -m pytest tests/test_login.py
```

Run all logout test cases:

```bash
python -m pytest tests/test_logout.py
```

Run the logout test for a specific user, for example `standard_user`:

```bash
python -m pytest tests/test_logout.py -k standard_user
```


## Code quality

Run Ruff:

```bash
python -m ruff check .
```

Run mypy:

```bash
python -m mypy .
```

mypy runs in strict mode as configured in `pyproject.toml`.