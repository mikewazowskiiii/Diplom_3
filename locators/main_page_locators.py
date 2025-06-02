from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_PROFILE = [By.XPATH, ".//p[text() = 'Личный Кабинет']"] # личный кабинет
    BUTTON_PROFILE_2 = [By.CSS_SELECTOR, ".AppHeader_header__linkText__3q_va"]
    ELEMENT_BUN = [By.XPATH, ".//h2[text() = 'Булки']"] # заголовок "Булки

    P_KONSTRUCTOR = [By.XPATH, ".//p[text() = 'Конструктор']"]  # ссылка "Конструктор"
    ORDER_FEED = [By.XPATH, ".//p[text() = 'Лента Заказов']"] # ссылка "Лента заказов"
    ORDER_FEED_2 = [By.XPATH, ".//nav/ul/li[2]/a[contains(@class, 'AppHeader_header__link__3D_hX')]/p"]
    HEAD_DETAIL_ING = [By.XPATH, ".//h2[text() = 'Детали ингредиента']"] # заголовок "Детали ингредиента"

    IMG_LOADING = [By.CSS_SELECTOR, ".Modal_modal__loading__3534A"] # подгрузка

    CLOSE_BUTTON = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened__3ISw4')]//button"] # кнопка "закрыть" у ингредиента
    CLOSE_BUTTON_ORDER = [By.CSS_SELECTOR, ".Modal_modal__close__TnseK"] # кнопка "Закрыть" у эурана успеха заказа
    COUNTER_INGREDIENT_NULL = [By.XPATH, ".//ul[2]/a[1]//p[@class = 'counter_counter__num__3nue1'][text() = '0']"] # нулевой каунтер третьего ингредиента
    INGREDIENT_BUN = [By.XPATH, "//img[@alt = 'Флюоресцентная булка R2-D3']"] # Булка :3
    COUNTER_INGREDIENT = [By.XPATH, ".//ul[2]/a[1]//p[@class = 'counter_counter__num__3nue1'][text() = '1']"] # ненулевой каунтер
    INGREDIENT_SAUSE = [By.XPATH, ".//img[@alt = 'Соус Spicy-X']"] # ингредиент - соус
    BUN_CONSTRUCTOR = [By.XPATH, ".//span[text() = 'Перетяните булочку сюда (верх)']"] # конструктор булочки
    BUTTON_REGISTER_ORDER = [By.XPATH, ".//button[text() = 'Оформить заказ']"] # кнопка "оформить заказ"

    NUMBER_ORDER_HEAD = [By.XPATH, ".//p[text() = 'идентификатор заказа']"] #заголовок "идентификатор заказа"
    NUMBER_ORDER_WINDOW = [By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_"] #окно "заказ"
    NUMBER_ORDER = [By.XPATH, ".//div/h2[contains(@class, 'Modal_modal__title__2L34m')]"] # номер заказа

    IMG_INGREDIENT = [By.XPATH, "//section[1]/div[1]/div/div[contains(@class , 'undefined')]"]
    PRICE_INGREDIENT = [By.CSS_SELECTOR, ".text_type_digits-medium"] # локатор цены ингредиента