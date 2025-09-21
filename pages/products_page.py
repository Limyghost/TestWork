import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):

    PAGE_URL = Links.PRODUCTS_PAGE

    BURGER_MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    LOGOUT_BUTTON = ("xpath", "//a[@id='logout_sidebar_link']")

    @allure.step("Click burger-menu button")
    def click_burger_menu_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU_BUTTON)).click()

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
