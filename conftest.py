import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope='class')
def driver(request):
    global options, version, platform, browser
    username = "prateektiwari241189"
    access_key = "LT_YyhB9S6FacoOJ5WjRUWav5tWxilQEuMMaTAxkeQ4zgDWpRP"
    scenario = request.param
    if scenario == 'test1':
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        platform = "macOS Ventura"
        version = "127.0"
    elif scenario == 'test2':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        platform = "Windows 10"
        version = "128"
    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    option = {
        "platform": platform,
        "version": version,
        "name": "Selenium Test: " + platform,
        "Build": "Selenium Advance Certification",
        "video": True,
        "visual": True,
        "network": True,
        "console": True
    }
    options.set_capability("LT:Options", option)
    browser = webdriver.Remote(command_executor=selenium_endpoint, options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
