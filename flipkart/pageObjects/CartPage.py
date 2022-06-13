from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.NAME, "q")
    searchbutton = (By.XPATH, "//button[@class='L0Z3Pu']")
    mobimg = (By.XPATH, "//img[@class='_396cs4 _3exPp9']")
    cartbutton = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")


    def getsearch(self):
        return self.driver.find_element(*CartPage.search)

    def getsearchbtn(self):
        return self.driver.find_element(*CartPage.searchbutton)

    def getmobileimage(self):
        return self.driver.find_element(*CartPage.mobimg)

    def getcartbtn(self):
        return self.driver.find_element(*CartPage.cartbutton)
