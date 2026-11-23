from pages.agency_details_page import AgencyDetailsPage
from pages.email_verification_page import EmailVerificationPage
from pages.professional_experience_page import ProfessionalExperiencePage
from pages.setup_account_page import SetupAccountPage
from pages.verification_page import VerificationPage
from selenium.webdriver.common.by import By

import test_data
from email_otp import get_otp


def register_user(driver):

    setup_account_page = SetupAccountPage(driver)
    setup_account_page.load_page().fill_account_details()
    
    otp = get_otp()
    email_verification_page = EmailVerificationPage(driver)
    email_verification_page.enter_otp(otp)

    email_verification_page.click_verify_button()


    agency_details_page = AgencyDetailsPage(driver)
    agency_details_page.fill_agency_details()

    professional_experience_page = ProfessionalExperiencePage(driver)
    professional_experience_page.fill_experience_details()

    verification_page = VerificationPage(driver)
    verification_page.upload_document(test_data.DOCUMENT_FILE_PATH)
    verification_page.click_submit()


def test_register_user(driver):
    register_user(driver)