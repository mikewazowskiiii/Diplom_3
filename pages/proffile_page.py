from pages.base_page import BasePage
import allure
from locators.profile_page_locators import ProfilePageLocators



class ProfilePageBurger(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Кликнуть на 'История заказов' и дождаться появления номера заказа")
    def click_order_history_and_wait(self):
        element = self.driver.find_element(*ProfilePageLocators.BUTTON_ORDER_HISTORY)
        self.click_element(element)
        self.wait_visibility_element(ProfilePageLocators.NUMBER_ORDER)

    @allure.step("Кликнуть на 'Выход' и дождаться перехода на URL: {url}")
    def click_exit(self, url):
        element = self.driver.find_element(*ProfilePageLocators.BUTTON_EXIT)
        self.click_element(element)
        self.wait_to_be(url)

    @allure.step("Найти номер заказа (прокрутить до элемента)")
    def find_number_order(self):
        element = self.driver.find_element(*ProfilePageLocators.NUMBER_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element.text

    @allure.step("Проверить, что текущий URL соответствует URL истории заказов: {expected_url}")
    def check_order_history_url(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step("Проверить, что текущий URL соответствует URL после выхода: {expected_url}")
    def check_exit_url(self, expected_url):
        return self.driver.current_url == expected_url