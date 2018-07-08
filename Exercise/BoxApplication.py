from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BoxApplication:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def open_browser(self):
        self.driver.fullscreen_window()
        self.driver.get("https://www.box.com")

    def login_box(self):
        self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Login")))
        self.driver.find_element_by_link_text("Login").click()
        self.wait.until(ec.presence_of_element_located((By.NAME, "login")))
        self.driver.find_element_by_name("login").send_keys("nancydhingra131@gmail.com")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait.until(ec.presence_of_element_located((By.NAME, "password")))
        self.driver.find_element_by_name("password").send_keys("nancy131")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def create_folder(self):
        self.driver.find_element_by_xpath("//a[@aria-label='Create a new item']").click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//button[@data-type='new-folder']")))
        self.driver.find_element_by_xpath("//button[@data-type='new-folder']").click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        # self.driver.switch_to.default_content()
        self.driver.find_element_by_name("folderName").send_keys("AR")
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, "//input[contains(@class,'invite-selector-input')][@data-keyboard-layer='pill-selector']")))
        element.send_keys("abc@abc.com")
        self.driver.find_element_by_xpath("//button[@data-resin-target='createfolder']").click()

    def logout_box(self):
        element = self.wait.until(ec.presence_of_element_located((By.XPATH, "//button[@data-resin-target='accountmenu']")))
        element.click()
        element = self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Log Out")))
        element.click()

    def close_browser(self):
        self.driver.quit()
