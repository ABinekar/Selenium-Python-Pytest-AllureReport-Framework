import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".\\TestData\\TestData.xlsx"
    logger = LogGen.loggen()

    @allure.description("Register User")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_TC_001(self, setup):
        self.logger.info("***** Test_001 Register User test started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Automation Exercise":
            assert True
            self.logger.info("***** Home page title is matched *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name = "test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Home page title is not matched *****")
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.clickSignInLogin()

