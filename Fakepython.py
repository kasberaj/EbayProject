import openpyxl
from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"
file = openpyxl.Workbook()
sheet = file.active
sheet.title = 'Fake jobs'
sheet.append(['Job Title'])
all_data = requests.get(url)
# print(all_data.text)

soup = BeautifulSoup(all_data.content, 'html.parser')
results = soup.select('div div.media-content h2')
titles = results

for title in titles:
    title = title.text

    print(title)

    # sheet.append(title)
# for job in job_title:
#     print(job.text)
file.save('FakePython.csv')