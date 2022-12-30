import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Utilities.customLogger import LogGen

logger = LogGen.loggen()


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        logger.info("************* Login test started ***********")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching chrome browser ------ ")
    elif browser == 'firefox':
        driver = webdriver.firefox()
        driver.maximize_window()
        print("Launching Firefox browser ------ ")
    else:
        logger.info("************* Login test started ***********")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching chrome browser ------ ")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##################### Pytest HTML Report ############################

def pytest_configure(config):
    config._metadata['Project Name'] = 'My Account-Automation demo site'
    config._metadata['Module Name'] = 'Order Place'
    config._metadata['Tester'] = 'Anant'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
