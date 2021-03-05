from selenium import webdriver

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id= "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def set_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def set_password(self, pwd):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()