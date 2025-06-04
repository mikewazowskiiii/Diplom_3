import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу по URL: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Кликаем по элементу")
    def click_element(self, element):
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step("Открываем страницу по URL: {url} и ждем видимости элемента: {locator}")
    def open_page_and_wait_visibility(self, url, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Открываем страницу по URL: {url} и ждем кликабельности элемента: {locator}")
    def open_page_and_wait_clickable(self, url, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Ждем видимости элемента: {locator}")
    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ждем, пока URL станет: {url}")
    def wait_to_be(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Ждем кликабельности элемента: {locator}")
    def wait_element_and_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Ждем отображения элемента: {locator}")
    def wait_displayed_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ждем, пока элемент станет невидимым: {locator}")
    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Ждем загрузки страницы: ждем видимости и исчезновения элемента {locator}")
    def wait_loading(self, locator):
        self.wait_visibility_element(locator)
        self.wait_invisibility(locator)