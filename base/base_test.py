import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class BaseTest:

    data: Data

    login_page: LoginPage
    products_page: ProductsPage

    # Фикстура для создания аннотации и прямого обращения к страницам в тестах
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.products_page = ProductsPage(driver)
