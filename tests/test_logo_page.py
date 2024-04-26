import allure

from pages.logo_page import LogoPage
from data import URL

class TestLogoPage:

    @allure.title('Проверка возврата на домашнюю страницу по клику на логотип Самоката')
    @allure.description('Кликаем на кнопку "Принять куки", далее на кнопку "Заказать", чтобы уйти с домашней страницы, а потом возвращаемся на нее обратно')
    def test_logo_scooter(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_cookie()
        logo_page.click_order_and_click_logo_scooter_back()

        assert logo_page.get_current_url() == URL.FIRST_PAGE

    @allure.title('Проверка редиректа на сайт Дзена по клику на лого Яндекса')
    @allure.description('Кликаем на кнопку "Принять куки", далее клик на лого Яндекса и проверяем, что произошел редирект на страничку Дзена')
    def test_logo_yandex(self, driver):
        logo_page = LogoPage(driver)
        logo_page.click_cookie()
        logo_page.click_logo_yandex()
        logo_page.wait_for_url_changes_dzen()
        logo_page.switch_driver()
        logo_page.wait_for_title()
        assert 'dzen.ru' in logo_page.get_current_url()



