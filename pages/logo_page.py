from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import URL
import allure

class LogoPage(BasePage):
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    ORDER_UPPER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")


    @allure.step('Кликаем по кнопке "Заказать" вверху')
    def click_order_button(self):
        self.click(self.ORDER_UPPER_BUTTON)

    @allure.step('Кликаем по лого Самоката')
    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step('Кликаем по лого Яндекса')
    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)

    @allure.step('Ожидаем пока изменится страница на Дзен')
    def wait_for_url_changes_dzen(self):
        self.wait_url_changes(URL.DZEN_PAGE)

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')

    @allure.step('Кликаем на кнопка Зказать для перехода на другу страницу и клик на лого самоката, чтобы вернуться обратно домой')
    def click_order_and_click_logo_scooter_back(self):
        self.click_order_button()
        self.click_logo_scooter()


