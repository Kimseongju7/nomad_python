import get_buttons
import scraping

url = "https://weworkremotely.com/remote-full-time-jobs?page=1"
page_nums = get_buttons.get_buttons(url)
for page_num in range(page_nums):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={page_num + 1}"
    scraping.scrape_page(url)
all_jobs = scraping.all_jobs
print(len(all_jobs))
for job in all_jobs:
    print(job["title"])