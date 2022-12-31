import allure
import pytest
from allure_commons.types import AttachmentType
from Utilities import XLUtility
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".\\TestData\\TestData.xlsx"
    logger = LogGen.loggen()

    @allure.description("Log-in with valid username and password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_TC_001(self, setup):
        self.logger.info("***** Test_001 Log-in with valid username and password test started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Automation Practice Site":
            assert True
            self.logger.info("***** Home page title is matched *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Home page title is not matched *****")
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.clickMyAccount()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.dp = DashboardPage(self.driver)
        act_title = self.driver.title
        print(act_title)
        if act_title == "My Account – Automation Practice Site":
            assert True
            self.logger.info("***** User Login is successfully *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** User Login is unsuccessfully *****")
            assert False

    @allure.description("Log-in with incorrect username and incorrect password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_TC_002(self, setup):
        self.logger.info("***** Test_001 Log-in with incorrect username and incorrect password test started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Automation Practice Site":
            assert True
            self.logger.info("***** Home page title is matched *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Home page title is not matched *****")
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.clickMyAccount()
        self.username = XLUtility.readData(self.path, 'Sheet1', 3, 3)
        self.password = XLUtility.readData(self.path, 'Sheet1', 3, 4)
        print(self.username)
        print(self.password)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.lp.getMsg()
        print(act_title)
        #if act_title == "Error":
        if act_title is None:
            assert True
            self.logger.info("***** User Login is successfully *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** User Login is unsuccessfully *****")
            assert False

    @allure.description("Log-in with correct username and empty password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_TC_003(self, setup):
        self.logger.info("***** Test_003 Log-in with correct username and empty password test started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Automation Practice Site":
            assert True
            self.logger.info("***** Home page title is matched *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Home page title is not matched *****")
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.clickMyAccount()
        self.username = XLUtility.readData(self.path, 'Sheet1', 4, 3)
        print(self.username)
        self.lp.setUsername(self.username)
        self.lp.clickLogin()
        act_title = self.lp.getEmptyPasswordMsg()
        print(act_title)
        # if act_title == "Error":
        if act_title is None:
            assert True
            self.logger.info("***** User Login is successfully *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** User Login is unsuccessfully *****")
            assert False
