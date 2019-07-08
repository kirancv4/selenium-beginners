"""
Test for choosing sunscreen or moisture.

"""
from selenium import webdriver


# webdriver of chrome.
driver=webdriver.Chrome()
# Maximize the size of the chrome window.
driver.maximize_window()
# Goto URL.
driver.get("https://weathershopper.pythonanywhere.com")
# Fetching the value of temperature from the page.
temperature_read=driver.find_element_by_xpath("//span[@id='temperature']").text.encode('utf-8')
# Printing temperature
print ("The temperature is",temperature_read)
#split the variable and fetch the temperature value
temperature_value=int(temperature_read.split()[0])
# print value
print (temperature_value)
# condition to check below 19 degrees.

def check(valid_page):
    print("I am coming here")
    if valid_page == "Moisturizers":
        print ("page is validated to moisturezer page")
    elif valid_page == "Sunscreens":
        print ("page is validated to Suncreen page")


if temperature_value<=19:
    #to click on the moisturizers button.
    driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
    # Print a message.
    print("landed on moisturizers page")
    #to validate on the landing page.
    # extract the heading of the page
    valid_page = driver.find_element_by_xpath("//h2").text
    print(valid_page)
    check(valid_page)


# condition to check above 34 degrees.    
elif temperature_value>=34:
    #to click on the suncreen button
    driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
    # Print a message.
    print("landed on suncreen page")
    #to validate on the landing page.
    # extract the heading of the page
    valid_page = driver.find_element_by_xpath("//h2").text
    print(valid_page)
    check(valid_page)
driver.close()


    

