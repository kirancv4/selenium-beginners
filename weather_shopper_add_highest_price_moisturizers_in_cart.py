"""
To add only the highest price moisturizers in cart.
"""
from selenium import webdriver
import time
# webdriver of chrome.
driver=webdriver.Chrome()
# Maximize the size of the chrome window.
driver.maximize_window()
# Goto URL.
driver.get("https://weathershopper.pythonanywhere.com/moisturizers")

# get all prizes of moisturizers.
all_prizes=driver.find_elements_by_xpath("//div[@class='text-center col-4']")
# Initialize max_product & max_prize to null.
max_product=""
max_prize=0
# Get all the objects split and get the highest priced moisturizers.
for each_product in all_prizes:
    each_product_text = each_product.text
    #print(each_product_text)
    product_name=each_product_text.split("Price")[0].strip()
    product_prize=each_product_text.split(" ")[-1]
    product_prize=int(product_prize.split("\n")[-2])
    #print(product_name)
    #print(product_prize)
    if max_prize<product_prize:
        max_product=product_name        
        max_prize=product_prize
# Max product and Max prize
print("\n",max_product)
print("\n",max_prize)
time.sleep(10)

# to click add
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.execute_script("window.scrollTo(0, 700)")
#time.sleep(10)
#driver.find_element_by_xpath("//button[@onclick,'addToCart('%s',%d)']"%(max_product,max_prize)).click()
driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(max_product)).click()

    







