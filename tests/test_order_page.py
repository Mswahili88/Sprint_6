from pages.order_page import OrderPage
from data import ITEMS
import allure

class TestOrderPage:
    @allure.title('Заполнение формы заказа самоката с набором данных №1')
    @allure.description('Заполняем форму заказа самоката из двух частей и убеждаемся в положительном финальном итоге заполнения')
    def test_order_page_scenario_1(self, driver):
        order_page = OrderPage(driver)
        order_page.click_cookie()
        order_page.click(OrderPage.ORDER_UPPER_BUTTON)
        order_page.set_details_data(ITEMS.NAME_1, ITEMS.SURNAME_1, ITEMS.ADDRESS_1)
        order_page.choose_metro_set_phone(OrderPage.METRO_PREOBRAZHENKA, ITEMS.PHONE_NUMBER_1)
        order_page.click(OrderPage.NEXT_BUTTON)
        order_page.click_and_set_date(ITEMS.DATE_1)
        order_page.click_and_choose_period_add_comment(ITEMS.COMMENT_2)
        order_page.press_buttons_order_and_yes()

        assert order_page.driver.find_element(*OrderPage.CONFIRMATION_BUTTON).is_displayed()

    @allure.title('Заполнение формы заказа самоката с набором данных №2')
    @allure.description('Заполняем форму заказа самоката из двух частей и убеждаемся в положительном финальном итоге заполнения')
    def test_order_page_scenario_2(self, driver):
        order_page = OrderPage(driver)
        order_page.click_cookie()
        order_page.click(OrderPage.ORDER_MIDDLE_BUTTON)
        order_page.set_details_data(ITEMS.NAME_2, ITEMS.SURNAME_2, ITEMS.ADDRESS_2)
        order_page.choose_metro_set_phone(OrderPage.METRO_CHERKIZOVSKAYA, ITEMS.PHONE_NUMBER_1)
        order_page.click(OrderPage.NEXT_BUTTON)
        order_page.click_and_set_date(ITEMS.DATE_2)
        order_page.click_and_choose_period_add_comment(ITEMS.COMMENT_1)
        order_page.press_buttons_order_and_yes()

        assert order_page.driver.find_element(*OrderPage.CONFIRMATION_BUTTON).is_displayed()






