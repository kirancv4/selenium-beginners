"""
To add the lowest priced aloe and almond of moisturizer
"""
from selenium import webdriver
import time
# webdriver of chrome.
driver=webdriver.Chrome()
# Maximize the size of the chrome window.
driver.maximize_window()
# Goto URL.
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")

# get all prices of sunscreen
all_products=driver.find_elements_by_xpath("//div[@class='text-center col-4']")

# Initialize min_product_aloe & min_products_almond to null.
min_product_aloe=""
min_price_aloe=1000
min_product_almond=""
min_price_almond=1000
print("Product Details")
# Get all the objects split and get the highest priced sunscreen.
for each_product in all_products:
    each_product_text = each_product.text
    #Getting each prouct name and its price
    product_name=each_product_text.split("Price")[0].strip()
    product_price=each_product_text.split(" ")[-1]
    product_price=int(product_price.split("\n")[-2])
    print("Product Name",product_name)
    print("Product price",product_price)
    # condition to check if the product is aloe moisturizer.
    if "aloe" in product_name.split(" ") or "Aloe" in product_name.split(" "):
        if min_price_aloe >= product_price:            
            min_price_aloe = product_price
            min_product_aloe = product_name
    # condition to check if the product is almond moisturizer.
    elif "almond" in product_name.split(" ") or "Almond" in product_name.split(" "):
        if min_price_almond >= product_price:
            min_price_almond=product_price
            min_product_almond=product_name

#To click add button of min aloe moisturizer.
driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(min_product_aloe)).click()
#To click add button of min almond moisturizer.
driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(min_product_almond)).click()
#driver.close()



print("The minimun product of Aloe moisturizer is ",min_product_aloe)
print("The price is ",min_price_aloe)  
print("The minimun product of Almond moisturizer is ",min_product_almond)
print("The price is ",min_price_almond)         


