from pages.base_page import BasePage
import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPageBurger(BasePage):

    @allure.step("Клик по кнопке 'глаз'")
    def click_eye_button(self):
        element = self.driver.find_element(*ResetPasswordPageLocators.EYE_BUTTON)
        self.driver.execute_script("arguments[0].style.visibility = 'visible';", element)
        element.click()

    @allure.step("Получение активного элемента после клика по кнопке 'глаз'")
    def active_input(self):
        self.driver.find_element(*ResetPasswordPageLocators.EYE_BUTTON).click()
        active = self.driver.find_element(*ResetPasswordPageLocators.EYE_BUTTON)
        return active