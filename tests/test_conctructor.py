from locators import Locators
from helpers import generate_email,generate_password

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