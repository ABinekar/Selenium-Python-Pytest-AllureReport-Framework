from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".\\TestData\\TestData.xlsx"
    logger = LogGen.loggen()

    
