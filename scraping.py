import re
import requests
from bs4 import BeautifulSoup
all_jobs = []

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[:-1]
    for job in jobs:
        title = job.find("span", class_="title").text
        company, position, region = job.find_all("span", class_="company")
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        job_data = {
            "title" : title,
            "company" : company.text,
            "position" : position.text,
            "region" : region.text,
            "url" :  f"https://weworkremotely.com/{url}"
        }
        all_jobs.append(job_data)
