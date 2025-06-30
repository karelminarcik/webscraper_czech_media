import requests
from bs4 import BeautifulSoup
from common.keywords import contains_keywords  # Ověř, že soubor existuje a funkce funguje

def scrape():
    URL = "https://www.novinky.cz/rss"
    print(f"📡 Načítám RSS feed z: {URL}")
    articles = []

    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException as e:
        print(f"❌ Chyba při načítání RSS: {e}")
        return articles

    if response.status_code != 200:
        print(f"❌ Neúspěšná odpověď: {response.status_code}")
        return articles

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")
    print(f"🔍 Nalezeno {len(items)} článků v RSS feedu.")

    for item in items:
        try:
            title_tag = item.find("title")
            link_tag = item.find("link")
            category_tag = item.find("category")

            title = title_tag.text.strip() if title_tag else ""
            link = link_tag.text.strip() if link_tag else ""
            category = category_tag.text.strip().lower() if category_tag else "žádná"

            print(f"\n📄 Titulek: {title}")
            print(f"🔗 Odkaz: {link}")
            print(f"🏷️ Kategorie: {category}")

            # Můžeš přidat zpět podmínku if "domácí" in category: pokud chceš později filtrovat

            if contains_keywords(title):
                print("✅ Klíčové slovo nalezeno, článek uložen.")
                articles.append({
                    "title": title,
                    "link": link,
                    "source": "novinky.cz"
                })
            else:
                print("❌ Titulek neobsahuje klíčové slovo.")
        except Exception as e:
            print(f"⚠️ Chyba při zpracování článku: {e}")

    print(f"\n✅ Scraping novinky.cz dokončen, uloženo: {len(articles)} článků.")
    return articles


# Testovací běh
if __name__ == "__main__":
    news = scrape()
    print("\n📰 Výpis nalezených článků:")
    for article in news:
        print(f"- {article['title']} ({article['link']})")
