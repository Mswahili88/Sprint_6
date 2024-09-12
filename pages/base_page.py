import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:
    COOKIE_BUTTON = (By.XPATH, "//*[contains(@class,'App_CookieButton__3cvqF')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаем драйвер')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Очевидно дожидаемся нужного элемента по локатору')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти элемент и вытащить текст элемента')
    def find_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Ожидание появления заголовка на странице')
    def wait_for_title_is(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))

    @allure.step('Дожидаемся, пока поменяется страница')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    @allure.step('Нажимаем на кнопку "Принять куки"')
    def click_cookie(self):
        self.driver.find_element(*self.COOKIE_BUTTON).click()

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step('Скроллим, пока не увидим нужный элемент по локатору')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Вытаскиваем по номеру и возвращаем локаторы вопросов')
    def question_locator(self, number):
        return (By.ID, f"accordion__heading-{number}")

    @allure.step('Вытаскиваем по номеру и возвращаем локаторы ответов')
    def answer_locator(self, number):
        return (By.ID, f"accordion__panel-{number}")