from bs4 import BeautifulSoup
import requests


def extract_berin_jobs(keyword):
    url =  f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    berlin_jobs = []
    response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser")
    pages = len(soup.find("ul", class_="bsj-nav").find_all("a"))
    if not pages:
        pages = 1
    for page in range(pages):
        tmp_url = f"{url}page/{page+1}/"
        print(f"Scrapping {tmp_url}")
        resp = requests.get(tmp_url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(resp.content, "html.parser")
    jobs = soup.find_all('li', class_="bjs-jlid")
    for job in jobs:
        company = job.find('a', class_="bjs-jlid__b").text
        title = job.find('h4', class_="bjs-jlid__h").find('a').text
        description = job.find('div', class_="bjs-jlid__description").text.strip()
        link = job.find('h4', class_="bjs-jlid__h").find('a')["href"]
        berlin_jobs.append({
            "company": company,
            "title": title,
            "description": description,
            "url": link
        })
    return berlin_jobs
