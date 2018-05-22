from selenium import webdriver


class Test_Company_Contact:

        driver = webdriver.Chrome()
        driver.fullscreen_window()
        driver.get("https://www.zscaler.com/company/contact")
        driver.fullscreen_window()
        print("\n==================================================\n")
        print(driver.title)
        assert "Contact Us | Internet Security Platform | Zscaler" in driver.title
        driver.find_element_by_id("FirstName").send_keys("Test Profile")
        driver.find_element_by_id("LastName").send_keys("Test Profile")
        driver.find_element_by_id("Company").send_keys("Zscaler")
        driver.find_element_by_id("Email").send_keys("rkaushal@zscaler.com")

        """Company Size dropdown section  """
        driver.find_element_by_xpath("//div[contains(@class,'selectize-control')]//input[@placeholder='Company size']").click()
        driver.find_element_by_css_selector("div[data-value='1 - 100']").click()

        """Country dropdown section   """
        driver.find_element_by_xpath("//div[contains(@class,'selectize-input')]//input[@id='Country-selectized']").click()
        driver.find_element_by_xpath("//div[contains(@class,'selectize-dropdown-content')]//div[@data-value='USA']").click()

        """Area of Interest dropddown  section  """
        driver.find_element_by_xpath("//div[contains(@class,'selectize-input')]/input[@id='Areas_of_Interest__c-"
                                     "selectized']").click()
        driver.find_element_by_css_selector("div[data-value='Pricing Info']").click()

        driver.find_element_by_xpath("//*[@id='Info_Request_Notes__c']").send_keys("Testing Purposes")
        driver.implicitly_wait(3000)
        driver.find_element_by_xpath("//*[@id='Single_OptIn__c']").click()
        # driver.find_element_by_xpath("//*[@id='btn-form-contact-us']").click()
        # driver.close()


def main():
    pass


if __name__ == 'main':
        main()