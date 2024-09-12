from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from data import ITEMS

class OrderPage(BasePage):

    ORDER_UPPER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_MIDDLE_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Заказать']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    BUTTON_YES = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    CONFIRMATION_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")
    NAME_INPUT = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@class='select-search__input']")
    METRO_CHERKIZOVSKAYA = (By.XPATH, "//button[@value='2']")
    METRO_PREOBRAZHENKA = (By.XPATH, "//button[@value='3']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    ABOUT_RENT_HEADER = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    DATE_OF_ORDER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_OF_ORDER = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    HOW_LONG_ORDER = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    COMMENT = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")

    @allure.step('Кликаем по кнопке "Заказать" вверху')
    def click_order_button(self):
        self.click(self.ORDER_UPPER_BUTTON)

    @allure.step('Находим поле Имя и помещаем туда значение')
    def set_name_input(self, name):
        name_input = self.wait_and_find_element(self.NAME_INPUT)
        name_input.send_keys(name)

    @allure.step('Находим поле Фамилия и помещаем туда значение')
    def set_surname_input(self, surname):
        surname_input = self.wait_and_find_element(self.SURNAME_INPUT)
        surname_input.send_keys(surname)

    @allure.step('Находим поле Адрес и помещаем туда значение')
    def set_address_input(self, address):
        address_input = self.wait_and_find_element(self.ADDRESS_INPUT)
        address_input.send_keys(address)

    @allure.step('Кликаем по полю Метро')
    def click_metro_field(self):
        self.wait_and_find_element(self.METRO_INPUT).click()

    @allure.step('Выбираем и кликаем по конкретной станции метро')
    def choose_metro(self, metro):
        metro_station = self.wait_and_find_element(metro)
        metro_station.click()

    @allure.step('Находим поле Телефон и помещаем туда значение')
    def set_phone_input(self, phone):
        phone_input = self.wait_and_find_element(self.PHONE_INPUT)
        phone_input.send_keys(phone)

    @allure.step('Кликаем по кнопке Далее')
    def click_page_button_next(self):
        self.click(self.NEXT_BUTTON)

    @allure.step('Находим и кликаем по полю Дата заказа')
    def click_date_field(self):
        self.wait_and_find_element(self.DATE_OF_ORDER).click()

    @allure.step('Заполняем поле дата')
    def set_date_input(self, date):
        date_input = self.wait_and_find_element(self.DATE_OF_ORDER)
        date_input.send_keys(date)

    @allure.step('Кликаем в сторону, чтобы убрать выпадающий календарь')
    def click_header_about_rent(self):
        self.wait_and_find_element(self.ABOUT_RENT_HEADER).click()

    @allure.step('Находим и кликаем по полю Срок аренды')
    def click_period_order(self):
        self.wait_and_find_element(self.PERIOD_OF_ORDER).click()

    @allure.step('Выбираем срок аренды')
    def choose_period_order(self):
        self.wait_and_find_element(self.HOW_LONG_ORDER).click()

    @allure.step('Находим поле Комментарий для курьера и вводим его')
    def set_comment_input(self, comment):
        date_input = self.wait_and_find_element(self.COMMENT)
        date_input.send_keys(comment)

    @allure.step('Находим кнопку Заказать под формой и кликаем по ней')
    def press_button_order(self):
        self.wait_and_find_element(self.ORDER_MIDDLE_BUTTON).click()

    @allure.step('Находим кнопку Да и кликаем по ней')
    def press_button_yes(self):
        self.wait_and_find_element(self.BUTTON_YES).click()

    @allure.step('Нажимаем финальное "Заказать", подтверждаем действие "Да')
    def press_buttons_order_and_yes(self):
        self.press_button_order()
        self.press_button_yes()

    @allure.step('Находим кнопку подтверждения с искомым текстом')
    def confirmation_button_present(self):
        return self.find_text(self.CONFIRMATION_BUTTON)

    @allure.step('Выбираем срок аренды самоката и вставляем комментарий по желанию, набор 1')
    def click_and_choose_period_add_comment_1(self):
        self.click_period_order()
        self.choose_period_order()
        self.set_comment_input(ITEMS.COMMENT_2)

    @allure.step('Выбираем срок аренды самоката и вставляем комментарий по желанию, набор 2')
    def click_and_choose_period_add_comment_2(self):
        self.click_period_order()
        self.choose_period_order()
        self.set_comment_input(ITEMS.COMMENT_1)

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону, набор 1')
    def click_and_set_date_1(self):
        self.click_date_field()
        self.set_date_input(ITEMS.DATE_1)
        self.click_header_about_rent()

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону, набор 2')
    def click_and_set_date_2(self):
        self.click_date_field()
        self.set_date_input(ITEMS.DATE_2)
        self.click_header_about_rent()

    @allure.step('Выбираем нужную станцию метро и заполняем соответствующее поле номером телефона, набор 1')
    def choose_metro_set_phone_1(self):
        self.click_metro_field()
        self.choose_metro(self.METRO_PREOBRAZHENKA)
        self.set_phone_input(ITEMS.PHONE_NUMBER_1)

    @allure.step('Выбираем нужную станцию метро и заполняем соответствующее поле номером телефона, набор 2')
    def choose_metro_set_phone_2(self):
        self.click_metro_field()
        self.choose_metro(self.METRO_CHERKIZOVSKAYA)
        self.set_phone_input(ITEMS.PHONE_NUMBER_2)
    @allure.step('Передаем в соответствующие поля имя, фамилию и адрес заказа набор 1')
    def set_details_data_1(self):
        self.set_name_input(ITEMS.NAME_1)
        self.set_surname_input(ITEMS.SURNAME_1)
        self.set_address_input(ITEMS.ADDRESS_1)

    @allure.step('Передаем в соответствующие поля имя, фамилию и адрес заказа набор 2')
    def set_details_data_2(self):
        self.set_name_input(ITEMS.NAME_2)
        self.set_surname_input(ITEMS.SURNAME_2)
        self.set_address_input(ITEMS.ADDRESS_2)