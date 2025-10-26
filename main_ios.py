#!/usr/bin/env python3
"""
Vietnam Stock Market News Collector - iOS Version
Optimized for Pythonista on iPhone/iPad
"""
import os
import sys
from datetime import datetime
from models import NewsCategory
from database import NewsDatabase
from news_collector import NewsCollector
from news_formatter import NewsFormatter
from sample_data import SampleNewsGenerator


class NewsAppIOS:
    """iOS-optimized version of the news app"""

    def __init__(self):
        # Use Pythonista's Documents directory if available
        if 'Pythonista' in sys.executable:
            self.db_path = os.path.expanduser('~/Documents/vietnam_news.db')
        else:
            self.db_path = "vietnam_news.db"

        self.db = NewsDatabase(self.db_path)
        self.collector = NewsCollector()
        print(f"📱 Initialized news app")
        print(f"💾 Database: {self.db_path}\n")

    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("🇻🇳 VIETNAM STOCK MARKET NEWS")
        print("="*40)
        print("1. Generate 100 news items")
        print("2. Show all news")
        print("3. Show 20 most recent news")
        print("4. Search by ticker symbol")
        print("5. Show by category")
        print("6. Export to file")
        print("7. Show statistics")
        print("8. Clear database")
        print("0. Exit")
        print("="*40)

    def generate_news(self, count=100):
        """Generate sample news"""
        print(f"\n📰 Generating {count} news items...")
        news_items = SampleNewsGenerator.generate_sample_news(count)

        print(f"💾 Saving to database...")
        for news in news_items:
            self.db.add_news(news)

        print(f"✅ Successfully generated {count} news items!\n")

    def show_all_news(self, limit=None):
        """Display news items"""
        news_items = self.db.get_all_news(limit)

        if not news_items:
            print("❌ No news items found in database")
            return

        formatted = NewsFormatter.format_news_list(news_items)
        print("\n" + formatted)
        print("\n" + NewsFormatter.format_summary(news_items))

    def search_by_ticker(self):
        """Search news by ticker symbol"""
        ticker = input("\n🔍 Enter ticker symbol (e.g., VNM, HPG, TCB): ").strip().upper()

        if not ticker:
            print("❌ Please enter a ticker symbol")
            return

        news_items = self.db.search_by_ticker(ticker)

        if not news_items:
            print(f"❌ No news found for ticker: {ticker}")
            return

        print(f"\n📊 News for {ticker}:")
        print("="*40)
        for news in news_items:
            print(f"\n{NewsFormatter.format_single_news(news)}")
            print(f"   📁 Category: {news.category.value}")

    def show_by_category(self):
        """Show news by category"""
        print("\n📂 Categories:")
        print("="*40)
        categories = [c for c in NewsCategory if c != NewsCategory.OTHER]

        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat.value}")

        try:
            choice = int(input("\nChoose category (1-6): "))
            if 1 <= choice <= len(categories):
                selected_cat = categories[choice - 1]
                news_items = self.db.get_news_by_category(selected_cat)

                if not news_items:
                    print(f"❌ No news in category: {selected_cat.value}")
                    return

                print(f"\n📂 {selected_cat.value}")
                print("="*40)
                for news in news_items:
                    print(f"\n{NewsFormatter.format_single_news(news)}")
            else:
                print("❌ Invalid choice")
        except ValueError:
            print("❌ Please enter a number")

    def export_to_file(self):
        """Export news to a file"""
        filename = input("\n💾 Enter filename (e.g., news.txt): ").strip()

        if not filename:
            filename = f"news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        if not filename.endswith('.txt'):
            filename += '.txt'

        # Use Pythonista's Documents directory if available
        if 'Pythonista' in sys.executable:
            filepath = os.path.expanduser(f'~/Documents/{filename}')
        else:
            filepath = filename

        limit_input = input("📊 How many items to export? (press Enter for all): ").strip()
        limit = int(limit_input) if limit_input else None

        news_items = self.db.get_all_news(limit)

        if not news_items:
            print("❌ No news to export")
            return

        NewsFormatter.export_to_text_file(news_items, filepath)
        print(f"✅ Exported {len(news_items)} items to: {filepath}")
        print(f"📁 You can find it in Files app or share it from Pythonista")

    def show_stats(self):
        """Show database statistics"""
        total = self.db.get_news_count()

        print("\n📊 DATABASE STATISTICS")
        print("="*40)
        print(f"📰 Total news items: {total}")

        if total > 0:
            print(f"\n📂 News by category:")
            for category in NewsCategory:
                if category == NewsCategory.OTHER:
                    continue
                count = len(self.db.get_news_by_category(category))
                if count > 0:
                    print(f"   {category.value}: {count}")

    def clear_database(self):
        """Clear all news from database"""
        confirm = input("\n⚠️  Clear ALL news? Type 'yes' to confirm: ").strip().lower()

        if confirm == 'yes':
            self.db.clear_all_news()
            print("✅ Database cleared")
        else:
            print("❌ Cancelled")

    def run(self):
        """Main application loop"""
        print("\n🎉 Welcome to Vietnam Stock Market News!")
        print("📱 iOS Version for Pythonista\n")

        while True:
            self.show_menu()

            try:
                choice = input("\n👉 Choose option: ").strip()

                if choice == '1':
                    self.generate_news(100)

                elif choice == '2':
                    self.show_all_news()

                elif choice == '3':
                    self.show_all_news(limit=20)

                elif choice == '4':
                    self.search_by_ticker()

                elif choice == '5':
                    self.show_by_category()

                elif choice == '6':
                    self.export_to_file()

                elif choice == '7':
                    self.show_stats()

                elif choice == '8':
                    self.clear_database()

                elif choice == '0':
                    print("\n👋 Goodbye! See you next time!")
                    break

                else:
                    print("❌ Invalid option. Please choose 0-8")

                # Wait for user to press Enter before showing menu again
                input("\n⏎ Press Enter to continue...")

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\n⏎ Press Enter to continue...")


def main():
    """Main entry point for iOS version"""
    app = NewsAppIOS()
    app.run()


if __name__ == "__main__":
    main()
