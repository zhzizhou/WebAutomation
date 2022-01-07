from selenium import webdriver
import bupa.constants as const
import os
from selenium.webdriver.common.by import By
# get back onto windows again



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

    # working on selection assessment option for the selected bupa centre
    def select_assessments(self,visa="student"):
        # first need an input validation check
        # need only 501, 502
        print("selecting assessment .....")
        # button for 501
        Med501 = self.find_element(By.ID,"chkClass1_489")
        Med501.click()
        # button for 502
        Med502  = self.find_element(By.ID,"chkClass1_492")
        Med502.click()



        if (visa != "student"):
            # need all three, adding the 704
            Med704 = self.find_element(By.ID, "chkClass1_572")
            Med704.click()



        # submit the form
        Next_Button = self.find_element(By.ID, "ContentPlaceHolder1_btnCont")
        Next_Button.click()


    def earliest_time(self):
        TimeSlot = self.find_element(By.ID, "ContentPlaceHolder1_SelectTime1_divSearchResults")
        TimeString = TimeSlot.text
        print(TimeString)


