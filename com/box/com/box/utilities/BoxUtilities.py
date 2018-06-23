import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoxUtilities:

    def setUp(self):
        self.driver = webdriver.Firefox()
        # driver.maximize_window ()
        self.driver.get("http://app.box.com")
        self.driver.implicitly_wait(30)  # seconds


    def verifyPageTitle(self, title):
        titleFlag = WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        assert titleFlag, "Title is not present"

    def loginProcess(self, username, password):

        element = self.waitAndFindElement(By.NAME, "login")

        element.send_keys(username)
        element = self.waitAndFindElement(By.CSS_SELECTOR, "button[type=\"submit\"]")
        element.click()
        element = self.waitAndFindElement (By.NAME, "password")
        element.send_keys(password)
        element = self.waitAndFindElement (By.CSS_SELECTOR, "button[type=\"submit\"]")
        element.click()

    def logOutProcess(self):
        element = self.waitAndFindElement (By.CSS_SELECTOR, "button[data-resin-target=\"accountmenu\"]")
        element.click()
        element = self.waitAndFindElement (By.CSS_SELECTOR, "a[data-resin-target=\"logout\"]")

        element.click()
        time.sleep(5)

    def driverQuit(self):
        self.driver.quit()
    #
    def waitAndFindElement(self, byLocator, value):
        print("Web Element with ",byLocator,":", value)
        element = None
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((byLocator, value)))
        except Exception:
            print ("Web Element with ",byLocator,":", value, " not found")
            self.driver.save_screenshot("/Users/rajat/pythonworkspace/PythonLearningProject1/screenshot.png")
        return element
