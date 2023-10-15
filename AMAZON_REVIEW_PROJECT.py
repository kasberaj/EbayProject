from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import pandas as pd

# driver = webdriver.Chrome()
url = "https://www.amazon.in/New-Apple-iPhone-Mini-128GB/product-reviews/B08L5VN68Y/ref=cm_cr_dp_d_show_all_btm?ie" \
      "=UTF8&reviewerType=all_reviews"
# driver.get(url)

source = requests.get(url)
soup = bs(source.content, 'html.parser')
# print(soup.prettify())

names = soup.find_all('span', class_="a-profile-name")
Cust_name = []
for i in range(len(names)):
    Cust_name.append(names[i].getText())
    print(names)
