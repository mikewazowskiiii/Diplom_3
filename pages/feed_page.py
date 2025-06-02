from pages.base_page import BasePageBurger
from locators.feed_page_locators import FeedPageLocators


class FeedPageBurger(BasePageBurger):
    def click_order_and_wait(self):
        element = self.driver.find_element(*FeedPageLocators.LIST_ORDER)
        self.click_element(element)
        self.wait_element_and_clickable(FeedPageLocators.HEAD_STRUCTURE)

    def window_order(self):
        element = self.driver.find_element(*FeedPageLocators.WINDOW_ORDER)
        return element

    def find_number_order(self):
        order_list = []
        elements = self.driver.find_elements(*FeedPageLocators.LIST_ORDER)
        for i in elements:
            order_list.append(i.text)
        return order_list

    def find_all_and_today_counter(self, locator):
        elements = self.driver.find_element(*locator)
        return elements.text

    def click_constructor(self):
        element = self.driver.find_element(*FeedPageLocators.P_KONSTRUCTOR)
        self.click_element(element)

    def find_order_in_work(self):
        elements = self.driver.find_element(*FeedPageLocators.ORDER_IN_WORK)
        return elements.text