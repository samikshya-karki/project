
# Authorized Partner - Selenium Automation

Automated testing of the Authorized Partner registration process using Python, Selenium, and Pytest.

## Project Structure

```text
project/
├── pages/
├── tests/
├── test_data.py
├── email_otp.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Tools Used
- Python
- Selenium
- Pytest
- Gmail IMAP for OTP verification

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

## Notes
- Uses Page Object Model (POM).
- Automates the registration process.
- Retrieves OTP from Gmail.
- Uses a new email for each test run.
- `.env` stores credentials and is excluded from GitHub.
