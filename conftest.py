import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    browser = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs',
                     {'intl.accept_languages': 'ru'})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", 'ru')
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(5)
    else:
        print("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
