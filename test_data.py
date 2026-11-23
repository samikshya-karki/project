import time
import random

PAGE_URL = "https://authorized-partner.vercel.app/register?step=setup"

FIRST_NAME = "Test"
LAST_NAME = "User"
VALID_PASSWORD = "Qwertyui1!"          
WEAK_PASSWORD = "123"


def new_email():
    """A different email every time so repeated runs do not clash."""
    return f"samikshyakarki478+{int(time.time() * 1000)}@gmail.com"





def new_phone():
    """Generate a random Nepali mobile number."""
    return "984" + str(random.randint(0, 99999999)).zfill(7)


AGENCY_NAME = "Himalayan Education Consultancy"
ROLE_IN_AGENCY = "Director"
AGENCY_EMAIL = "agency.qa@example.com"
AGENCY_WEBSITE = "example.com"
AGENCY_ADDRESS = "Kathmandu, Nepal"

YEARS_OF_EXPERIENCE = "5 years"
STUDENTS_RECRUITED = "100"
FOCUS_AREA = "Undergraduate admissions to Canada"
SUCCESS_METRICS = "90"


BUSINESS_REGISTRATION_NUMBER = "REG-123456"
CERTIFICATION_DETAILS = "ICEF Certified Education Agent"