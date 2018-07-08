import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import requests


class ImagesOnPage(unittest.TestCase):
    srcList = []

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.fullscreen_window()

    def test_case1(self):
        self.driver.get("https://www.zscaler.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='/Users/Reports/'))
