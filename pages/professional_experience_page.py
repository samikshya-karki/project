

from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class ProfessionalExperiencePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        
        self.years_of_experience_dropdown = (
            By.XPATH, "//label[normalize-space()='Years of Experience']/following-sibling::button")

        
        self.students_recruited_input = (By.NAME, "number_of_students_recruited_annually")
        self.focus_area_input = (By.NAME, "focus_area")
        self.success_metrics_input = (By.NAME, "success_metrics")

       
        self.career_counseling_checkbox = self.checkbox_with_label("Career Counseling")
        self.admission_applications_checkbox = self.checkbox_with_label("Admission Applications")
        self.visa_processing_checkbox = self.checkbox_with_label("Visa Processing")
        self.test_preparation_checkbox = self.checkbox_with_label("Test Prepration")

   
    def choose_years_of_experience(self, years_text=None):
        """Example text: '5 years'. No text given = pick the first option."""
        self.select_from_dropdown(self.years_of_experience_dropdown, years_text)

    def enter_students_recruited(self, number):
        self.type_text(self.students_recruited_input, number)

    def enter_focus_area(self, focus_area):
        self.type_text(self.focus_area_input, focus_area)

    def enter_success_metrics(self, percent):
        self.type_text(self.success_metrics_input, percent)

    
    def get_years_of_experience_text(self):
        return self.find(self.years_of_experience_dropdown).text

    def is_step_open(self, wait_seconds=5):
        return super().is_step_open("Experience and Performance Metrics", wait_seconds)

    
    def fill_experience_details(self, years_text=test_data.YEARS_OF_EXPERIENCE,
                                students_recruited=test_data.STUDENTS_RECRUITED,
                                focus_area=test_data.FOCUS_AREA,
                                success_metrics=test_data.SUCCESS_METRICS,
                                tick_a_service=True):
        self.choose_years_of_experience(years_text)
        self.enter_students_recruited(students_recruited)
        self.enter_focus_area(focus_area)
        self.enter_success_metrics(success_metrics)
        if tick_a_service:
            self.tick_checkbox(self.career_counseling_checkbox)
        return self
