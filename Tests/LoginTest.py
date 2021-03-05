import time

from selenium import webdriver
from Pages.LoginPage import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Software\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")
        cls.driver.maximize_window()
        time.sleep(1)

    def test_valid_login(self):
        driver = self.driver
        login_obj = LoginPage(driver)
        login_obj.set_username("Admin")
        time.sleep(1)
        login_obj.set_password("admin123")
        time.sleep(1)
        login_obj.click_login()



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




