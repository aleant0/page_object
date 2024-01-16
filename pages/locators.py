from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="login_submit"]')

    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSCONF = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_TITLE = (By.CSS_SELECTOR, '.alertinner>strong')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong ')
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
