"""
Data models for Vietnam Stock Market News
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum


class NewsCategory(Enum):
    """News categories based on Vietnam stock market news structure"""
    ENTERPRISE = "DOANH NGHIỆP"  # Companies/Enterprises
    TRADING = "MUA BÁN/ PHÁT HÀNH"  # Trading/Issuance
    DIVIDEND = "CỔ TỨC"  # Dividends
    MARKET_MOVEMENT = "CHUYỂN ĐỘNG THỊ TRƯỜNG"  # Market Movements
    SECURITIES_FINANCE = "CHỨNG KHOÁN/ TÀI CHÍNH"  # Securities/Finance
    VIETNAM_ECONOMY = "VIỆT NAM"  # Vietnam Economy
    OTHER = "KHÁC"  # Other


@dataclass
class NewsItem:
    """Represents a single news item"""
    id: int
    title: str
    category: NewsCategory
    tickers: List[str]  # Stock ticker symbols like POW, MWG, TCB
    date: datetime
    source: Optional[str] = None
    url: Optional[str] = None
    summary: Optional[str] = None
    importance: int = 0  # 0-5, higher is more important

    def __str__(self):
        tickers_str = "/".join(self.tickers) if self.tickers else ""
        ticker_prefix = f"{tickers_str}: " if tickers_str else ""
        return f"{self.id}) {ticker_prefix}{self.title}"

    def to_dict(self):
        """Convert to dictionary for storage"""
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category.value,
            'tickers': self.tickers,
            'date': self.date.isoformat(),
            'source': self.source,
            'url': self.url,
            'summary': self.summary,
            'importance': self.importance
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create NewsItem from dictionary"""
        return cls(
            id=data['id'],
            title=data['title'],
            category=NewsCategory(data['category']),
            tickers=data['tickers'],
            date=datetime.fromisoformat(data['date']),
            source=data.get('source'),
            url=data.get('url'),
            summary=data.get('summary'),
            importance=data.get('importance', 0)
        )


@dataclass
class DailyNewsDigest:
    """Represents a daily news digest"""
    date: datetime
    title: str
    news_items: List[NewsItem]

    def get_news_by_category(self, category: NewsCategory) -> List[NewsItem]:
        """Get all news items for a specific category"""
        return [item for item in self.news_items if item.category == category]

    def format_digest(self) -> str:
        """Format the digest similar to the example provided"""
        output = []
        output.append(f"{self.title}\n")

        # Group news by category
        for category in NewsCategory:
            category_news = self.get_news_by_category(category)
            if not category_news:
                continue

            output.append(f"\n=> {category.value}\n")
            for news in category_news:
                output.append(str(news))
            output.append("_")

        return "\n".join(output)
