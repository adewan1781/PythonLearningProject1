import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebControls:

    def __init__(self,driver, byLocator, byValue):
        self.driver = driver
        self.byLocator = byLocator
        self.byValue = byValue
        self.wait = WebDriverWait(self.driver, 45)


    def waitAndFindElement(self):
        self.element = None
        present = True
        try:
            self.element = self.wait.until(EC.presence_of_element_located((self.byLocator, self.byValue)))
            print ("Web Element with ", self.byLocator, ":", self.byValue," found")
        except Exception:
            present = False
            print("Web Element with ", self.byLocator, ":", self.byValue, " not found")
            self.driver.save_screenshot("/Users/rajat/pythonworkspace/PythonLearningProject1/screenshot.png")
        return present

    def waitForVisibilityAndFindElement(self):
        self.element = None
        present = True
        try:
            self.element = self.wait.until(EC.visibility_of_element_located((self.byLocator, self.byValue)))
            print ("Web Element with ", self.byLocator, ":", self.byValue, " found")
        except Exception:
            present = False
            print ("Web Element with ", self.byLocator, ":", self.byValue, " not found")
            self.driver.save_screenshot ("/Users/rajat/pythonworkspace/PythonLearningProject1/screenshot.png")
        return present

    def typeKeys(self, value):
        if self.waitAndFindElement():
            self.element.send_keys(value)

    def clickControl(self):
        if self.waitAndFindElement():
            self.element.click()

    def waitAndClick(self):
        if self.waitForVisibilityAndFindElement():
            self.element.click()

    def getElementText(self):
        elementText = None
        if self.waitAndFindElement():
            elementText = self.element.text
        return elementText

    def verifyTitle(self, title):
        present = True
        try:
            self.wait.until(EC.title_contains(title))
        except Exception:
            present = False
        return present

    def waitForElementInvisibility(self, timeout=5):
        self.driver.implicitly_wait(0)
        try:
            element = WebDriverWait (self.driver, timeout).until(EC.invisibility_of_element_located ((self.byLocator, self.byValue)))
        except selenium.common.exceptions.TimeoutException:
            print ("wait_for_element timeout: " + self.byValue)
        # self.driver.implicitly_wait(30)

    def driverQuit(self):
        self.driver.quit()

