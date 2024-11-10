from flask import Flask, render_template, request
from extract_berlin_jobs import extract_berin_jobs
from flack_assignment.extract_weremotely_jobs import extract_weremotely_jobs
from extract_web3_jobs import extract_web3_jobs

app = Flask("JobScrapper")

"""
Do this when scraping a website to avoid getting blocked.

headers = {
      'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept':
      'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
}

response = requests.get(URL, headers=headers)
"""

db = { }
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        berlin = extract_berin_jobs(keyword)
        we_remote = extract_weremotely_jobs(keyword)
        web3 = extract_web3_jobs(keyword)
        jobs = berlin + we_remote + web3
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs = jobs)

app.run()

if __name__ == "__main__":
    app.run()