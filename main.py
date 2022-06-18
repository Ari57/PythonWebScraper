import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


    
    
jobs = soup.find_all("div", class_="card-content")
for job in jobs:
        title = job.find("h2", class_= "title is-5")
        company = job.find("h3", class_="subtitle is-6 company")
        location = job.find("p", class_="location")
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print()
     


# class = "title is-5" - Job Title
# class = "subtitle is-6 company" - Name of company
# class = "location" - Location


