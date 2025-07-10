import os
import sqlite3
from datetime import datetime

# Získání cesty ke složce, kde je skript uložen
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "news.db")

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT UNIQUE,
            source TEXT,
            date_added TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(articles):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today_date = datetime.now().strftime("%Y-%m-%d")
    for article in articles:
        try:
            cursor.execute("""
                INSERT INTO articles (title, link, source, date_added) 
                VALUES (?, ?, ?, ?)
            """, (article["title"], article["link"], article["source"], today_date))
        except sqlite3.IntegrityError:
            continue
    conn.commit()
    cursor.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 5")
    print("✅ Poslední články v databázi:")
    for row in cursor.fetchall():
        print(row)
    conn.close()

