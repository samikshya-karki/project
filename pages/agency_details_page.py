
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class AgencyDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.agency_name_input = (By.NAME, "agency_name")
        self.role_in_agency_input = (By.NAME, "role_in_agency")
        self.agency_email_input = (By.NAME, "agency_email")
        self.agency_website_input = (By.NAME, "agency_website")
        self.agency_address_input = (By.NAME, "agency_address")
        self.next_button = (By.XPATH, "//button[type='Submit']")

        
        self.region_of_operation_dropdown = (
            By.XPATH, "//label[normalize-space()='Region of Operation']/following-sibling::button")

    
    def enter_agency_name(self, agency_name):
        self.type_text(self.agency_name_input, agency_name)

    def enter_role_in_agency(self, role):
        self.type_text(self.role_in_agency_input, role)

    def enter_agency_email(self, email):
        self.type_text(self.agency_email_input, email)

    def enter_agency_website(self, website):
        self.type_text(self.agency_website_input, website)

    def enter_agency_address(self, address):
        self.type_text(self.agency_address_input, address)

    def choose_region_of_operation(self, region_name=None):
    
        self.select_from_dropdown(self.region_of_operation_dropdown, region_name)

    
    def get_selected_region_text(self):
        return self.find(self.region_of_operation_dropdown).text

    def is_step_open(self, wait_seconds=5):
        return super().is_step_open("About your Agency", wait_seconds)

    def click_next_button(self):
       self.driver.find_element(*self.next_button).click()

    
    def fill_agency_details(self, agency_name=test_data.AGENCY_NAME,
        role=test_data.ROLE_IN_AGENCY,
        email=test_data.AGENCY_EMAIL,
        address=test_data.AGENCY_ADDRESS,
        website=test_data.AGENCY_WEBSITE,
        region=None):
        self.enter_agency_name(agency_name)
        self.enter_role_in_agency(role)
        self.enter_agency_email(email)
        self.enter_agency_website(website)
        self.enter_agency_address(address)
        self.choose_region_of_operation(region)
        self.click_next_button()
        return self
