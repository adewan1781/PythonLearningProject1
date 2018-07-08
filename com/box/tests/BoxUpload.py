from com.box.com.box.utilities.BoxLoginSteps import BoxLoginSteps
from com.box.com.box.utilities.BoxUploadSteps import BoxUploadSteps


if __name__ == '__main__':
    obj = BoxLoginSteps()
    obj.verifyPageTitle("Box | Login")
    obj.loginProcess("nancydhingra131@gmail.com", "nancy131")
    obj.verifyPageTitle("All Files | Powered By Box")
    obj1 = BoxUploadSteps()
    obj1.selectFolderToUpload()

