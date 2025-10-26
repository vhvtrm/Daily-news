"""
Database module for storing and retrieving news items
"""
import sqlite3
import json
from datetime import datetime
from typing import List, Optional
from models import NewsItem, NewsCategory


class NewsDatabase:
    """Manages news storage in SQLite database"""

    def __init__(self, db_path: str = "vietnam_news.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                tickers TEXT,
                date TEXT NOT NULL,
                source TEXT,
                url TEXT,
                summary TEXT,
                importance INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    def add_news(self, news: NewsItem) -> int:
        """Add a news item to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO news_items (title, category, tickers, date, source, url, summary, importance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            news.title,
            news.category.value,
            json.dumps(news.tickers),
            news.date.isoformat(),
            news.source,
            news.url,
            news.summary,
            news.importance
        ))

        news_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return news_id

    def get_all_news(self, limit: Optional[int] = None) -> List[NewsItem]:
        """Retrieve all news items from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = 'SELECT * FROM news_items ORDER BY date DESC, id DESC'
        if limit:
            query += f' LIMIT {limit}'

        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        news_items = []
        for row in rows:
            news_items.append(NewsItem(
                id=row[0],
                title=row[1],
                category=NewsCategory(row[2]),
                tickers=json.loads(row[3]) if row[3] else [],
                date=datetime.fromisoformat(row[4]),
                source=row[5],
                url=row[6],
                summary=row[7],
                importance=row[8]
            ))

        return news_items

    def get_news_by_category(self, category: NewsCategory) -> List[NewsItem]:
        """Get news items by category"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM news_items WHERE category = ? ORDER BY date DESC
        ''', (category.value,))

        rows = cursor.fetchall()
        conn.close()

        news_items = []
        for row in rows:
            news_items.append(NewsItem(
                id=row[0],
                title=row[1],
                category=NewsCategory(row[2]),
                tickers=json.loads(row[3]) if row[3] else [],
                date=datetime.fromisoformat(row[4]),
                source=row[5],
                url=row[6],
                summary=row[7],
                importance=row[8]
            ))

        return news_items

    def get_news_count(self) -> int:
        """Get total number of news items"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM news_items')
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def clear_all_news(self):
        """Clear all news items from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM news_items')
        conn.commit()
        conn.close()

    def search_by_ticker(self, ticker: str) -> List[NewsItem]:
        """Search news by stock ticker"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM news_items WHERE tickers LIKE ? ORDER BY date DESC
        ''', (f'%"{ticker}"%',))

        rows = cursor.fetchall()
        conn.close()

        news_items = []
        for row in rows:
            news_items.append(NewsItem(
                id=row[0],
                title=row[1],
                category=NewsCategory(row[2]),
                tickers=json.loads(row[3]) if row[3] else [],
                date=datetime.fromisoformat(row[4]),
                source=row[5],
                url=row[6],
                summary=row[7],
                importance=row[8]
            ))

        return news_items
