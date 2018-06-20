from com.box.com.box.utilities.BoxUtilities import BoxUtilities

if __name__ == '__main__':
    obj = BoxUtilities()
    obj.setUp()
    obj.verifyPageTitle("Box | Login")
    obj.loginProcess("nancydhingra131@gmail.com", "nancy131")
    obj.verifyPageTitle("All Files | Powered By Box")
    obj.logOutProcess()
    obj.verifyPageTitle("Box | Login")
    obj.driverQuit()