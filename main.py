#!/usr/bin/env python3
"""
Vietnam Stock Market News Collector
Main application for collecting and managing stock market news
"""
import argparse
import sys
from datetime import datetime
from models import NewsCategory
from database import NewsDatabase
from news_collector import NewsCollector
from news_formatter import NewsFormatter
from sample_data import SampleNewsGenerator
from real_news_scraper import collect_real_news


class NewsApp:
    """Main application class"""

    def __init__(self, db_path: str = "vietnam_news.db"):
        self.db = NewsDatabase(db_path)
        self.collector = NewsCollector()
        print(f"Initialized news app with database: {db_path}")

    def collect_from_text(self, text_file: str):
        """Collect news from a text file"""
        try:
            with open(text_file, 'r', encoding='utf-8') as f:
                content = f.read()

            news_items = self.collector.parse_news_from_text(content)
            print(f"Parsed {len(news_items)} news items from {text_file}")

            for news in news_items:
                self.db.add_news(news)

            print(f"Added {len(news_items)} news items to database")
            return news_items

        except FileNotFoundError:
            print(f"Error: File {text_file} not found")
            return []
        except Exception as e:
            print(f"Error parsing file: {e}")
            return []

    def generate_sample_news(self, count: int = 100):
        """Generate sample news for demonstration"""
        print(f"Generating {count} sample news items...")
        news_items = SampleNewsGenerator.generate_sample_news(count)

        print(f"Saving to database...")
        for news in news_items:
            self.db.add_news(news)

        print(f"Successfully generated and saved {count} news items")
        return news_items

    def scrape_real_news(self, count: int = 50):
        """Scrape real news from Vietnamese financial websites"""
        print(f"\n{'='*60}")
        print(f"📰 SCRAPING REAL NEWS (NOT FAKE/GENERATED)")
        print(f"{'='*60}\n")
        print(f"Target: {count} unique, real news items")
        print(f"Sources: CafeF, VietStock, VnEconomy, CafeBiz\n")

        news_items = collect_real_news(count)

        if news_items:
            print(f"\n💾 Saving {len(news_items)} real news to database...")
            for news in news_items:
                self.db.add_news(news)

            print(f"✅ Successfully scraped and saved {len(news_items)} REAL news items")
            print(f"   All news are unique (duplicates removed)\n")
        else:
            print(f"⚠️ No news items were collected. Check internet connection.")

        return news_items

    def add_manual_news(self, title: str, tickers: list, category: str):
        """Add a single news item manually"""
        try:
            cat = NewsCategory(category)
        except ValueError:
            print(f"Invalid category. Available: {[c.value for c in NewsCategory]}")
            return None

        news = self.collector.add_news_manual(title, tickers, cat)
        news_id = self.db.add_news(news)
        print(f"Added news item with ID: {news_id}")
        return news

    def show_all_news(self, limit: int = None):
        """Display all news items"""
        news_items = self.db.get_all_news(limit)

        if not news_items:
            print("No news items found in database")
            return

        formatted = NewsFormatter.format_news_list(news_items)
        print(formatted)
        print(f"\n{NewsFormatter.format_summary(news_items)}")

    def show_by_category(self, category: str):
        """Show news by category"""
        try:
            cat = NewsCategory(category)
            news_items = self.db.get_news_by_category(cat)

            if not news_items:
                print(f"No news items found in category: {category}")
                return

            print(f"\n=== {category} ===\n")
            for news in news_items:
                print(NewsFormatter.format_single_news(news))

        except ValueError:
            print(f"Invalid category: {category}")

    def search_by_ticker(self, ticker: str):
        """Search news by stock ticker"""
        news_items = self.db.search_by_ticker(ticker.upper())

        if not news_items:
            print(f"No news found for ticker: {ticker}")
            return

        print(f"\n=== News for {ticker.upper()} ===\n")
        for news in news_items:
            print(f"{NewsFormatter.format_single_news(news)} [{news.category.value}]")

    def export_to_file(self, filename: str, limit: int = None):
        """Export news to a text file"""
        news_items = self.db.get_all_news(limit)

        if not news_items:
            print("No news items to export")
            return

        NewsFormatter.export_to_text_file(news_items, filename)
        print(f"Exported {len(news_items)} news items to {filename}")

    def show_stats(self):
        """Show database statistics"""
        total = self.db.get_news_count()
        print(f"\n=== Database Statistics ===")
        print(f"Total news items: {total}")

        print(f"\nNews by category:")
        for category in NewsCategory:
            count = len(self.db.get_news_by_category(category))
            if count > 0:
                print(f"  {category.value}: {count}")

    def clear_database(self):
        """Clear all news from database"""
        confirm = input("Are you sure you want to clear all news? (yes/no): ")
        if confirm.lower() == 'yes':
            self.db.clear_all_news()
            print("Database cleared")
        else:
            print("Cancelled")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Vietnam Stock Market News Collector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scrape 50 REAL news from Vietnamese websites (RECOMMENDED)
  python main.py --scrape 50

  # Generate 50 sample/demo news items (for testing only)
  python main.py --generate 50

  # Show all news
  python main.py --show

  # Show only 30 most recent news
  python main.py --show --limit 30

  # Search for news about a specific ticker
  python main.py --ticker VNM

  # Show news by category
  python main.py --category "DOANH NGHIỆP"

  # Export to file
  python main.py --export news_output.txt --limit 50

  # Import from text file
  python main.py --import news_input.txt

  # Show database statistics
  python main.py --stats

  # Clear database
  python main.py --clear

Note: --scrape gets REAL news (not fake), --generate creates sample data
        """
    )

    parser.add_argument('--db', default='vietnam_news.db', help='Database file path')
    parser.add_argument('--scrape', type=int, metavar='COUNT', help='Scrape N REAL news from Vietnamese websites')
    parser.add_argument('--generate', type=int, metavar='COUNT', help='Generate N sample/demo news items')
    parser.add_argument('--show', action='store_true', help='Show all news')
    parser.add_argument('--limit', type=int, help='Limit number of news items shown')
    parser.add_argument('--ticker', help='Search news by stock ticker')
    parser.add_argument('--category', help='Show news by category')
    parser.add_argument('--export', metavar='FILE', help='Export news to file')
    parser.add_argument('--import', dest='import_file', metavar='FILE', help='Import news from text file')
    parser.add_argument('--stats', action='store_true', help='Show database statistics')
    parser.add_argument('--clear', action='store_true', help='Clear all news from database')

    args = parser.parse_args()

    # Create app instance
    app = NewsApp(args.db)

    # Handle commands
    if args.scrape:
        app.scrape_real_news(args.scrape)
        if not args.export and not args.show:
            print("\nUse --show to display the news or --export to save to file")

    elif args.generate:
        app.generate_sample_news(args.generate)
        if not args.export and not args.show:
            print("\nUse --show to display the news or --export to save to file")

    elif args.import_file:
        app.collect_from_text(args.import_file)

    elif args.ticker:
        app.search_by_ticker(args.ticker)

    elif args.category:
        app.show_by_category(args.category)

    elif args.stats:
        app.show_stats()

    elif args.clear:
        app.clear_database()

    elif args.show:
        app.show_all_news(args.limit)

    elif args.export:
        app.export_to_file(args.export, args.limit)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
