from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.proffile_page import ProfilePageBurger
from conftest import driver
import allure
from data import DataUrl
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver):
        main = MainPageBurger(driver)
        main.open_page_and_wait_visibility(DataUrl.BASE_URL, MainPageLocators.ELEMENT_BUN)
        main.click_personal_account()
        assert main.check_personal_account_url(DataUrl.BASE_URL + DataUrl.LOGIN_URL)

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver):
        main = MainPageBurger(driver)
        login = LoginPageBurger(driver)
        profile = ProfilePageBurger(driver)
        main.open_page_and_wait_visibility(DataUrl.BASE_URL, MainPageLocators.ELEMENT_BUN)
        main.click_personal_account()
        login.login_user_and_wait_element_clickable()
        main.click_personal_account_and_wait_clickable(ProfilePageLocators.BUTTON_ORDER_HISTORY)
        profile.click_order_history_and_wait()
        assert profile.check_order_history_url(DataUrl.BASE_URL + DataUrl.ORDER_HISTORY)

    @allure.title("Выход из аккаунта")
    def test_go_to_exit(self, driver):
        main = MainPageBurger(driver)
        login = LoginPageBurger(driver)
        profile = ProfilePageBurger(driver)
        main.open_page_and_wait_visibility(DataUrl.BASE_URL + DataUrl.LOGIN_URL, LoginPageLocators.LOGIN_BUTTON)
        login.login_user_and_wait_element_clickable()
        main.click_personal_account_and_wait_clickable(ProfilePageLocators.BUTTON_EXIT)
        profile.click_exit(DataUrl.BASE_URL + DataUrl.LOGIN_URL)
        assert profile.check_exit_url(DataUrl.BASE_URL + DataUrl.LOGIN_URL)