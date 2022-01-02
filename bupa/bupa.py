from selenium import webdriver
import bupa.constants as const
import os
from selenium.webdriver.common.by import By




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

    def newIndividual(self):
        new_individual = self.find_element_by_id("ContentPlaceHolder1_btnInd")
        new_individual.click()
        print("new individual booking looking up....")

    def select_centre(self,location=None):
        print(f"selecting {location} bupa centre")
        selected_location = self.find_element(By.CLASS_NAME,"tdloc_checkbox")
        try:
            selected_location.click()
            print(f"Clicked the {location} centre")
        except:
            alert = self.switch_to_alert()
            alert.accpet()
            print("alert dismissed")
        # handle the javascript pop up box
        #self.popupHandle()
        submit_button = self.find_element(
            By.ID,
            "ContentPlaceHolder1_btnCont"
        )

        submit_button.click()
        print("Location request submitted ....")

    def select_assessments(self,visa="student"):
        # first need an input validation check
        if (visa == "student"):
            # need only 501, 502
            print("selecting assessment for general student visa .....")
            Med = self.find_element()

        else:
            # need all three
            print("selecting assessment for general migration visa .....")

        # submit the form





