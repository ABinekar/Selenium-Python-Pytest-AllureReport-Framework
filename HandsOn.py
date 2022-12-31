from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
text = driver.find_element(by=By.XPATH, value='//*[@id="menu-item-50"]/a').text
print(text)
