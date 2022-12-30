from selenium.webdriver.common.by import By


class LoginPage:

    link_signInLogin_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"
    text_NewUserSignUp_xpath = "//*[@id='form']/div/div/div[3]/div/h2"

    def __init__(self, driver):
        self.driver = driver

    def clickSignInLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.link_signInLogin_xpath).click()
