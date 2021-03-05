from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageObjects():
    def __init__(self, driver):
        self.driver = driver

        self.womenTag_xpath = "(//*[@class='sf-with-ul'])[1]"
        self.dressesTag_xpath = "(//*[@class='sf-with-ul'])[4]"
        self.casualdress_xpath=("(//*[@title='Casual Dresses'])[2]")
        self.searchBox_Id = "search_query_top"

    def search_Dress(self, dress_To_be_Searched):
        self.driver.find_element_by_id(self.searchBox_Id).clear()
        self.driver.find_element_by_id(self.searchBox_Id).send_keys(dress_To_be_Searched)

    def get_Title(self):
        return self.driver.title

    def get_womenTag(self):
        womentag = self.driver.find_element_by_xpath(self.womenTag_xpath)
        return womentag

    def get_dress_tag(self):
        dress = self.driver.find_element_by_xpath(self.dressesTag_xpath)
        return dress

    def get_casual_dress(self):
        casual_dress = self.driver.find_element_by_xpath(self.casualdress_xpath)
        return casual_dress