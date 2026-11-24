import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import test_data
from pages.base_page import BasePage


class VerificationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        
        self.business_registration_number_input = (
            By.NAME, "business_registration_number"
        )

        self.certification_details_input = (
            By.NAME, "certification_details"
        )

        self.preferred_countries_dropdown = (
            By.XPATH,
            "//label[normalize-space()='Preferred Countries']/following-sibling::button"
        )

        
        self.universities_checkbox = self.checkbox_with_label(
            "Universities"
        )

        self.colleges_checkbox = self.checkbox_with_label(
            "Colleges"
        )

        self.vocational_school_checkbox = self.checkbox_with_label(
            "Vocational School"
        )

        self.other_institution_checkbox = self.checkbox_with_label(
            "Other"
        )

        
        self.document_file_inputs = (
            By.XPATH, "//input[@type='file']"
        )

        self.add_documents_button = (
            By.XPATH, "//button[contains(., 'Add Documents')]"
        )

        
        self.submit_button = (
            By.XPATH,
            "//button[normalize-space()='Submit']"
        )

    def enter_business_registration_number(self, number):
        self.type_text(
            self.business_registration_number_input,
            number
        )

    def enter_certification_details(self, details):
        self.type_text(
            self.certification_details_input,
            details
        )

    def choose_preferred_country(self, country_name=None):
        self.select_from_dropdown(
            self.preferred_countries_dropdown,
            country_name
        )

    def upload_document(self, file_path):

        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        
        file_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                self.document_file_inputs
            )
        )

        
        file_inputs[0].send_keys(
            os.path.abspath(file_path)
        )

        self.pause(1)

        print("Document uploaded successfully:", file_path)

    def click_add_documents(self):
        self.click(self.add_documents_button)

    def click_submit(self):
        self.click(self.submit_button)
        self.pause(2)

        print("Verification form submitted")

    def get_preferred_countries_text(self):
        return self.find(
            self.preferred_countries_dropdown
        ).text

    def is_submit_button_visible(self):
        return self.is_displayed(
            self.submit_button
        )

    def is_step_open(self, wait_seconds=5):
        return super().is_step_open(
            "Provide Business Details",
            wait_seconds
        )

    def fill_verification_details(
        self,
        registration_number=test_data.BUSINESS_REGISTRATION_NUMBER,
        certification=test_data.CERTIFICATION_DETAILS
    ):

        self.enter_business_registration_number(
            registration_number
        )

        self.choose_preferred_country()

        self.tick_checkbox(
            self.universities_checkbox
        )

        self.enter_certification_details(
            certification
        )

        return self