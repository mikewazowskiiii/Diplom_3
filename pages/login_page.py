from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.forgot_page_locators import ForgotPageLocators
from data import DataAuthorization
from data import DataUrl



class LoginPageBurger(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Клик на ссылку 'Восстановить пароль' и ожидание кликабельности кнопки восстановления")
    def click_recover_password_and_wait_clickable(self):
        element = self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD)
        self.click_element(element)
        self.wait_element_and_clickable(ForgotPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step("Логин пользователя и ожидание кликабельности элемента 'Булки'")
    def login_user_and_wait_element_clickable(self):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(DataAuthorization.LOGIN)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(DataAuthorization.PASS)
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        self.click_element(element)
        self.wait_element_and_clickable(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Клик на ссылку 'Конструктор'")
    def click_go_to_constructor(self):
        element = self.driver.find_element(*LoginPageLocators.P_KONSTRUCTOR)
        self.click_element(element)

    @allure.step("Проверка, что текущий URL соответствует URL конструктора")
    def check_constructor_url(self):
        return self.driver.current_url == DataUrl.BASE_URL + DataUrl.CONSTRUCTOR

    @allure.step("Проверка, что текущий URL соответствует URL восстановления пароля")
    def check_forgot_password_url(self):
        return self.driver.current_url == DataUrl.BASE_URL + DataUrl.FORGOT_PASS




