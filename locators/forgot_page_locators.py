from selenium.webdriver.common.by import By


class ForgotPageLocators:
    # страница ввода почты
    RECOVER_EMAIL_INPUT = [By.XPATH, ".//input[@name = 'name']"] # инпут почты
    RECOVER_PASSWORD_BUTTON = [By.XPATH, ".//button[text() = 'Восстановить']"] # кнопка "Восстановить"