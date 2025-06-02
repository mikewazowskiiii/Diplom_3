from selenium.webdriver.common.by import By


class FeedPageLocators:
    LAST_ORDER = [By.XPATH, ".//main/div/div/ul/li[1]"] # последний заказ
    HEAD_STRUCTURE = [By.XPATH, ".//p[text() = 'Cостав']"] # заголовок "состав"
    WINDOW_ORDER = [By.CSS_SELECTOR, ".Modal_orderBox__1xWdi"]

    LIST_ORDER = [By.XPATH, ".//ul/li/a/div[1]/p[1]"] # 50 последних заказов

    COUNTER_ALL_ORDERS = [By.XPATH, ".//div[contains(@class,'undefined')]/p[contains(@class,'OrderFeed_number__2MbrQ')]"] # количество заказов за всё время
    COUNTER_TODAY_ORDERS = [By.XPATH, "//div[3]/p[contains(@class,'OrderFeed_number__2MbrQ')]"] # количество заказов за день

    P_KONSTRUCTOR = [By.XPATH, ".//p[text() = 'Конструктор']"]  # ссылка "Конструктор"

    ORDER_IN_WORK = [By.XPATH, ".//ul[2]/li[contains(@class,'text_type_digits-default')]"] # заказ в работе