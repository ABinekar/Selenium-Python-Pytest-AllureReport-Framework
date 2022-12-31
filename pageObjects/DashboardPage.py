from selenium.webdriver.common.by import By


class DashboardPage:

    link_Dashboard_xpath = "/html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[1]/a"

    def __init__(self, driver):
        self.driver = driver

    def getDashboard(self):
        self.driver.find_element(by=By.XPATH, value=self.link_Dashboard_xpath).text


