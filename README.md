# Authorized Partner - Selenium QA (Page Object Model)

Tests for the 4-step registration: https://authorized-partner.vercel.app/register?step=setup

## Folder structure

```
authorized_partner_tests/
├── pages/                                  <- HOW to talk to each page
│   ├── base_page.py                        shared helpers (type, click, dropdown, checkbox)
│   ├── setup_account_page.py               Step 1 - Set up your Account
│   ├── agency_details_page.py              Step 2 - Agency Details
│   ├── professional_experience_page.py     Step 3 - Professional Experience
│   └── verification_page.py                Step 4 - Verification and Preferences
├── tests/                                  <- WHAT we check
│   ├── test_step1_setup_account.py
│   ├── test_step2_agency_details.py
│   ├── test_step3_professional_experience.py
│   └── test_step4_verification.py
├── test_data.py                            sample values used by the tests
├── conftest.py                             opens Chrome, "go to step N" fixtures
├── pytest.ini
├── requirements.txt
└── screenshots/                            saved automatically when a test fails
```

## The idea in one line

Tests never touch locators. They call readable methods, for example:

```python
setup_account_page.fill_account_details()
setup_account_page.click_next()
```

If the website changes, fix the locator once in the page class and every test keeps working.

## How locators are named

Each page class lists its locators at the top, with names a human can read:

```python
self.first_name_input = (By.NAME, "firstName")
self.region_of_operation_dropdown = (By.XPATH, "//label[...]/following-sibling::button")
self.career_counseling_checkbox = self.checkbox_with_label("Career Counseling")
```

The site's `id` values (like `_r_7m_-form-item`) change on every page load, so
the stable `name` attribute or the label text is used instead.

## Run

```
pip install -r requirements.txt
pytest                                           # everything
pytest tests/test_step1_setup_account.py         # one step only
pytest -k "back_button"                          # tests with this word in the name
```

Chrome must be installed. Selenium 4.6+ downloads the driver by itself.
To run without a browser window, remove the `#` before the `--headless=new` line in `conftest.py`.

## Things to know

- Each test starts from Step 1 and fills the earlier steps by itself, so tests are independent (but slower).
- Step 1 uses a new email like `qa.test+1732...@example.com` on every run.
- No test submits valid data on Step 4, so no real account is created.
- Dropdowns on this site are custom (not a normal `<select>`). The code assumes the
  list items have `role="option"`, which is the standard for this kind of dropdown.
- Tests marked "possible bug" are expected to FAIL if the bug is real:
  - names made only of digits ("11") accepted
  - negative number of students accepted
  - success metrics above 100% accepted
  - label "Test Prepration" is missing an 'a'
