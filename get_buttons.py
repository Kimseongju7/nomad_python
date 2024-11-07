import re
import requests
from bs4 import BeautifulSoup
import scraping

def get_buttons(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))
