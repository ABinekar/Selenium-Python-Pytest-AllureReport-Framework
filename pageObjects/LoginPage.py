from selenium.webdriver.common.by import By


class LoginPage:

    link_signInLogin_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"
    text_NewUserSignUp_xpath = "//*[@id='form']/div/div/div[3]/div/h2"
    textbox_SignInName_xpath = ""
    textbox_SignInEmail_xpath = ""
    btn_Signup_xpath = ""
    textbox_LoginEmailAddress_xpath = ""
    textbox_LoginPassword_xpath = ""
    text_LoginToYourAccount_xpath = ""
    btn_Login_xpath = ""
    text_YourEmailOrPasswordIsIncorrect_xpath = ""

    def __init__(self, driver):
        self.driver = driver

    def clickSignInLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.link_signInLogin_xpath).click()
