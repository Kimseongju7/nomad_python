from bs4 import BeautifulSoup
import requests

job_datas = []

class Job:
    def __init__(self, company, title, description, url):
        self.company = company
        self.title = title
        self.des = description
        self.url = url
    def __str__(self):
        return f"company : {self.company}, title : {self.title}\ndescription : {self.des}\nurl : {self.url}"

def web_scrapper(url):
    response = requests.get(url, headers={"User-Agent":"user info"})
    soup = BeautifulSoup(response.content, "html.parser")
    pages = len(soup.find("ul", class_="bsj-nav").find_all("a"))
    if not pages:
        pages = 1
    for page in range(pages):
        tmp_url = f"{url}page/{page+1}/"
        print(tmp_url)
        resp = requests.get(tmp_url, headers={"User-Agent":"user info"})
        soup = BeautifulSoup(resp.content, "html.parser")
        jobs = soup.find_all('li', class_="bjs-jlid")
        for job in jobs:
            company = job.find('a', class_="bjs-jlid__b").text
            title = job.find('h4', class_="bjs-jlid__h").find('a').text
            description = job.find('div', class_="bjs-jlid__description").text.strip()
            link = job.find('h4', class_="bjs-jlid__h").find('a')["href"]
            job_data = Job(company=company, title=title, description=description, url=link)
            job_datas.append(job_data)
        print(len(job_datas))

skils = ['python', 'typescript', 'javascript']
urls = ['https://berlinstartupjobs.com/engineering/']
for skil in skils:
    urls.append(f"https://berlinstartupjobs.com/skill-areas/{skil}/")
for url in urls:
    web_scrapper(url=url)
print(len(job_datas))