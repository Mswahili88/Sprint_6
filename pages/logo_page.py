from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class LogoPage(BasePage):
    HOME_HEADER = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    ORDER_UPPER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_UPPER_BUTTON)

    def click_logo_scooter(self):
        self.driver.find_element(*self.LOGO_SCOOTER)

    @allure.step('Кликаем по лого Яндекса')
    def click_logo_yandex(self):
        self.driver.find_element(*self.LOGO_YANDEX).click()
    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is('Дзен'))

    @allure.step('Кликаем на кнопка Зказать для перехода на другу страницу и клик на лого самоката, чтобы вернуться обратно домой')
    def click_order_and_click_logo_scooter_back(self):
        self.click_order_button()
        self.click_logo_scooter()


