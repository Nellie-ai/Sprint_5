from locators import Locators
from helpers import generate_email,generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Registration:
   def test_successful_registration(self, driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    driver.find_element(*Locators.NAME_INPUT).send_keys("Нелли")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
    login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON))
    assert login_button.is_displayed()
   def test_incorrect_password(self, driver):
    driver.get("https://stellarburgers.education-services.ru//")
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    driver.find_element(*Locators.NAME_INPUT).send_keys("Нелли")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
          
    error=driver.find_element(*Locators.ERROR_PASSWORD)
    assert error.is_displayed()

    
    