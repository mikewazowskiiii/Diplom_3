from pages.base_page import BasePageBurger
from locators.forgot_page_locators import ForgotPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from data import DataAuthorization


class ForgotPageBurger(BasePageBurger):
    # ввод значения почты и нажатие на кнопку "Восстановить"
    def input_email(self):
        self.driver.find_element(*ForgotPageLocators.RECOVER_EMAIL_INPUT).send_keys(DataAuthorization.LOGIN)

    def click_button_forgot(self):
        element = self.driver.find_element(*ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        self.click_element(element)

    # шаг восстановления пароля
    def entering_password_recovery_email(self):
        self.input_email()
        self.click_button_forgot()
        self.wait_element_and_clickable(ResetPasswordPageLocators.EYE_BUTTON)