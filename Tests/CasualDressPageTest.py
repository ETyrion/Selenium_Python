import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CasualDressPage import CasualDressPageObject
from Pages.HomePage import HomePageObjects


class CasualDressTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Software\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        time.sleep(1)

    @pytest.mark.order(1)
    def test_click_casual_btn(self):
        driver = self.driver
        homePageObj = HomePageObjects(driver)
        axn = ActionChains(driver)
        axn.move_to_element(homePageObj.get_dress_tag()).perform()
        time.sleep(3)
        axn.move_to_element(homePageObj.get_casual_dress()).click().perform()
        time.sleep(2)


    @pytest.mark.order(2)
    def test_add_to_cart_validation(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(1)
        casualDressPageObj = CasualDressPageObject(driver)
        axn2 = ActionChains(driver)
        axn2.move_to_element(casualDressPageObj.hover_on_image()).perform()
        time.sleep(3)
        axn3 = ActionChains(driver)
        axn3.move_to_element(casualDressPageObj.get_add_to_cart_btn()).click().perform()
        time.sleep(2)

    @pytest.mark.order(3)
    def test_validate_cart_msg(self):
        driver =self.driver
        casualDressPageObj = CasualDressPageObject(driver)
        casualDressPageObj.get_cart_msg()
        print(casualDressPageObj.get_cart_msg())
        msg = 'Product successfully added to your shopping cart'
        assert msg == casualDressPageObj.get_cart_msg()
        time.sleep(5)

    @pytest.mark.order(4)
    def test_validate_cart_button(self):
        driver = self.driver
        casualDressPageObj = CasualDressPageObject(driver)
        button = casualDressPageObj.get_checkout_btn()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button))
        )
        #axn4 = ActionChains(driver)
        #axn4.move_to_element(button).click().perform()
        element.click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
