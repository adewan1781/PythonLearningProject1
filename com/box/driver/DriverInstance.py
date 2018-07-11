from selenium import webdriver

class DriverInstance:
    # Here will be the instance stored.
    __webDriver = None

    def __init__(self):
        """ Virtually private constructor. """
        if DriverInstance.__webDriver != None:
            raise Exception ("This class is a singleton!")
        else:
            DriverInstance.__webDriver = self

    @staticmethod
    def getWebdiver():
        if DriverInstance.__webDriver == None:
            DriverInstance.__webDriver = webdriver.Firefox()
        return DriverInstance.__webDriver

