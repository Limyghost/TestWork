import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Profile functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Authentication and authorization")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.products_page.is_opened()
        self.products_page.make_screenshot("Products page successfully opened screenshot")

    @allure.title("Login and logout")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_logout(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.products_page.is_opened()
        self.products_page.click_burger_menu_button()
        self.products_page.click_logout_button()
        self.login_page.is_returned()
        self.login_page.make_screenshot("Login page redirect success screenshot")