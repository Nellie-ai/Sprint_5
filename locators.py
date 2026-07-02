from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON=(By.XPATH,".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON=(By.XPATH,".//p[text()='Личный Кабинет']")
    REGISTER_BUTTON=(By.XPATH,".//a[contains(text(),'Зарегистрироваться')]")
    NAME_INPUT=(By.XPATH,".//input[@name='name']")
    EMAIL_INPUT=(By.XPATH,".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT=(By.XPATH,".//label[text()='Пароль']/following-sibling::input")
    REGISTER_SUBMIT_BUTTON=(By.XPATH,".//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_SUBMIT_BUTTON=(By.XPATH,".//button[text()='Войти']")
    ERROR_PASSWORD=(By.XPATH,".//p[text()='Некорректный пароль']")
    FORGOT_PASSWORD_BUTTON=(By.XPATH,".//a[text()='Восстановить пароль']")
    CONSTRUCTOR_BUTTON=(By.XPATH,".//p[text()='Конструктор']")
    LOGO=(By.XPATH,".//div[contains(@class,'AppHeader_header__logo')]")
    LOGOUT_BUTTON=(By.XPATH,".//button[text()='Выход']")
    BUNS_SECTION=(By.XPATH,".//span[text()='Булки']")
    SAUCES_SECTION=(By.XPATH,".//span[text()='Соусы']")
    FILLINGS_SECTION=(By.XPATH,".//span[text()='Начинки']") 