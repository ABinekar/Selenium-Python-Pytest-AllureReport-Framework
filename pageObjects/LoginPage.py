from selenium.webdriver.common.by import By


class LoginPage:

    link_signInLogin_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"
    text_NewUserSignUp_xpath = "//*[@id='form']/div/div/div[3]/div/h2"
    textbox_SignInName_xpath = "//input[@data-qa='signup-name']"
    textbox_SignInEmail_xpath = "//input[@data-qa='signup-email']"
    btn_Signup_xpath = "//button[@data-qa='signup-button']"
    textbox_LoginEmailAddress_xpath = "//input[@data-qa='login-email']"
    textbox_LoginPassword_xpath = "//input[@data-qa='login-password']"
    text_LoginToYourAccount_xpath = "//*[@id='form']/div/div/div[1]/div/h2"
    btn_Login_xpath = "//button[@data-qa='login-button']"
    text_YourEmailOrPasswordIsIncorrect_xpath = ""

    def __init__(self, driver):
        self.driver = driver

    def clickSignInLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.link_signInLogin_xpath).click()
