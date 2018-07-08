import unittest
from selenium import webdriver


class LinkOnPage(unittest.TestCase):
        hrefList = []

        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.fullscreen_window()
            self.driver.get("https://www.zscaler.com")

        def test_case1(self):
            self.listOfLinks = self.driver.find_elements_by_tag_name("a")
            self.linkCount = len(self.listOfLinks)
            print("Number of links on home page are : ", self.linkCount)
            for i in self.listOfLinks:
                actualLink = i.get_attribute("href")
                self.hrefList.append(actualLink)
                print(actualLink)

        # def test_case2(self):
        #     for el in self.hrefList:
        #         if not el or el is None:
        #             continue
        #         else:
        #             self.driver.get(el)
        #             print(self.driver.title)

        def tearDown(self):
                self.driver.close()
                
                
if __name__ == '__main__':
    unittest.main()
