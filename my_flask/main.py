from extract_berlinstartupjobs import extract_berin_jobs
from file import save_to_file
from flask import Flask, render_template, request

app = Flask("JobScraper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    return render_template("search.html", keyword=keyword)

app.run()