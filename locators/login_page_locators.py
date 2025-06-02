from selenium.webdriver.common.by import By


class LoginPageLocators:
    # страница логина
    RECOVER_PASSWORD = [By.XPATH, ".//a[text() = 'Восстановить пароль']"] # ссылка "Восстановить пароль"
    LOGIN_BUTTON = [By.XPATH, ".//button[text() = 'Войти']"] # кнопка "Войти"

    INPUT_EMAIL = [By.XPATH, ".//label[text() = 'Email']/../input"] # инпут почты
    INPUT_PASSWORD = [By.XPATH, ".//label[text() = 'Пароль']/../input"] # инпут пароля

    P_KONSTRUCTOR = [By.XPATH, ".//p[text() = 'Конструктор']"]  # ссылка "Конструктор"