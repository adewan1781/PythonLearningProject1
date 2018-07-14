from selenium.webdriver.common.by import By

from com.box.com.box.utilities.WebControls import WebControls
from com.box.driver.DriverInstance import DriverInstance


class BoxUploadSteps:

    def __init__(self):
        self.driver = DriverInstance.getWebdiver()
        self.folderselect = WebControls(self.driver,By.XPATH, "//a[@class='item-name-link'][contains(text(),'serious123')]")
        self.uploadMenuButton = WebControls(self.driver,By.CSS_SELECTOR, "a[data-resin-target=\"uploadmenubutton\"]")
        self.fileElement = WebControls(self.driver,By.XPATH, "//li[@class='upload-file-handler-target']//input")
        self.uploadingStatus = WebControls(self.driver,By.CSS_SELECTOR, "div[class=\"uploads-manager is-uploading\"]")
        self.uploadCompletedStatus = WebControls(self.driver,By.CSS_SELECTOR, "div[class=\"uploads-manager is-completed\"]")
        self.uploadInactiveStatus = WebControls(self.driver,By.CSS_SELECTOR, "div[class=\"uploads-manager is-inactive\"]")
        self.alertdialog = WebControls(self.driver,By.CSS_SELECTOR, "div[role=\"alertdialog\"]")
        self.deletionRow = WebControls(self.driver,By.XPATH, "//li[@data-name='java basics.txt']/div[@role='row']")
        self.trashButton = WebControls(self.driver,By.CSS_SELECTOR, "button[data-type=\"bulk-delete-btn\"]")
        self.confirmButton = WebControls (self.driver, By.CSS_SELECTOR, "button[data-event-type=\"ok\"]")

    def selectFolderToGoIn(self):
        self.folderselect.clickControl()

    def clickUploadMenu(self):
        self.uploadMenuButton.clickControl()

    def uploadFile(self, filePath):
        self.fileElement.typeKeys(filePath)

    def verifyUpload(self):
        self.uploadingStatus.waitForElementInvisibility()
        self.uploadCompletedStatus.waitForElementInvisibility()
        self.uploadInactiveStatus.waitForElementInvisibility()
        uploadMessage = self.alertdialog.getElementText()
        assert ("1 item was uploaded successfully." in uploadMessage), "Upload message not there."
        print("aaaaaaaaaaaaaaaaaaaaaa   ",uploadMessage)
        self.alertdialog.waitForElementInvisibility()

    def selectRowToDelete(self):
        self.deletionRow.clickControl()

    def deleteRow(self):
        self.trashButton.waitAndClick()
        self.confirmButton.waitAndClick()
        uploadMessage = self.alertdialog.getElementText()
        # assert ("Item successfully moved to trash." in uploadMessage), "Upload message not there."
        print ("aaaaaaaaaaaaaaaaaaaaaa   ", uploadMessage)









    



