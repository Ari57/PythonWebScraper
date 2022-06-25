import requests
from bs4 import BeautifulSoup

URL = "https://uk.indeed.com/jobs?q=Software%20Developer&l=London&from=searchOnHP&vjk=9872bb840bcc17a6"
mainURL = "https://uk.indeed.com"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

jobs = soup.find_all("td", class_="resultContent")
jobsTest = soup.find_all("a", class_="tapItem")

links = [mainURL+a["href"] for a in soup.select("a.tapItem")]
print(links)

for job in jobs:
    title = job.find("a", class_="jcs-JobTitle")
    company = job.find("span", class_="companyName")
    location = job.find("div", class_="companyLocation")
   
    
    try: 
        print("Job Title: " + title.text)
        print("Company: " + company.text)
        print("Location: " + location.text)
        # print("Apply here: " + link)
        print()
    except:
        pass




