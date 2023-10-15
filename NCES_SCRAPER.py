import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the NCES website
Source = "https://nces.ed.gov/ccd/schoolsearch/"
driver.get(Source)

try:
    # Find the search input field and type "A" in it
    search_Box = driver.find_element(By.NAME, "InstName")
    # Entering 'A' in search Bos
    search_Box.send_keys("A")

    # Click the Search button
    Search_button = driver.find_element(By.XPATH, "//input[@value='  Search  ']")
    # Click on Search Button
    Search_button.click()

    # Wait for the search results to load
    # Wait for element to visible
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[3]/table[3]/tbody[1]"))
    )

    # Extract data from the search results //tbody/tr[position()=1]/td
    School_Details = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/table[3]/tbody[1]")

    School_Data = []

    for school_names in School_Details:
        name = school_names.text
        address_element = school_names.find_element(By.XPATH, "//tbody//tr//td//strong")
        address = address_element.text
        phone_element = school_names.find_element(By.XPATH, "//tbody//tr//td//strong")
        phone = phone_element.text

        # Append the data to the list
        School_Data.append([name, address, phone])

    # Store the scraped data in a CSV file
    df = pd.DataFrame(School_Data, columns=["Name", "Address", "Phone"])
    df.to_csv("schools_data.csv", index=False)
    # Print success message
    print("Data scraped and saved to schools_data.csv")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver
    driver.quit()
