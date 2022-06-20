import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

def jobSearch(jobWord):
    job = soup.find_all("h2", string=lambda text: jobWord in text.lower()) # find all jobs with 'python' in their name

    jobs = [h2_element.parent.parent.parent for h2_element in job] # TODO

    for job in jobs: # iterate through the entire div containing the jobs, rather than just search for h2 elements
        title = job.find("h2", class_= "title is-5")
        company = job.find("h3", class_="subtitle is-6 company")
        location = job.find("p", class_="location")
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print()


def main():
    jobSearch("engineer")
    
main()



# class = "title is-5" - Job Title
# class = "subtitle is-6 company" - Name of company
# class = "location" - Location
