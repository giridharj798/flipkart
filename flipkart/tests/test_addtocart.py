import time
from lib2to3.pgen2 import driver

import pytest

from TestData.Data import LoginPageData
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_cart(BaseClass):
    def test_addtocart(self, getData):
        homepage = HomePage(self.driver)
        homepage.getID().send_keys(getData["Mobileno"])
        homepage.getLoginpass().send_keys(getData["Password"])
        homepage.getContinuebtn().click()
        cartpage = CartPage(self.driver)
        time.sleep(3)
        cartpage.getsearch().send_keys("shirts")
        cartpage.getsearchbtn().click()
        time.sleep(15)
        cartpage.getmobileimage().click()
        cartpage.getcartbtn().click()




    @pytest.fixture(params=LoginPageData.test_Login_Data)
    def getData(self, request):
        return request.param