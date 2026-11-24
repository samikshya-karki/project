
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
1. clone the repository 
2. create a .env file at the root of the repo and set environment credentials as per .env.example(you will need a valid email address and your app password for email address)

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
python -m pytest tests/register.py -v
```

## Notes
- Uses Page Object Model (POM).
- Automates the registration process.
- Retrieves OTP from Gmail.
- Uses a new email for each test run.
- `.env` stores credentials and is excluded from GitHub.
