import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook()
ws=wb.active

titleArray = []
companyArray = []
locationArray = []
linkArray = []
salaryArray = []

def page(TitleSearch, LocationSearch):
    URL = "https://uk.indeed.com/jobs?q="+TitleSearch+"%20&l="+LocationSearch
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
    j = 0

    length = len(titleArray)

    for j in range(0,length):
        ws.cell(row=1, column=1, value="Title")
        ws.cell(row=1, column=2, value="Company")
        ws.cell(row=1, column=3, value="Location")
        ws.cell(row=1, column=4, value="Salary")
        ws.cell(row=1, column=5, value="Apply Here")     
    
        ws.cell(row=i, column=1, value=titleArray[j])
        ws.cell(row=i, column=2, value=companyArray[j])
        ws.cell(row=i, column=3, value=locationArray[j])
        ws.cell(row=i, column=4, value=salaryArray[j])
        ws.cell(row=i, column=5).hyperlink = linkArray[j]
        i+=1
        j+=1
    wb.save("jobs.xlsx")
    
def main():
    jobs = page("Apprentice Software Developer", "London")
    results(jobs, "Apprentice")
    
    titleArray, companyArray, locationArray, salaryArray, linkArray = results("", "")
    publish(titleArray, companyArray, locationArray, salaryArray, linkArray)
    
  
    
    # https://uk.indeed.com/jobs?q=Software&20Developer%20&l=London

main()
    
    




