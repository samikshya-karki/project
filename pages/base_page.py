
import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


SCREENSHOT_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "screenshots"
)


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.step_heading = (By.XPATH, "//h3")
        self.error_messages = (
            By.XPATH,
            "//*[contains(@class,'destructive')]"
        )

        self.first_dropdown_option = (
            By.XPATH,
            "(//div[contains(@class,'cursor-pointer')])[1]"
        )

        self.back_button = (
            By.XPATH,
            "//button[normalize-space()='Back']"
        )

        self.next_button = (
            By.XPATH,
            "//button[normalize-space()='Next']"
        )

    def open_url(self, url):

        self.driver.get(url)

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input"))
        )

    def pause(self, seconds=1.5):

        time.sleep(seconds)

    def take_screenshot(self, name):

        os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

        self.driver.save_screenshot(
            os.path.join(SCREENSHOT_FOLDER, f"{name}.png")
        )

    def find(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def is_displayed(self, locator):

        found = self.driver.find_elements(*locator)

        return len(found) > 0 and found[0].is_displayed()

    def type_text(self, locator, text):

        field = self.find(locator)

        field.clear()
        field.send_keys(text)

    def click(self, locator):

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def click_next(self):

        self.click(self.next_button)
        self.pause()

    def click_back(self):

        self.click(self.back_button)
        self.pause()

    def get_value(self, locator):

        return self.find(locator).get_attribute("value")

    def get_attribute(self, locator, attribute_name):

        return self.find(locator).get_attribute(attribute_name)

    def get_page_text(self):

        return self.driver.find_element(
            By.TAG_NAME, "body"
        ).text

    def get_step_heading(self):

        for heading in self.driver.find_elements(*self.step_heading):

            if heading.is_displayed() and heading.text.strip():

                return heading.text.strip()

        return ""

    def get_error_messages(self):

        messages = []

        for element in self.driver.find_elements(*self.error_messages):

            if element.is_displayed() and element.text.strip():

                messages.append(element.text.strip())

        return messages

    def is_step_open(self, heading_text, wait_seconds=5):

        try:

            WebDriverWait(
                self.driver,
                wait_seconds
            ).until(
                lambda d: heading_text.lower()
                in self.get_step_heading().lower()
            )

            return True

        except TimeoutException:

            return False

    def checkbox_with_label(self, label_text):

        return (
            By.XPATH,
            f"//label[normalize-space()='{label_text}']"
            "/preceding-sibling::button[@role='checkbox']"
        )

    def tick_checkbox(self, checkbox_locator):

        checkbox = self.find(checkbox_locator)

        if checkbox.get_attribute("aria-checked") != "true":

            checkbox.click()

    def untick_checkbox(self, checkbox_locator):

        checkbox = self.find(checkbox_locator)

        if checkbox.get_attribute("aria-checked") == "true":

            checkbox.click()

    def is_checkbox_ticked(self, checkbox_locator):

        return (
            self.find(checkbox_locator).get_attribute("aria-checked")
            == "true"
        )

    def select_from_dropdown(self, dropdown_locator, option_text=None):

        self.click(dropdown_locator)

        if option_text:

            option = (
                By.XPATH,
                f"//div[contains(@class,'cursor-pointer')]"
                f"[.//span[normalize-space()='{option_text}']]"
            )

        else:

            option = self.first_dropdown_option

        self.click(option)

        self.pause(0.5)

        print("Selected dropdown option:", option_text)
