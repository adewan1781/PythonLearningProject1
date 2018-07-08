import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from com.box.com.box.utilities.WebControls import WebControls
from com.box.driver.DriverInstance import DriverInstance


class BoxLoginSteps:

    def __init__(self):
        # self.driver = webdriver.Firefox()
        self.driver = DriverInstance.getWebdiver()
        # driver.maximize_window ()
        self.driver.get("http://app.box.com")
        self.driver.implicitly_wait(30)  # seconds
        self.emailTextField = WebControls(self.driver,By.NAME, "login")
        self.passwordTextField = WebControls(self.driver,By.NAME, "password")
        self.loginButton = WebControls(self.driver,By.CSS_SELECTOR, "button[type=\"submit\"]")
        self.optionsDropdown = WebControls(self.driver,By.CSS_SELECTOR, "button[data-resin-target=\"accountmenu\"]")
        self.logoutLink = WebControls(self.driver, By.CSS_SELECTOR, "a[data-resin-target=\"logout\"]")
        self.page = WebControls(self.driver,"","")


    def verifyPageTitle(self, title):
        titleFlag = self.page.verifyTitle(title)
        assert titleFlag, "Title is not present"

    def loginProcess(self, username, password):
        self.emailTextField.typeKeys(username)
        # element = self.waitAndFindElement(By.NAME, "login")
        # element.send_keys(username)
        self.loginButton.clickControl()
        # element = self.waitAndFindElement(By.CSS_SELECTOR, "button[type=\"submit\"]")
        # element.click()
        self.passwordTextField.typeKeys(password)
        # element = self.waitAndFindElement(By.NAME, "password")
        # element.send_keys(password)
        self.loginButton.clickControl()
        # element = self.waitAndFindElement(By.CSS_SELECTOR, "button[type=\"submit\"]")
        # element.click()

    def logOutProcess(self):
        self.optionsDropdown.clickControl()
        # element = self.waitAndFindElement(By.CSS_SELECTOR, "button[data-resin-target=\"accountmenu\"]")
        # element.click()
        self.logoutLink.clickControl()
        # element = self.waitAndFindElement()
        # element.click()
        time.sleep(5)

    def driverQuit(self):
        self.driver.quit()


