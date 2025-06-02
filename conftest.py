import pytest
from selenium import webdriver


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.fullscreen_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()