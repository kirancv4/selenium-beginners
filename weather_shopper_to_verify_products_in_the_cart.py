"""
Verify the cart
"""
from selenium import webdriver
import time
# webdriver of chrome.
driver=webdriver.Chrome()
# Maximize the size of the chrome window.
driver.maximize_window()
# Goto URL.
driver.get("https://weathershopper.pythonanywhere.com/sunscreen")

# get all prices of sunscreen
all_products=driver.find_elements_by_xpath("//div[@class='text-center col-4']")

# Initialize min_product_spf50 & min_productspf30 to null.
min_product_spf50=""
min_price_spf50=1000
min_product_spf30=""
min_price_spf30=1000
print("Product Details")

# Get all the objects split and get the highest priced sunscreen.
for each_product in all_products:
    each_product_text = each_product.text
    #Getting each prouct name and its price
    product_name=each_product_text.split("Price")[0].strip()
    product_price=each_product_text.split(" ")[-1]
    product_price=int(product_price.split("\n")[-2])    
    #print("Product Name",product_name)
    #print("Product price",product_price)  
    # condition to check if the product is spf-50
    if product_name.split(" ")[-1] == "spf-50" or product_name.split(" ")[-1] == "SPF-50":
        if min_price_spf50 >= product_price:            
            min_price_spf50 = product_price
            min_product_spf50 = product_name
    # condition to check if the product is spf-30        
    elif product_name.split(" ")[-1] == "spf-30" or product_name.split(" ")[-1] == "SPF-30":
        if min_price_spf30 >= product_price:
            min_price_spf30=product_price
            min_product_spf30=product_name

print("The minimun product of SPF-50 is ",min_product_spf50)
print("The price is ",min_price_spf50)
print("The minimun product of SPF-30 is ",min_product_spf30)
print("The price is ",min_price_spf30)


sum_of_items=0
sum_of_items = min_price_spf50 + min_price_spf30
print("sum of the items",sum_of_items)

#To click add button of min spf-50.
driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(min_product_spf50)).click()
#To click add button of min spf-30.
driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"%(min_product_spf30)).click()
# To verify the items in the cart is the same which are added


driver.find_element_by_xpath("//button[@onclick='goToCart()']").click()
time.sleep(2)
#cart webpage heading
cart_heading=driver.find_element_by_xpath("//H2[text()='Checkout']").text
print ("Heading is ",cart_heading)
#Get the products and its prices

#table=driver.find_elements_by_xpath("//tr")
table=driver.find_elements_by_xpath("//tbody")


# get each products in the table.
flag=0
print("Products In Table")
for each_product_table in table:
    each_product_table_text=each_product_table.text
    print(each_product_table_text)
    if (min_product_spf30) in each_product_table_text or (min_product_spf50) in each_product_table_text:
        #print("product is matched")
        flag=1

if flag==0:
    print("Product didnt match")
else:
    print("Product Matches")
# Get total of the products
sum_in_cart=(driver.find_element_by_xpath("//p[@id='total']").text)
sum_in_cart=int(sum_in_cart.split(" ")[-1])
print("Total in cart",sum_in_cart)
if (sum_of_items==sum_in_cart):
    print("Total of the products Match")
else:
    print("Total dosent Match")



