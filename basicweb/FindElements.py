import selenium.webdriver as webdriver
import time




class BrowserInfo():

    def open(self):
        baseUrl = "https://shopbagg.inone.useinsider.com/web-social-proof"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)


        driver.find_element_by_id("email").send_keys("sumeyye.erdogan@useinsider.com")
        driver.find_element_by_id("password").send_keys(" ")
        driver.find_element_by_id("login-button").click()
        driver.implicitly_wait(10)

        #1
        #elementbyId = driver.find_element_by_id("enableUtmSettings")

        #if elementbyId is not None:
        #print("We found an element")

        #2

        #input_SMS =driver.find_element_by_xpath("//div[@id='smsMessageAttribute']")
        #input_SMS.send_keys("")
        #print(driver.find_element_by_xpath("//p[.='The Your Message field is required.']").text)

        #3
        #input_SearchValue = driver.find_element_by_xpath("//input[@id='search-value']")
        #input_SearchValue.send_keys("test")

        #4
        #radiobutton_test = driver.find_element_by_xpath("//input[@id='Test']")
        #radiobutton_test.click()

        #driver.find_element_by_id("maybe-later").click()
        #time.sleep(5)

        #5
        #button_statistics = driver.find_elements_by_class_name("statistics")
        #button_statistics = driver.find_elements_by_css_selector(".vuetable-slot.test-link")

        #button_statistics[0].click()
        #time.sleep(5)

        #6
        #button_delete = driver.find_element_by_class_name("in-button-wrapper.qa-button.w-1.in-button-wrapper_text-alert")
        #button_delete.click()

        #time.sleep(3)

        #7
        #driver.find_element_by_xpath('//button[@id = "Delete"]').click()
        #driver.find_element_by_link_text("Delete").click()
        #change = driver.find_elements_by_xpath("//p[contains(text(),'Delete')]")[1]
        #change.click()
        #time.sleep(2)
        #driver.find_element_by_class_name("textButton.textBlue").click()
        #8
        #a = driver.find_element_by_id("sms-41")
        #time.sleep(4)
        #a.click()
        #time.sleep(5)
        #driver.find_element_by_id("smsMessageAttribute").send_keys(" ")
        #driver.find_element_by_name("submitButton").click()
        #time.sleep(6)
        #print(driver.find_elements_by_class_name("messageAlertBoxIcon"))

        #9
        #button = driver.find_element_by_class_name("btnBlue")
        #button.click()
        #time.sleep(4)
        #driver.find_element_by_class_name("inputBlock").send_keys("test1237777")
        #driver.find_element_by_class_name("textButton.textBlue").click()
        #time.sleep(5)
        #driver.find_element_by_class_name("in-button-wrapper_primary-default").click()
        #time.sleep(7)












        


ff = BrowserInfo()
ff.open()