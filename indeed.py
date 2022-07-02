import requests
import pandas as pd
from openpyxl import Workbook
from bs4 import BeautifulSoup


URL = "https://uk.indeed.com/jobs?q=Software%20Developer&l=London&from=searchOnHP&vjk=478ec0670e968d98"
mainURL = "https://uk.indeed.com"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

jobs = soup.find_all("td", class_="resultContent")


wb = Workbook()
ws=wb.active


titleArray = []
companyArray = []
locationArray = []
linkArray = []

for job in jobs:
    try:
        title = job.find("a", class_="jcs-JobTitle")
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        link = job.find("a").get("href")
        
        titleArray.append(title.text)
        companyArray.append(company.text)
        locationArray.append(location.text)
        linkArray.append(mainURL + link)
    except:
        pass
    
    
i = 2
j = 0

length = len(titleArray)

for j in range(0,length):
    ws.cell(row=1, column=1, value="Title")
    ws.cell(row=1, column=2, value="Company")
    ws.cell(row=1, column=3, value="Location")
    ws.cell(row=1, column=4, value="Apply Here")     
    
    ws.cell(row=i, column=1, value=titleArray[j])
    ws.cell(row=i, column=2, value=companyArray[j])
    ws.cell(row=i, column=3, value=locationArray[j])
    ws.cell(row=i, column=4, value=linkArray[j])
    i+=1
    j+=1
    
wb.save("jobs.xlsx")

    
# append it to a list
# as the row increases, we move along one position in the array


