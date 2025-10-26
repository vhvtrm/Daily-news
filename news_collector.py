"""
News collector module for gathering Vietnam stock market news
"""
import re
from datetime import datetime
from typing import List, Optional
from models import NewsItem, NewsCategory


class NewsCollector:
    """Base class for collecting news from various sources"""

    def __init__(self):
        self.news_items: List[NewsItem] = []

    def extract_tickers(self, text: str) -> List[str]:
        """
        Extract stock ticker symbols from text
        Tickers are typically 3-letter codes in uppercase
        """
        # Look for patterns like "POW:", "MWG/TCB:", etc.
        ticker_pattern = r'\b([A-Z]{3})\b'
        tickers = re.findall(ticker_pattern, text)
        return list(set(tickers))  # Remove duplicates

    def categorize_news(self, title: str, keywords: Optional[List[str]] = None) -> NewsCategory:
        """
        Automatically categorize news based on title and keywords
        """
        title_lower = title.lower()

        # Dividend related keywords
        if any(word in title_lower for word in ['cổ tức', 'trả cổ tức', 'chia cổ tức', 'dividend']):
            return NewsCategory.DIVIDEND

        # Trading/Issuance keywords
        if any(word in title_lower for word in ['chào bán', 'phát hành', 'mua bán', 'tăng vốn', 'bán cổ phiếu']):
            return NewsCategory.TRADING

        # Market movement keywords
        if any(word in title_lower for word in ['vn-index', 'thị trường', 'khối ngoại', 'tự doanh', 'thanh khoản']):
            return NewsCategory.MARKET_MOVEMENT

        # Securities/Finance keywords
        if any(word in title_lower for word in ['ngân hàng', 'chứng khoán', 'tài chính', 'ctck', 'room tín dụng']):
            return NewsCategory.SECURITIES_FINANCE

        # Vietnam economy keywords
        if any(word in title_lower for word in ['việt nam', 'chính phủ', 'thủ tướng', 'kinh tế vĩ mô', 'xuất khẩu', 'cao tốc']):
            return NewsCategory.VIETNAM_ECONOMY

        # Default to Enterprise
        return NewsCategory.ENTERPRISE

    def parse_news_from_text(self, text: str, base_date: Optional[datetime] = None) -> List[NewsItem]:
        """
        Parse news items from formatted text (like the example provided)
        """
        if base_date is None:
            base_date = datetime.now()

        news_items = []
        current_category = NewsCategory.ENTERPRISE

        lines = text.split('\n')
        news_id = 1

        for line in lines:
            line = line.strip()

            # Check if line is a category header
            if line.startswith('=>'):
                category_text = line.replace('=>', '').strip()
                for cat in NewsCategory:
                    if cat.value in category_text:
                        current_category = cat
                        break
                continue

            # Parse numbered news items
            match = re.match(r'^(\d+)\)\s+(.+)$', line)
            if match:
                news_id_num = int(match.group(1))
                content = match.group(2)

                # Extract tickers and title
                tickers = []
                title = content

                # Check if content starts with ticker symbols
                ticker_match = re.match(r'^([A-Z/]+):\s+(.+)$', content)
                if ticker_match:
                    ticker_str = ticker_match.group(1)
                    title = ticker_match.group(2)
                    tickers = ticker_str.split('/')
                else:
                    # Try to extract tickers from title
                    tickers = self.extract_tickers(content)

                news_item = NewsItem(
                    id=news_id_num,
                    title=title.strip(),
                    category=current_category,
                    tickers=tickers,
                    date=base_date
                )

                news_items.append(news_item)

        return news_items

    def add_news_manual(self, title: str, tickers: List[str], category: Optional[NewsCategory] = None,
                       source: Optional[str] = None, url: Optional[str] = None) -> NewsItem:
        """
        Manually add a news item
        """
        if category is None:
            category = self.categorize_news(title)

        news_item = NewsItem(
            id=len(self.news_items) + 1,
            title=title,
            category=category,
            tickers=tickers,
            date=datetime.now(),
            source=source,
            url=url
        )

        self.news_items.append(news_item)
        return news_item

    def import_from_json(self, json_data: dict) -> NewsItem:
        """Import news from JSON data"""
        news_item = NewsItem.from_dict(json_data)
        self.news_items.append(news_item)
        return news_item

    def get_collected_news(self) -> List[NewsItem]:
        """Get all collected news items"""
        return self.news_items

    def clear_collected_news(self):
        """Clear all collected news"""
        self.news_items = []
