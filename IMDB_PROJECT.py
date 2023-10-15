import openpyxl as openpyxl
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# source = "https://www.imdb.com/chart/top/"
# driver = webdriver.Chrome()
# driver.get(source)
file = openpyxl.Workbook()
sheet = file.active
sheet.title = 'Top rated movies'
sheet.append(['Rank', 'Movie Name', 'Year', 'Rating'])
print(sheet)
try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()  # For capturing error
    # m = []
    Names = []
    soup = BeautifulSoup(source.text, 'html.parcer')
    # movies = driver.find_elements(By.XPATH, "//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-between "
    #                                         "sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base']//li")

    # for movie in movies:
    #     Details = movie.text
    #     sheet.append(Details)

    movies = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj "
                                    "compact-list-view ipc-metadata-list--base").find_all('li')




except Exception as e:
    print(e)

# //ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"]//li[
file.save('IMDB Project.csv')
