from locators import Locators
from helpers import generate_email, generate_password

class TestPersonalAccount:
    def test_go_topersonal_account(self, driver):
        email=generate_email()
        password=generate_password()
        
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("Нелли")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
        personal_account=driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        assert personal_account.is_displayed()    