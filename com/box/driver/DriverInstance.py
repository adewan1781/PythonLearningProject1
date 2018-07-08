from selenium import webdriver

class DriverInstance:
    __webDriver = None

    def __init__(self):
        DriverInstance.__webDriver = webdriver.Firefox()

    @staticmethod
    def getWebdiver():
        DriverInstance.__webDriver = webdriver.Firefox()
        return DriverInstance.__webDriver