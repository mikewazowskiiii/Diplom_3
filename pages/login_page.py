from pages.base_page import BasePageBurger
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.forgot_page_locators import ForgotPageLocators
from data import DataAuthorization



class LoginPageBurger(BasePageBurger):
    # клик по ссылке "Восстановить пароль"
    def click_recover_password_and_wait_clickable(self):
        element = self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD)
        self.click_element(element)
        self.wait_element_and_clickable(ForgotPageLocators.RECOVER_PASSWORD_BUTTON)

    def login_user_and_wait_element_clickable(self):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(DataAuthorization.LOGIN)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(DataAuthorization.PASS)
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        self.click_element(element)
        self.wait_element_and_clickable(MainPageLocators.INGREDIENT_BUN)

    def click_go_to_constructor(self):
        element = self.driver.find_element(*LoginPageLocators.P_KONSTRUCTOR)
        self.click_element(element)