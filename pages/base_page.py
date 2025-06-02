from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageBurger:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, element):
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def open_page_and_wait_visibility(self, url, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def open_page_and_wait_clickable(self, url, locator):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def wait_to_be(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def wait_element_and_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def wait_displayed_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_loading(self, locator):
        self.wait_visibility_element(locator)
        self.wait_invisibility(locator)