import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.title)

results = soup.find_all("h2")

print(results)

# class = "title is-5" - Job Title
# class = "subtitle is-6 company" - Name of company
# class = "location" - Location