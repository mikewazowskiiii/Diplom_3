from pages.base_page import BasePageBurger
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPageBurger(BasePageBurger):
    def click_personal_account(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        self.click_element(element)

    def click_personal_account_and_wait(self, url):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        self.click_element(element)
        self.wait_to_be(url)

    def click_personal_account_and_wait_clickable(self, locator):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        self.click_element(element)
        self.wait_element_and_clickable(locator)

    def click_feed_order_and_wait(self):
        element = self.driver.find_element(*MainPageLocators.ORDER_FEED_2)
        self.click_element(element)
        self.wait_element_and_clickable(FeedPageLocators.LIST_ORDER)

    def click_feed_order_and_wait_displayed(self):
        element = self.driver.find_element(*MainPageLocators.ORDER_FEED_2)
        self.click_element(element)
        self.wait_displayed_element(FeedPageLocators.ORDER_IN_WORK)

    def click_ingredient_and_wait_visibility(self):
        element = self.driver.find_element(*MainPageLocators.INGREDIENT_SAUSE)
        self.click_element(element)
        self.wait_visibility_element(MainPageLocators.IMG_INGREDIENT)

    def open_window_ingredient(self):
        element = self.driver.find_element(*MainPageLocators.IMG_INGREDIENT)
        return element

    def visible_price(self):
        element = self.driver.find_element(*MainPageLocators.PRICE_INGREDIENT)
        return element

    def close_window_ingredient_and_wait_visibility(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_BUTTON)
        self.click_element(element)
        self.wait_visibility_element(MainPageLocators.PRICE_INGREDIENT)

    def drag_and_drop_souse(self):
        souse = self.driver.find_element(*MainPageLocators.INGREDIENT_SAUSE)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, souse, bun_cons)

    def up_counter(self):
        element = self.driver.find_element(*MainPageLocators.COUNTER_INGREDIENT)
        return element

    def click_register_order_and_wait(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_REGISTER_ORDER)
        self.click_element(element)
        self.wait_visibility_element(MainPageLocators.NUMBER_ORDER_HEAD)
        self.wait_loading(MainPageLocators.IMG_LOADING)

    def drag_and_drop_bun_and_wait_text(self):
        bun = self.driver.find_element(*MainPageLocators.INGREDIENT_BUN)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, bun, bun_cons)
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(MainPageLocators.PRICE_INGREDIENT, '1976'))

    def order_is_made(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER_WINDOW)
        return element

    def close_window_order_succesfull(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_BUTTON_ORDER)
        self.click_element(element)

    def find_number_order(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER)
        return f'0{element.text}'

    # шаг заказ
    def create_order(self):
        self.drag_and_drop_bun_and_wait_text()
        self.click_register_order_and_wait()
        self.close_window_order_succesfull()