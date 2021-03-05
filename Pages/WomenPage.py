class WomenPageObjects():
    def __init__(self, driver):
        self.driver = driver

        self.sizexpath = "//*[@id='ul_layered_id_attribute_group_1']/li/div"

    def size_xpath(self):
        sizeelements = self.driver.find_elements_by_xpath(self.sizexpath)
        print(len(sizeelements))
        return sizeelements
