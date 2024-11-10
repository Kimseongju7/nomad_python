from extract_berlinstartupjobs import extract_berin_jobs
from file import save_to_file
from flask import Flask, render_template, request

app = Flask("JobScraper")

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
        jobs = berlin
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs = jobs)

app.run()