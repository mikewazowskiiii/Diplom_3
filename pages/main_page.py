from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
from data import DataUrl
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPageBurger(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_personal_account(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        self.click_element(element)

    @allure.step("Кликнуть на кнопку 'Личный кабинет' и дождаться перехода на URL: {url}")
    def click_personal_account_and_wait(self, url):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        self.click_element(element)
        self.wait_to_be(url)

    @allure.step("Проверить, что текущий URL соответствует: {expected_url}")
    def check_personal_account_url(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step("Кликнуть на кнопку 'Личный кабинет' и дождаться кликабельности элемента: {locator}")
    def click_personal_account_and_wait_clickable(self, locator):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        self.click_element(element)
        self.wait_element_and_clickable(locator)

    @allure.step("Кликнуть на 'Ленту заказов' и дождаться появления списка заказов")
    def click_feed_order_and_wait(self):
        element = self.driver.find_element(*MainPageLocators.ORDER_FEED_2)
        self.click_element(element)
        self.wait_element_and_clickable(FeedPageLocators.LIST_ORDER)

    @allure.step("Проверить, что текущий URL соответствует URL 'Ленты заказов'")
    def check_feed_order_url(self):
        return self.driver.current_url == DataUrl.BASE_URL + DataUrl.FEED

    @allure.step("Кликнуть на 'Ленту заказов' и дождаться отображения элемента 'В работе'")
    def click_feed_order_and_wait_displayed(self):
        element = self.driver.find_element(*MainPageLocators.ORDER_FEED_2)
        self.click_element(element)
        self.wait_displayed_element(FeedPageLocators.ORDER_IN_WORK)

    @allure.step("Кликнуть на ингредиент (соус) и дождаться отображения окна ингредиента")
    def click_ingredient_and_wait_visibility(self):
        element = self.driver.find_element(*MainPageLocators.INGREDIENT_SAUSE)
        self.click_element(element)
        self.wait_visibility_element(MainPageLocators.IMG_INGREDIENT)

    @allure.step("Получить элемент окна ингредиента")
    def open_window_ingredient(self):
        element = self.driver.find_element(*MainPageLocators.IMG_INGREDIENT)
        return element

    @allure.step("Получить элемент цены ингредиента")
    def visible_price(self):
        element = self.driver.find_element(*MainPageLocators.PRICE_INGREDIENT)
        return element

    @allure.step("Кликнуть на кнопку закрытия окна ингредиента и дождаться его скрытия")
    def close_window_ingredient_and_wait_visibility(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_BUTTON)
        self.click_element(element)
        self.wait_visibility_element(MainPageLocators.PRICE_INGREDIENT)

    @allure.step("Перетащить ингредиент (соус) в конструктор")
    def drag_and_drop_souse(self):
        souse = self.driver.find_element(*MainPageLocators.INGREDIENT_SAUSE)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, souse, bun_cons)

    @allure.step("Получить элемент счетчика ингредиента")
    def up_counter(self):
        element = self.driver.find_element(*MainPageLocators.COUNTER_INGREDIENT)
        return element

    @allure.step("Кликнуть на кнопку 'Оформить заказ' и дождаться появления номера заказа")
    def click_register_order_and_wait(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_REGISTER_ORDER)
        self.click_element(element)
        self.wait_visibility_element(MainPageLocators.NUMBER_ORDER_HEAD)
        self.wait_loading(MainPageLocators.IMG_LOADING)

    @allure.step("Перетащить ингридиент (булка) в конструктор и дождаться отображения текста цены")
    def drag_and_drop_bun_and_wait_text(self):
        bun = self.driver.find_element(*MainPageLocators.INGREDIENT_BUN)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, bun, bun_cons)
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(MainPageLocators.PRICE_INGREDIENT, '1976'))

    @allure.step("Получить элемент окна с номером заказа")
    def order_is_made(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER_WINDOW)
        return element

    @allure.step("Закрыть окно успешного оформления заказа")
    def close_window_order_succesfull(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_BUTTON_ORDER)
        self.click_element(element)

    @allure.step("Получить номер заказа")
    def find_number_order(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER)
        return f'0{element.text}'

    @allure.step("Создать заказ: перетащить булку, оформить заказ, закрыть окно")
    def create_order(self):
        self.drag_and_drop_bun_and_wait_text()
        self.click_register_order_and_wait()
        self.close_window_order_succesfull()