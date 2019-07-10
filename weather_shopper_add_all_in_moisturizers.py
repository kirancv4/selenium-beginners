"""
Program to add all the items in the Moisturizers page into the cart
"""
import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)
#check if have landed on the correct page
if(driver.find_element_by_xpath("//H2").text=="Moisturizers"):
    print("Successfully entered the sunscreen shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)

#find the location of the cart
cart_before=driver.find_element_by_xpath("//BUTTON[@onclick='goToCart()']").text
#extract the quantity of items in the cart
cart_before_split=cart_before.split()[-1]
print(cart_before_split)

# Get all the add buttons
for i in range(1,7):
    	driver.find_element_by_xpath("(//BUTTON[contains(@class,'btn btn-primary')][text()='Add'])[%d]"%i).click()


# location of the cart after adding items
cart_button=driver.find_element_by_xpath("//BUTTON[@onclick='goToCart()']").text
print(cart_button)
#extract the quantity of items in the cart
cart_items_quantity=cart_button.split()[2]
print(cart_items_quantity)

#check if the cart before matches with cart after adding item
if(cart_items_quantity==cart_before_split):
    print("Failed to add items into the cart")

driver.close()