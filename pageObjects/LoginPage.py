from selenium.webdriver.common.by import By


class LoginPage:
    link_MyAccount_xpath = "//*[@id='menu-item-50']/a"
    textbox_Username_id = "username"
    textbox_Password_id = "password"
    btn_Login_name = "login"
    textbox_EmailAddress_id = "reg_email"
    textbox_RegPassword_id = "reg_password"
    btn_Register_name = "register"
    text_IncorrectMsg_xpath = "//*[@id='page-36']/div/div[1]/ul/li/strong[1]"
    text_EmptyMsg_xpath = "//*[@id='page-36']/div/div[1]/ul/li"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(by=By.XPATH, value=self.link_MyAccount_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(by=By.ID, value=self.textbox_Username_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_Username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(by=By.ID, value=self.textbox_Password_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(by=By.NAME, value=self.btn_Login_name).click()

    def setRegEmail(self, email):
        self.driver.find_element(by=By.ID, value=self.textbox_EmailAddress_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_EmailAddress_id).send_keys(email)

    def setRegPassword(self, password):
        self.driver.find_element(by=By.ID, value=self.textbox_RegPassword_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_RegPassword_id).send_keys(password)

    def clickRegister(self):
        self.driver.find_element(by=By.NAME, value=self.btn_Register_name).click()

    def getMsg(self):
        self.driver.find_element(by=By.XPATH, value=self.text_IncorrectMsg_xpath).text

    def getEmptyPasswordMsg(self):
        self.driver.find_element(by=By.XPATH, value=self.text_EmptyMsg_xpath).text
