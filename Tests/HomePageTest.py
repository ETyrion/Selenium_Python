import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from Pages.HomePage import HomePageObjects
import unittest
import pytest


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Software\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        time.sleep(1)

    @pytest.mark.smoke
    def test_validate_PageTitle(self):
        driver = self.driver
        homeObj = HomePageObjects(driver)
        title = homeObj.get_Title()
        assert title == 'My Store'
        if(title=='My Store'):
            print('Title is matched')
        else:
            print('Title is not matched')

    @pytest.mark.smoke
    def test_searchDress(self):
        driver = self.driver
        homeObj = HomePageObjects(driver)
        homeObj.search_Dress('party dress')
        time.sleep(3)

    def test_select_womenTag(self):
        driver = self.driver
        homeObj = HomePageObjects(driver)
        axn = ActionChains(driver)
        axn.move_to_element(homeObj.get_womenTag()).perform()
        time.sleep(3)

    def test_select_casualTag(self):
        driver = self.driver
        homeObj = HomePageObjects(driver)
        axn = ActionChains(driver)
        axn.move_to_element(homeObj.get_dress_tag()).perform()
        time.sleep(3)
        axn.move_to_element(homeObj.get_casual_dress()).click().perform()
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()