from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebControls:

    def __init__(self,driver, byLocator, byValue):
        self.driver = driver
        self.byLocator = byLocator
        self.byValue = byValue
        self.wait = WebDriverWait(self.driver, 45)


    def waitAndFindElement(self):
        print("Web Element with ", self.byLocator, ":", self.byValue)
        self.element = None
        present = True
        try:
            self.element = self.wait.until(EC.presence_of_element_located((self.byLocator, self.byValue)))
        except Exception:
            present = False
            print("Web Element with ", self.byLocator, ":", self.byValue, " not found")
            self.driver.save_screenshot("/Users/rajat/pythonworkspace/PythonLearningProject1/screenshot.png")
        return present

    def typeKeys(self, value):
        if self.waitAndFindElement():
            self.element.send_keys(value)

    def clickControl(self):
        if self.waitAndFindElement():
            self.element.click()

    def verifyTitle(self, title):
        present = True
        try:
            self.wait.until(EC.title_contains(title))
        except Exception:
            present = False
        return present

    def driverQuit(self):
        self.driver.quit()

