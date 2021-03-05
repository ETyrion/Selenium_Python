class CasualDressPageObject():
    def __init__(self, driver):
        self.driver = driver

        self.add_cart_btn_xpath = "//*[@class='button ajax_add_to_cart_button btn btn-default']"
        self.dress_image_xpath ="//*[@class='product-container']//*[@itemprop='name']"
        self.shopping_msg_xpath = "//*[@class='layer_cart_product col-xs-12 col-md-6']//h2"
        self.checkout_xpath = "//*[@id='layer_cart']//div[@class='layer_cart_cart col-xs-12 col-md-6']//a[@class='btn btn-default button button-medium']"

    def get_Page_Title(self):
        casualPageTitle = self.driver.ttle

    def get_add_to_cart_btn(self):
        cartbtn= self.driver.find_element_by_xpath(self.add_cart_btn_xpath)
        return cartbtn

    def hover_on_image(self):
        img = self.driver.find_element_by_xpath(self.dress_image_xpath)
        return img

    def get_cart_msg(self):
        msg = self.driver.find_element_by_xpath(self.shopping_msg_xpath).text
        return msg

    def get_checkout_btn(self):
       btn= self.checkout_xpath
       return btn





