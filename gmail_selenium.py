"""
gmail selenium
"""
import time
from selenium import webdriver
driver=webdriver.Chrome() #Create an object webdriver
driver.maximize_window()  #To maximize the Browser window
driver.get("https://mail.google.com") #To fetch the URL
time.sleep(3) #wait for 3 seconds
mail_id=driver.find_element_by_xpath("//input[@type='email']") #Get to the Email ID text box
mail_id.send_keys("kiran.cv@qxf2.com") #Enter the id into the textbox
driver.find_element_by_xpath("//span[text()='Next']").click() # get the location of the Next button and click on it
time.sleep(7) #wait for 3 seconds
mail_pass=driver.find_element_by_xpath("//input[@type='password']")#Get to the password Text box
mail_pass.send_keys("kingdom!@#")#Enter the password
driver.find_element_by_xpath("//span[text()='Next']").click()#Locate the Next Button and click on it
time.sleep(10)#sleep for 10 seconds
driver.find_element_by_xpath("//div[@gh='cm']").click()#Locate compose button and click on ot
time.sleep(4)
driver.find_element_by_xpath("//textarea[@name='to']").send_keys("kiran.cv@qxf2.com")#Enter receptient mail adress into the To field
driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("selenium testing")#Enter data into subject field
driver.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys("this is a test to compose a mail using selenium")#Enter data into the Email body.
driver.find_element_by_xpath("//div[@aria-label='Send ‪(Ctrl-Enter)‬']").click()#Locate and click on the send button
time.sleep(5)
driver.find_element_by_xpath("//img[@src='https://www.google.com/a/cpanel/qxf2.com/images/logo.gif?service=google_gsuite']").click()#click on the menu button
time.sleep(1)
driver.find_element_by_xpath("//a[text()='Sign out']").click()#click on logout
driver.close()