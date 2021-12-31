from selenium import webdriver
import bupa.constants as const
import os

class Bupa(webdriver.Chrome):
    def __init__(self, driver_path="C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += ";"
        os.environ['PATH'] += self.driver_path
        super(Bupa, self).__init__()
        self.implicitly_wait(15)

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def startFresh(self):
        start_button = self.find_element_by_class_name(
            "blue-button"
        )
        start_button.click()
        print("The button is clicked")