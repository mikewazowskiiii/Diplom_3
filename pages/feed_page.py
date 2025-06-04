from pages.base_page import BasePage
import allure
from locators.feed_page_locators import FeedPageLocators


class FeedPageBurger(BasePage):

    @allure.step("Кликнуть на заказ и дождаться загрузки структуры заказа")
    def click_order_and_wait(self):
        element = self.driver.find_element(*FeedPageLocators.LIST_ORDER)
        self.click_element(element)
        self.wait_element_and_clickable(FeedPageLocators.HEAD_STRUCTURE)

    @allure.step("Получить элемент окна заказа")
    def window_order(self):
        element = self.driver.find_element(*FeedPageLocators.WINDOW_ORDER)
        return element

    @allure.step("Получить список номеров заказов")
    def find_number_order(self):
        order_list = []
        elements = self.driver.find_elements(*FeedPageLocators.LIST_ORDER)
        for i in elements:
            order_list.append(i.text)
        return order_list

    @allure.step("Найти и получить текст счетчика 'Всего заказов' или 'Заказов за сегодня'")
    def find_all_and_today_counter(self, locator):
        elements = self.driver.find_element(*locator)
        return elements.text

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        element = self.driver.find_element(*FeedPageLocators.P_KONSTRUCTOR)
        self.click_element(element)

    @allure.step("Найти и получить текст заказа в разделе 'В работе'")
    def find_order_in_work(self):
        elements = self.driver.find_element(*FeedPageLocators.ORDER_IN_WORK)
        return elements.text