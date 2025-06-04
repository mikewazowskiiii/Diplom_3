from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPageBurger
from pages.forgot_page import ForgotPageBurger
from pages.reset_password_page import ResetPasswordPageBurger
from conftest import driver
import allure
from data import DataUrl


class TestRecoverPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password(self, driver):
        login = LoginPageBurger(driver)
        login.open_page(DataUrl.BASE_URL + DataUrl.LOGIN_URL)
        login.click_recover_password_and_wait_clickable()
        assert login.check_forgot_password_url()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_go_to_reset_password(self, driver):
        login = LoginPageBurger(driver)
        forgot = ForgotPageBurger(driver)
        login.open_page_and_wait_visibility(DataUrl.BASE_URL + DataUrl.LOGIN_URL, LoginPageLocators.LOGIN_BUTTON)
        login.click_recover_password_and_wait_clickable()
        forgot.entering_password_recovery_email()
        assert forgot.check_reset_password_url()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_click_eye_button(self, driver):
        login = LoginPageBurger(driver)
        forgot = ForgotPageBurger(driver)
        reset = ResetPasswordPageBurger(driver)
        login.open_page(DataUrl.BASE_URL + DataUrl.LOGIN_URL)
        login.click_recover_password_and_wait_clickable()
        forgot.entering_password_recovery_email()
        reset.click_eye_button()
        active = reset.active_input()
        assert active.is_displayed() is True