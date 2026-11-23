from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmailVerificationPage:

    def __init__(self, driver):
        self.driver = driver

    OTP_FIELD = (
        By.CSS_SELECTOR,
        "input[data-input-otp='true']"
    )

    def enter_otp(self, otp):

        otp_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.OTP_FIELD)
        )

        otp_input.send_keys(otp)

        return self

    def click_verify_button(self):
        verify_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and normalize-space()='Verify Code']"
)
        verify_button.click()