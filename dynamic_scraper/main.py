from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.wanted.co.kr/")
#page.screenshot(path = "screenshot.png")
time.sleep(3)

#page.click("button.Aside_searchButton__rajGo Aside_isNotMobileDevice__hTNEe") #첫번째 클래스만 가지고 와야 했네
#page.locator("button.Aside_searchButton__rajGo").click()
page.click("button.Aside_searchButton__rajGo")
time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(3)

page.keyboard.down("Enter")
time.sleep(3)

page.click("a#search_tab_position")
time.sleep(3)


for i in range(5):
    page.keyboard.down("End")
    time.sleep(1)

content = page.content()
p.stop()

soup = BeautifulSoup(content, "html.parser")
jobs = soup.find_all("div", class_ = "JobCard_container__REty8 JobCard_container--variant-card__gaJS_")
job_datas = []

class Job:
    def __init__(self, link, title, company, reward):
        self.link = link
        self.title = title
        self.company = company
        self.reward = reward
    def __str__(self):
        return f"Title: {self.title}, Company: {self.company}, Reward: {self.reward}\nLink: {self.link}"

for job in jobs :
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
    title = job.find("strong", class_ = "JobCard_title__HBpZf").text
    company = job.find("span", class_= "JobCard_companyName__N1YrF").text
    reward = job.find("span", class_ = "JobCard_reward__cNlG5").text
    job_datas.append({
        "title": title,
        "company": company,
        "reward": reward,
        "link": link
    })

file = open("jobs.csv", mode = "w")
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Reward", "Link"])
for job in job_datas:
    writer.writerow(list(job.values()))

