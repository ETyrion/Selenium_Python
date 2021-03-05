import time

import unittest
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Pages.HomePage import HomePageObjects
from Pages.WomenPage import WomenPageObjects
from Tests.HomePageTest import HomePageTest


class WomenPageTestMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Software\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        driver = cls.driver

    @pytest.mark.smoke
    def test_click_womenTag(self):
        driver = self.driver
        homeObj = HomePageObjects(driver)
        womentag = homeObj.get_womenTag()
        axn = ActionChains(driver)
        axn.move_to_element(womentag).click().perform()
        time.sleep(5)

    @pytest.mark.smoke
    def test_selectSize(self):
        driver = self.driver
        womenpageobj = WomenPageObjects(driver)
        womenpageobj.size_xpath()
        for size in womenpageobj.size_xpath():
            time.sleep(1)
            size.click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()