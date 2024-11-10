import requests
from bs4 import BeautifulSoup

def extract_weremotely_jobs(keyword):
    print("weremote Scraping")
    url =  f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    print(f"Scrapping{url}")
    weremote_jobs = []
    response = requests.get(url, headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    })
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all('li', class_="feature")
    for job in jobs:
        company = job.find('span', class_="company").text
        title = job.find('span', class_="title").text
        description = job.find('span', class_="region company").text
        link = job.find('a')["href"]
        link = f"https://weworkremotely.com{link}"
        weremote_jobs.append({
            "company": company,
            "title": title,
            "description": description,
            "link": link
        })
    return weremote_jobs

