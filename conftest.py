import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    prefs = {
        "credentials_enable_service": False,
        "password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()