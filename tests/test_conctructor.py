from locators import Locators
from helpers import generate_email,generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor:
    def test_go_to_constructor(self, driver):
        email=generate_email()
        password=generate_password()

        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("Нелли")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        constructor=driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        assert constructor.is_displayed()

    def test_go_to_sauces_section(self, driver):
        driver.get("http://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.SAUCES_SECTION).click()
        sauses=driver.find_element(*Locators.SAUCES_ACTIVE)
        assert sauses.is_displayed()

    def test_go_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        fillings=driver.find_element(*Locators.FILLINGS_ACTIVE)
        assert fillings.is_displayed()

    def test_go_to_buns_sections(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        buns = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUNS_ACTIVE))
        assert buns.is_displayed()            