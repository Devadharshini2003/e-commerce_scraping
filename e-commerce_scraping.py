from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument('--headless')  

driver = webdriver.Chrome()


source1 = "https://www.flipkart.com/apple-iphone-14-pro-space-black-256-gb/p/itmbf9b9d0d108a7?pid=MOBGHWFHMSKYWVTR&lid=LSTMOBGHWFHMSKYWVTR5JKE5U&marketplace=FLIPKART&q=iphone+14+pro&store=tyy%2F4io&srno=s_1_7&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&fm=organic&iid=c6ae1ce8-5480-43d5-b08c-51393404329e.MOBGHWFHMSKYWVTR.SEARCH&ppt=hp&ppn=homepage&ssid=p6hew7z6hc0000001697173735076&qH=73a41d19c3188cc2"
source2 ="https://www.amazon.in/Apple-iPhone-Pro-256GB-Gold/dp/B0BDJ8WMV7/ref=sr_1_6?crid=3JW8PPSLKZ6WM&keywords=iphone+14&qid=1697204308&sprefix=%2Caps%2C294&sr=8-6"
# Navigate to the URL
driver.get(source1)


print("Connecting to Flipkart")


f_price = driver.find_element(By.CSS_SELECTOR, '._30jeq3._16Jk6d')
pr_name = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span')
product = pr_name.text
r_price = f_price.text

print(product)
print(r_price)
print(" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(3)

driver.get(source2)

print("Connecting to Amazon....")


wait = WebDriverWait(driver, 20)

pr_name = driver.find_element(By.XPATH, '//*[@id="productTitle"]')
f_price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]')

product = pr_name.text
r_price = f_price.text
print(product)
print(r_price)


# Close the WebDriver
driver.quit()
