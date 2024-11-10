import requests
from bs4 import BeautifulSoup
from click import style


def extract_web3_jobs(keyword):
    print("web3 Scraping")
    url =  f"https://web3.career/{keyword}-jobs"
    web3_jobs = []
    response = requests.get(url, headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    })
    soup = BeautifulSoup(response.content, "html.parser")
    pages = len(soup.find_all('a', class_="page-link")) - 3
    for page in range(pages):
        tmp_url = f"{url}?page={page+1}"
        print(f"Scrapping {tmp_url}")
        tbody = soup.find('tbody')
        jobs = tbody.find_all('tr')
        for job in jobs:
            company = job.find('h3')
            if not company:
                continue
            company = company.text
            title = job.find('h2').text
            description = job.find('a', style="font-size: 12px; color: #d5d3d3;")
            if description:
                description = description.text
            else:
                description = "remote"
            link = job.find('a')["href"]
            link = f"https://web3.career/{link}"
            web3_jobs.append({
                "company": company,
                "title": title,
                "description": description,
                "link": link
            })
    return web3_jobs

extract_web3_jobs("python")