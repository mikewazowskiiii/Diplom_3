from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    # страница восстановления пароля
    RECOVER_PASSWORD_INPUT = [By.XPATH, ".//input[@name = 'Введите новый пароль']"]
    EYE_BUTTON = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]
    ACTIVE_RECOVER_INPUT = [By.XPATH, ".//label[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]"]