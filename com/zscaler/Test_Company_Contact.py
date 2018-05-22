from selenium import webdriver


class Test_Company_Contact:

        driver = webdriver.Chrome()
        # driver.fullscreen_window()
        driver.get("https://www.zscaler.com/company/contact")
        driver.fullscreen_window()
        print("\n==================================================\n")
        print(driver.title)
        assert "Contact Us | Internet Security Platform | Zscaler" in driver.title
        driver.find_element_by_id("FirstName").send_keys("Test Profile")
        # driver.find_elements_by_xpath("//input[@id='FirstName']")[0].send_keys("Test Profile")
        driver.find_elements_by_xpath("//input[@id='LastName']")[0].send_keys("Test Profile")
        driver.find_elements_by_xpath("//input[@id='Company']")[0].send_keys("Zscaler")
        driver.find_elements_by_xpath("//input[@id='Email']")[0].send_keys("rkaushal@zscaler.com")

        """Company Size dropdown section  """
        driver.find_element_by_xpath("//div[contains(@class,'selectize-control')]//input[@placeholder='Company size']").click()
        driver.find_element_by_css_selector("div[data-value='1 - 100']").click()
        list_comp_size = []
        # list_comp_size = driver.find_elements_by_xpath("//*[@id='myform']/div[4]/div[1]/div/div[1]/div[2]/div")

        """Country dropdown section   """
        driver.find_elements_by_xpath("//*[@id='myform']/div[4]/div[2]/div/div[1]/div[1]")[0].click()
        list_country = []
        # list_country = driver.find_elements_by_xpath("//*[@id='myform']/div[4]/div[2]/div/div[1]/div[2]/div")

        """Area of Interest dropddown  section  """
        driver.find_elements_by_xpath("//*[@id='myform']/div[5]/div/div/div[1]/div[1]")[0].click()
        list_interest = []
        # list_interest=driver.find_elements_by_xpath("//*[@id='myform']/div[5]/div/div/div[1]/div[2]/div")

        driver.find_elements_by_xpath("//*[@id='Info_Request_Notes__c']")[0].send_keys("Testing Purposes")
        driver.implicitly_wait(3000)
        driver.find_elements_by_xpath("//*[@id='Single_OptIn__c']")[0].click()
        driver.find_elements_by_xpath("//*[@id='btn-form-contact-us']")[0].click()
        # driver.close()


def main():
    pass


if __name__ == 'main':
        main()

