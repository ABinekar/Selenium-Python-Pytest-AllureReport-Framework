import random
import string
import time
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
        if act_title == "Error: A user could not be found with this email address.":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False

    @allure.description("Log-in with correct username and empty password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
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
        if act_title == "Error: Password is required.":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False

    @allure.description("Log-in with empty username and valid password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_TC_004(self, setup):
        self.logger.info("***** Test_004 Log-in with empty username and valid password test started *****")
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
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.lp.getEmptyPasswordMsg()
        print(act_title)
        if act_title == "Error: Username is required.":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False

    @allure.description("Log-in with empty username and empty password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_TC_005(self, setup):
        self.logger.info("***** Test_005 Log-in with empty username and empty password test started *****")
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
        self.lp.clickLogin()
        act_title = self.lp.getEmptyPasswordMsg()
        print(act_title)
        if act_title == "Error: Username is required.":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False

    @allure.description("Log-in -Password should be masked")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_TC_006(self, setup):
        self.logger.info("***** Test_006 Log-in -Password should be masked test started *****")
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
        self.lp.setPassword(self.password)
        act_title = self.lp.gettextPassword()
        print(act_title)
        if act_title == "password":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False

    @allure.description("Login-Handles case sensitive")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_TC_007(self, setup):
        self.logger.info("***** Test_007 Login-Handles case sensitive test started *****")
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
        self.username = XLUtility.readData(self.path, 'Sheet1', 8, 3)
        self.password = XLUtility.readData(self.path, 'Sheet1', 8, 4)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_msg = self.lp.getErrorMsg()
        print(act_msg)
        if act_msg == "Error: the password you entered for the username ANANTBINEKAR@GMAIL.COM is incorrect. Lost " \
                      "your password?":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False

    @allure.description("Registration-Sign-in")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_TC_008(self, setup):
        self.logger.info("***** Test_008 Registration-Sign-in test started *****")
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
        self.dp = DashboardPage(self.driver)
        self.lp.clickMyAccount()
        N = 7
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=N))
        username = str(res) + "@gmail.com"
        self.lp.setRegEmail(username.lower())
        self.lp.setRegPassword(self.password)
        self.lp.clickRegister()
        self.lp.clickRegister()
        time.sleep(5)
        act_msg = self.dp.gettextDashboard()
        print(act_msg)
        if act_msg == "Dashboard":
            assert True
            self.logger.info("***** Test case is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TC_001_1.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_TC_001_1",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("***** Test case is failed *****")
            assert False
