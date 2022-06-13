import pytest

from TestData.Data import LoginPageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestLogin(BaseClass):
    def test_2login(self, getData):
        homepage = HomePage(self.driver)
        homepage.getID().send_keys(getData["Mobileno"])
        homepage.getLoginpass().send_keys(getData["Password"])
        homepage.getContinuebtn().click()

    @pytest.fixture(params=LoginPageData.test_Login_Data)
    def getData(self, request):
        return request.param
