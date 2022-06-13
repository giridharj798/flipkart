from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    loginbtn = (By.LINK_TEXT, "Login")
    id = (By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    loginpass = (By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']")
    continuebtn = (By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")


    def getLoginbtn(self):
        return self.driver.find_elements(*HomePage.loginbtn)

    def getID(self):
        return self.driver.find_element(*HomePage.id)

    def getLoginpass(self):
        return self.driver.find_element(*HomePage.loginpass)

    def getContinuebtn(self):
        return self.driver.find_element(*HomePage.continuebtn)