from locators import Locators
from helpers import generate_email, generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_login_by_login_button(self, driver):
        email = generate_email()
        password = generate_password()

        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*Locators.NAME_INPUT).send_keys("Нелли")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
        driver.get("https://stellarburgers.education-services.ru/login")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  

        

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()