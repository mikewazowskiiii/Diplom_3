from pages.base_page import BasePage
import allure
from locators.forgot_page_locators import ForgotPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from data import DataAuthorization
from data import DataUrl


class ForgotPageBurger(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Вводим email для восстановления пароля")
    def input_email(self):
        self.driver.find_element(*ForgotPageLocators.RECOVER_EMAIL_INPUT).send_keys(DataAuthorization.LOGIN)

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_button_forgot(self):
        element = self.driver.find_element(*ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        self.click_element(element)

    @allure.step("Вводим email и нажимаем кнопку 'Восстановить', ждем кликабельности кнопки показа пароля")
    def entering_password_recovery_email(self):
        self.input_email()
        self.click_button_forgot()
        self.wait_element_and_clickable(ResetPasswordPageLocators.EYE_BUTTON)

    @allure.step("Проверяем, что перешли на страницу сброса пароля")
    def check_reset_password_url(self):
        return self.driver.current_url == DataUrl.BASE_URL + DataUrl.RESET_PASS