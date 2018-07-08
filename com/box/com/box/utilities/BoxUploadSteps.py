from selenium.webdriver.common.by import By

from com.box.com.box.utilities.WebControls import WebControls
from com.box.driver.DriverInstance import DriverInstance


class BoxUploadSteps:

    def __init__(self):
        self.driver = DriverInstance.getWebdiver()
        self.folderselect = WebControls(self.driver,By.XPATH, "//a[@class='item-name-link'][contains(text(),'serious123')]")


    def selectFolderToUpload(self):
        self.folderselect.clickControl()


