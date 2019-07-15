from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()

#click pay with card

driver.get("https://weathershopper.pythonanywhere.com/cart")
driver.find_element_by_xpath("//span[contains(text(),'Pay with Card')]").click()
time.sleep(5)
driver.switch_to.frame("stripe_checkout_app")
driver.find_element_by_xpath("//input[@type='email']").send_keys("cvk@gmail.com")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Card number']").send_keys("4000056655665556")

time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys("12/20")

time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='CVC']").send_keys("120")

time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys("560019")


time.sleep(1)
driver.find_element_by_xpath("//div[@class='Checkbox-tick']").click()

time.sleep(3)
driver.find_element_by_xpath("//input[@autocomplete='mobile tel']").send_keys("9738102762")

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(4)

heading=driver.find_element_by_xpath("//h2").text
if heading=="PAYMENT SUCCESS":
    print("Payment is sucessful and landed on confirmation page.")
else:
    print("Payment not sucessful!!!")
driver.close()
