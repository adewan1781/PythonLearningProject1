import time

import nil as nil
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

        element = self.waitAndFindElement('name', 'login')
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
        element.send_keys(username)
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type=\"submit\"]")))
        element.click()
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type=\"submit\"]")))
        element.click()

        # assert "All Files | Powered By Box" in driver.title, "Title is incorrect"

    def logOutProcess(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-resin-target=\"accountmenu\"]")))
        element.click()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-resin-target=\"logout\"]")))
        element.click()
        time.sleep(5)

    def driverQuit(self):
        self.driver.quit()

    def waitAndFindElement(self, byLocator, value):
        print(value, byLocator)
        element = nil
        try:
            if byLocator == 'name':
                element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.NAME, value))
        except Exception:
            self.driver.save_screenshot("/Users/rajat/pythonworkspace/PythonLearningProject1/screenshot.png")
        finally:
            print("Web Element with value: ", value, " not found")
        return element
