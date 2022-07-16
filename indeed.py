import requests
from openpyxl import Workbook
from openpyxl.styles import Font
from bs4 import BeautifulSoup
import os
import time

start_time = time.time()


wb = Workbook()
ws=wb.active

titleArray = []
companyArray = []
locationArray = []
linkArray = []
salaryArray = []


def page(TitleSearch, LocationSearch):
   for start in range(20):
        URL = "https://uk.indeed.com/jobs?q="+TitleSearch+"%20&l="+LocationSearch+"%20&start={}".format(start * 10)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        jobs = soup.find_all("td", class_="resultContent")
        return jobs
    

def results(jobs, jobWord):
    mainURL = "https://uk.indeed.com"
    
    for job in jobs:
        try:
            title = job.find("a", class_="jcs-JobTitle").text
            company = job.find("span", class_="companyName").text
            location = job.find("div", class_="companyLocation").text
            salary = job.find("div", class_="metadata salary-snippet-container").text
            link = job.find("a").get("href")
        
            if title.find(jobWord) or title.find(jobWord.lower()) != -1:
                titleArray.append(title)
                companyArray.append(company)
                locationArray.append(location)
                salaryArray.append(salary)
                linkArray.append(mainURL + link)
        except:
                pass
    return titleArray, companyArray, locationArray, salaryArray, linkArray
            
            
def publish(titleArray, companyArray, locationArray, salaryArray, linkArray):
    i = 2

    length = len(titleArray)
    
    ws.cell(row=1, column=1, value="Title")
    ws.cell(row=1, column=2, value="Company")
    ws.cell(row=1, column=3, value="Location")
    ws.cell(row=1, column=4, value="Salary")
    ws.cell(row=1, column=5, value="Apply Here")
        
    ws["A1"].font = Font(bold=True)
    ws["B1"].font = Font(bold=True)
    ws["C1"].font = Font(bold=True)
    ws["D1"].font = Font(bold=True)
    ws["E1"].font = Font(bold=True)

    for j in range(0,length):
        ws.cell(row=i, column=1, value=titleArray[j])
        ws.cell(row=i, column=2, value=companyArray[j])
        ws.cell(row=i, column=3, value=locationArray[j])
        ws.cell(row=i, column=4, value=salaryArray[j])
        ws.cell(row=i, column=5).hyperlink = linkArray[j]
        i+=1
        
    wb.save("jobs.xlsx")
    print("File is located at " + os.path.abspath("jobs.xlsx"))
    
def main():
    jobs = page("Software Developer", "London")
    results(jobs, "Developer")
    
    titleArray, companyArray, locationArray, salaryArray, linkArray = results("", "")
    publish(titleArray, companyArray, locationArray, salaryArray, linkArray)
    
    # https://uk.indeed.com/jobs?q=Software%20Developer&l=London&start=10

main()

print(time.time() - start_time)