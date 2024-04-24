from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

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


    def set_name_input(self, name):
        name_input = self.wait_and_find_element(self.NAME_INPUT)
        name_input.send_keys(name)

    def set_surname_input(self, surname):
        surname_input = self.wait_and_find_element(self.SURNAME_INPUT)
        surname_input.send_keys(surname)

    def set_address_input(self, address):
        address_input = self.wait_and_find_element(self.ADDRESS_INPUT)
        address_input.send_keys(address)

    def click_metro_field(self):
        self.driver.find_element(*self.METRO_INPUT).click()

    def choose_metro(self, metro):
        metro_station = self.wait_and_find_element(metro)
        metro_station.click()

    def set_phone_input(self, phone):
        phone_input = self.wait_and_find_element(self.PHONE_INPUT)
        phone_input.send_keys(phone)

    def click_date_field(self):
        self.driver.find_element(*self.DATE_OF_ORDER).click()

    def set_date_input(self, date):
        date_input = self.wait_and_find_element(self.DATE_OF_ORDER)
        date_input.send_keys(date)

    def click_header_about_rent(self):
        self.driver.find_element(*self.ABOUT_RENT_HEADER).click()

    def click_period_order(self):
        self.driver.find_element(*self.PERIOD_OF_ORDER).click()

    def choose_period_order(self):
        self.driver.find_element(*self.HOW_LONG_ORDER).click()

    def set_comment_input(self, comment):
        date_input = self.wait_and_find_element(self.COMMENT)
        date_input.send_keys(comment)

    def press_button_order(self):
        self.driver.find_element(*self.ORDER_MIDDLE_BUTTON).click()

    def press_button_yes(self):
        self.driver.find_element(*self.BUTTON_YES).click()

    @allure.step('Нажимаем финальное "Заказать", подтверждаем действие "Да')
    def press_buttons_order_and_yes(self):
        self.press_button_order()
        self.press_button_yes()

    @allure.step('Выбираем срок аренды самоката и вставляем комментарий по желанию')
    def click_and_choose_period_add_comment(self, comment):
        self.click_period_order()
        self.choose_period_order()
        self.set_comment_input(comment)

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону')
    def click_and_set_date(self,date):
        self.click_date_field()
        self.set_date_input(date)
        self.click_header_about_rent()

    @allure.step('Выбираем нажную станцию метро и заполняем соответствующее поле номером телефона')
    def choose_metro_set_phone(self, metro, phone):
        self.click_metro_field()
        self.choose_metro(metro)
        self.set_phone_input(phone)
    @allure.step('Передаем в соответствующие поля имя, фамилию и адрес заказа')
    def set_details_data(self, name, surname, address):
        self.set_name_input(name)
        self.set_surname_input(surname)
        self.set_address_input(address)