from requests import get

websites = [
    "google.com", "airbnb.com", "https://twitter.com", "facebook.com",
    "https://tiktok.com"
]

result = {}

for website in websites:
    if not website.startswith("https://"):
        website = "https://" + website
    response = get(website)
    if response.status_code == 100:
        result[website] = "continue"
    elif response.status_code == 101:
        result[website] = "switching protocols"
    elif response.status_code >= 500:
        result[website] = "server error"
    elif response.status_code >= 400:
        result[website] = "client error"
    elif response.status_code >= 300:
        result[website] = "redirection"
    else:
        result[website] = "success"

print(result)
