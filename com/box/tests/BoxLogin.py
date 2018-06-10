from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BoxLogin:

    def login(self):
        driver = webdriver.Firefox()
        # driver.maximize_window ()
        driver.get ("http://app.box.com")

        print ("\n==================================================\n")
        print (driver.title)
        assert "Box | Login" in driver.title, "Title is incorrect"
        # driver.find_element_by_name("login")
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
        element.send_keys ("Test Profile1")
        driver.quit()

if __name__ == '__main__':
    obj = BoxLogin()
    obj.login()