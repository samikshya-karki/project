

from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class SetupAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.email_input = (By.NAME, "email")
        self.phone_number_input = (By.NAME, "phoneNumber")
        self.password_input = (By.NAME, "password")
        self.confirm_password_input = (By.NAME, "confirmPassword")
        self.next_button = (By.XPATH, "//button[@type='submit' and text()='Next']")

        self.country_code_dropdown = (
            By.XPATH, "//input[@name='phoneNumber']/following-sibling::div//button[@role='combobox']")
        self.show_password_button = (
            By.XPATH, "//input[@name='password']/following-sibling::button")
        self.show_confirm_password_button = (
            By.XPATH, "//input[@name='confirmPassword']/following-sibling::button")
        self.green_password_strength_bars = (
            By.XPATH,
            "//input[@name='password']/parent::div/following-sibling::div//div[contains(@class,'bg-green-500')]")
        self.go_to_login_link = (By.XPATH, "//span[contains(., 'Go to Login')]")

    
    def load_page(self):
        self.open_url(test_data.PAGE_URL)
        return self

    def enter_first_name(self, first_name):
        self.type_text(self.first_name_input, first_name)

    def enter_last_name(self, last_name):
        self.type_text(self.last_name_input, last_name)

    def enter_email(self, email):
        self.type_text(self.email_input, email)

    def enter_phone_number(self, phone_number):
        self.type_text(self.phone_number_input, phone_number)

    def enter_password(self, password):
        self.type_text(self.password_input, password)

    def enter_confirm_password(self, confirm_password):
        self.type_text(self.confirm_password_input, confirm_password)

    def click_show_password(self):
        self.click(self.show_password_button)

    
    def get_password_field_type(self):
        """'password' means hidden, 'text' means visible."""
        return self.get_attribute(self.password_input, "type")

    def get_phone_number_value(self):
        return self.get_value(self.phone_number_input)

    def count_green_password_bars(self):
        return len(self.driver.find_elements(*self.green_password_strength_bars))

    def is_step_open(self, wait_seconds=5):
        return super().is_step_open("personal details", wait_seconds)
    
    def click_next_button(self):
           self.driver.find_element(*self.next_button).click()

    
    def fill_account_details(self, first_name=test_data.FIRST_NAME,
                             last_name=test_data.LAST_NAME,
                             email=None,
                             phone_number=None,
                             password=test_data.VALID_PASSWORD,
                             confirm_password=None):
        email = email or test_data.new_email()
        phone_number = phone_number or test_data.new_phone()
        confirm_password = password if confirm_password is None else confirm_password

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_phone_number(phone_number)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_next_button()
        return self
