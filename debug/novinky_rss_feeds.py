import requests
from bs4 import BeautifulSoup

def debug_feed():
    resp = requests.get("https://www.novinky.cz/rss")
    soup = BeautifulSoup(resp.content, "xml")
    items = soup.find_all("item")

    for item in items:
        title = item.find("title").text.strip()
        category = item.find("category").text.strip() if item.find("category") else "Bez kategorie"
        print(f"📰 {title}  [{category}]")

if __name__ == "__main__":
    debug_feed()

