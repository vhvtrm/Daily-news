"""
News formatter module for generating formatted output
"""
from datetime import datetime
from typing import List, Dict
from models import NewsItem, NewsCategory, DailyNewsDigest


class NewsFormatter:
    """Formats news items into readable output"""

    @staticmethod
    def format_single_news(news: NewsItem, show_id: bool = True) -> str:
        """Format a single news item"""
        tickers_str = "/".join(news.tickers) if news.tickers else ""
        ticker_prefix = f"{tickers_str}: " if tickers_str else ""

        if show_id:
            return f"{news.id}) {ticker_prefix}{news.title}"
        else:
            return f"{ticker_prefix}{news.title}"

    @staticmethod
    def format_news_list(news_items: List[NewsItem], title: str = "TIN NHANH CHỨNG KHOÁN") -> str:
        """
        Format a list of news items grouped by category
        Similar to the example format provided
        """
        output = []

        # Add title with date
        date_str = datetime.now().strftime("%d/%m")
        output.append(f"{title} {date_str}\n")

        # Group news by category
        news_by_category: Dict[NewsCategory, List[NewsItem]] = {}
        for news in news_items:
            if news.category not in news_by_category:
                news_by_category[news.category] = []
            news_by_category[news.category].append(news)

        # Format each category
        for category in NewsCategory:
            if category not in news_by_category or category == NewsCategory.OTHER:
                continue

            category_news = news_by_category[category]
            if not category_news:
                continue

            output.append(f"=> {category.value}\n")

            for news in category_news:
                output.append(NewsFormatter.format_single_news(news))

            output.append("\n_\n")

        return "\n".join(output)

    @staticmethod
    def format_digest(digest: DailyNewsDigest) -> str:
        """Format a daily news digest"""
        return digest.format_digest()

    @staticmethod
    def format_summary(news_items: List[NewsItem]) -> str:
        """Generate a summary of news items"""
        total = len(news_items)

        # Count by category
        category_counts = {}
        for news in news_items:
            cat = news.category.value
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # Count unique tickers
        all_tickers = set()
        for news in news_items:
            all_tickers.update(news.tickers)

        output = []
        output.append(f"=== TỔNG KẾT TIN TỨC ===")
        output.append(f"Tổng số tin: {total}")
        output.append(f"Số mã chứng khoán: {len(all_tickers)}")
        output.append(f"\nPhân loại theo danh mục:")

        for category, count in category_counts.items():
            output.append(f"  - {category}: {count} tin")

        return "\n".join(output)

    @staticmethod
    def export_to_text_file(news_items: List[NewsItem], filename: str):
        """Export formatted news to a text file"""
        content = NewsFormatter.format_news_list(news_items)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            f.write("\n\n")
            f.write(NewsFormatter.format_summary(news_items))

        return filename
