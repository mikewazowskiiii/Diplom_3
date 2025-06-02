from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.feed_page import FeedPageBurger
from pages.proffile_page import ProfilePageBurger
from locators.feed_page_locators import FeedPageLocators
from conftest import driver
import allure
import pytest
import time
from data import DataUrl


class TestOrderFeed:

    @allure.title("Eсли кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_details_order(self, driver):
        feed = FeedPageBurger(driver)
        feed.open_page_and_wait_visibility(DataUrl.BASE_URL + DataUrl.FEED, FeedPageLocators.COUNTER_ALL_ORDERS)
        feed.click_order_and_wait()
        structure = feed.window_order()
        assert structure.is_displayed() is True

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_user_in_feed_order(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)
        profile = ProfilePageBurger(driver)
        login.open_page(DataUrl.BASE_URL + DataUrl.LOGIN_URL)
        login.login_user_and_wait_element_clickable()
        main.create_order()
        main.click_personal_account_and_wait(DataUrl.BASE_URL + DataUrl.PROFILE)
        profile.click_order_history_and_wait()
        number_order_main = profile.find_number_order()
        main.click_feed_order_and_wait()
        number_order_feed = feed.find_number_order()
        assert number_order_main in number_order_feed

    @allure.title("При создании нового заказа счётчик Выполнено за всё время/ Выполнено за сегодня увеличивается")
    @pytest.mark.parametrize(
        'locator',
        [
            FeedPageLocators.COUNTER_ALL_ORDERS,
            FeedPageLocators.COUNTER_TODAY_ORDERS
        ]
    )
    def test_counter_all_up_and_today(self, locator, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)
        login.open_page(DataUrl.BASE_URL + DataUrl.LOGIN_URL)
        login.login_user_and_wait_element_clickable()
        main.click_feed_order_and_wait()
        first_count = feed.find_all_and_today_counter(locator)
        feed.click_constructor()
        main.create_order()
        main.click_feed_order_and_wait()
        time.sleep(2)
        last_count = feed.find_all_and_today_counter(locator)
        assert last_count > first_count

    @allure.title("После оформления заказа его номер появляется в разделе В работе.")
    def test_order_in_work(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)
        login.open_page(DataUrl.BASE_URL + DataUrl.LOGIN_URL)
        login.login_user_and_wait_element_clickable()
        main.drag_and_drop_bun_and_wait_text()
        main.click_register_order_and_wait()
        number_order = main.find_number_order()
        main.close_window_order_succesfull()
        main.click_feed_order_and_wait_displayed()
        number_order_feed = feed.find_order_in_work()
        assert number_order == number_order_feed