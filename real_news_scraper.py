"""
Real news scraper for Vietnamese financial news websites
Scrapes actual news from CafeF, VietStock, VnEconomy, CafeBiz, and more
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import time
from typing import List, Optional
from models import NewsItem, NewsCategory


class RealNewsScraper:
    """Scrapes real news from Vietnamese financial news websites"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def extract_tickers(self, text: str) -> List[str]:
        """Extract stock ticker symbols from text"""
        # Vietnamese stock tickers are typically 3-letter uppercase codes
        ticker_pattern = r'\b([A-Z]{3})\b'
        tickers = re.findall(ticker_pattern, text)
        # Filter to keep only valid Vietnamese stock tickers
        valid_tickers = [t for t in tickers if len(t) == 3 and t.isalpha()]
        return list(set(valid_tickers))[:3]  # Return max 3 tickers

    def categorize_news(self, title: str, url: str = "") -> NewsCategory:
        """Categorize news based on title and URL keywords"""
        title_lower = title.lower()
        url_lower = url.lower()

        # Dividend keywords
        if any(word in title_lower for word in ['cổ tức', 'trả cổ tức', 'chia cổ tức', 'chốt quyền']):
            return NewsCategory.DIVIDEND

        # Trading/Issuance keywords
        if any(word in title_lower for word in ['chào bán', 'phát hành', 'tăng vốn', 'mua bán', 'trái phiếu', 'cổ phiếu']):
            return NewsCategory.TRADING

        # Market movement keywords
        if any(word in title_lower for word in ['vn-index', 'vnindex', 'thị trường', 'khối ngoại', 'tự doanh', 'thanh khoản', 'tăng điểm', 'giảm điểm']):
            return NewsCategory.MARKET_MOVEMENT

        # Securities/Finance keywords
        if any(word in title_lower for word in ['ngân hàng', 'bank', 'tín dụng', 'lãi suất', 'room']):
            return NewsCategory.SECURITIES_FINANCE

        # Vietnam economy keywords
        if any(word in title_lower for word in ['gdp', 'kinh tế', 'xuất khẩu', 'nhập khẩu', 'chính phủ', 'thủ tướng', 'fdi', 'cao tốc']):
            return NewsCategory.VIETNAM_ECONOMY

        # Default to Enterprise
        return NewsCategory.ENTERPRISE

    def scrape_cafef(self, limit: int = 30) -> List[NewsItem]:
        """Scrape news from CafeF - Vietnam's leading financial news site"""
        news_items = []

        # Try RSS feeds first (more reliable)
        rss_urls = [
            'https://cafef.vn/rss/thi-truong-chung-khoan.rss',
            'https://cafef.vn/rss/doanh-nghiep.rss',
            'https://cafef.vn/rss/tai-chinh-ngan-hang.rss',
        ]

        # Fallback to regular URLs
        urls_to_scrape = [
            'https://cafef.vn/thi-truong-chung-khoan.chn',
            'https://cafef.vn/doanh-nghiep.chn',
            'https://cafef.vn/tai-chinh-ngan-hang.chn',
        ]

        print("📰 Scraping CafeF...")

        # Try RSS feeds first
        for rss_url in rss_urls:
            try:
                response = self.session.get(rss_url, timeout=15)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'lxml-xml')
                    items = soup.find_all('item')

                    for item in items[:10]:
                        try:
                            title_elem = item.find('title')
                            link_elem = item.find('link')

                            if not title_elem or not link_elem:
                                continue

                            title = title_elem.get_text(strip=True)
                            full_url = link_elem.get_text(strip=True)

                            if not title or len(title) < 20:
                                continue

                            tickers = self.extract_tickers(title)
                            category = self.categorize_news(title, full_url)

                            news_item = NewsItem(
                                id=len(news_items) + 1,
                                title=title,
                                category=category,
                                tickers=tickers,
                                date=datetime.now(),
                                source="CafeF",
                                url=full_url
                            )
                            news_items.append(news_item)

                            if len(news_items) >= limit:
                                break
                        except:
                            continue

                    if len(news_items) >= limit:
                        break

                time.sleep(0.3)
            except Exception as e:
                continue

        # If RSS failed or didn't get enough, try regular scraping
        if len(news_items) < limit:
            for url in urls_to_scrape:
                try:
                    response = self.session.get(url, timeout=15)
                    response.encoding = 'utf-8'

                    if response.status_code != 200:
                        print(f"   ⚠️ Failed to fetch {url}: {response.status_code}")
                        continue

                    soup = BeautifulSoup(response.text, 'lxml')

                    # Find news articles
                    articles = soup.find_all('h3', class_='titlehidden') or soup.find_all('h3')

                    for article in articles[:15]:
                        try:
                            link = article.find('a')
                            if not link:
                                continue

                            title = link.get_text(strip=True)
                            href = link.get('href', '')

                            if not title or len(title) < 20:
                                continue

                            # Build full URL
                            if href.startswith('/'):
                                full_url = f"https://cafef.vn{href}"
                            elif href.startswith('http'):
                                full_url = href
                            else:
                                continue

                            tickers = self.extract_tickers(title)
                            category = self.categorize_news(title, full_url)

                            news_item = NewsItem(
                                id=len(news_items) + 1,
                                title=title,
                                category=category,
                                tickers=tickers,
                                date=datetime.now(),
                                source="CafeF",
                                url=full_url
                            )
                            news_items.append(news_item)

                            if len(news_items) >= limit:
                                break

                        except Exception as e:
                            continue

                    time.sleep(0.5)  # Be respectful to the server

                except Exception as e:
                    print(f"   ❌ Error scraping CafeF: {e}")

        print(f"   ✅ Got {len(news_items)} news from CafeF")
        return news_items[:limit]

    def scrape_vietstock(self, limit: int = 30) -> List[NewsItem]:
        """Scrape news from VietStock"""
        news_items = []
        urls_to_scrape = [
            'https://vietstock.vn/chung-khoan.htm',
            'https://vietstock.vn/doanh-nghiep.htm',
        ]

        print("📰 Scraping VietStock...")

        for url in urls_to_scrape:
            try:
                response = self.session.get(url, timeout=15)
                response.encoding = 'utf-8'

                if response.status_code != 200:
                    print(f"   ⚠️ Failed to fetch {url}: {response.status_code}")
                    continue

                soup = BeautifulSoup(response.text, 'lxml')

                # Find news articles
                articles = soup.find_all(['h2', 'h3', 'h4'], class_=lambda x: x and 'title' in x.lower() if x else False)
                if not articles:
                    articles = soup.find_all('a', class_=lambda x: x and 'title' in x.lower() if x else False)

                for article in articles[:15]:
                    try:
                        if article.name == 'a':
                            link = article
                        else:
                            link = article.find('a')

                        if not link:
                            continue

                        title = link.get_text(strip=True)
                        href = link.get('href', '')

                        if not title or len(title) < 20:
                            continue

                        # Build full URL
                        if href.startswith('/'):
                            full_url = f"https://vietstock.vn{href}"
                        elif href.startswith('http'):
                            full_url = href
                        else:
                            continue

                        tickers = self.extract_tickers(title)
                        category = self.categorize_news(title, full_url)

                        news_item = NewsItem(
                            id=len(news_items) + 1,
                            title=title,
                            category=category,
                            tickers=tickers,
                            date=datetime.now(),
                            source="VietStock",
                            url=full_url
                        )
                        news_items.append(news_item)

                        if len(news_items) >= limit:
                            break

                    except Exception as e:
                        continue

                time.sleep(0.5)

            except Exception as e:
                print(f"   ❌ Error scraping VietStock: {e}")

        print(f"   ✅ Got {len(news_items)} news from VietStock")
        return news_items[:limit]

    def scrape_vneconomy(self, limit: int = 25) -> List[NewsItem]:
        """Scrape news from VnEconomy"""
        news_items = []
        urls_to_scrape = [
            'https://vneconomy.vn/chung-khoan.htm',
            'https://vneconomy.vn/doanh-nghiep.htm',
        ]

        print("📰 Scraping VnEconomy...")

        for url in urls_to_scrape:
            try:
                response = self.session.get(url, timeout=15)
                response.encoding = 'utf-8'

                if response.status_code != 200:
                    print(f"   ⚠️ Failed to fetch {url}: {response.status_code}")
                    continue

                soup = BeautifulSoup(response.text, 'lxml')

                # Find news articles
                articles = soup.find_all('h3') or soup.find_all('h2')

                for article in articles[:12]:
                    try:
                        link = article.find('a')
                        if not link:
                            continue

                        title = link.get_text(strip=True)
                        href = link.get('href', '')

                        if not title or len(title) < 20:
                            continue

                        # Build full URL
                        if href.startswith('/'):
                            full_url = f"https://vneconomy.vn{href}"
                        elif href.startswith('http'):
                            full_url = href
                        else:
                            continue

                        tickers = self.extract_tickers(title)
                        category = self.categorize_news(title, full_url)

                        news_item = NewsItem(
                            id=len(news_items) + 1,
                            title=title,
                            category=category,
                            tickers=tickers,
                            date=datetime.now(),
                            source="VnEconomy",
                            url=full_url
                        )
                        news_items.append(news_item)

                        if len(news_items) >= limit:
                            break

                    except Exception as e:
                        continue

                time.sleep(0.5)

            except Exception as e:
                print(f"   ❌ Error scraping VnEconomy: {e}")

        print(f"   ✅ Got {len(news_items)} news from VnEconomy")
        return news_items[:limit]

    def scrape_cafebiz(self, limit: int = 20) -> List[NewsItem]:
        """Scrape news from CafeBiz"""
        news_items = []
        urls_to_scrape = [
            'https://cafebiz.vn/tai-chinh.chn',
            'https://cafebiz.vn/doanh-nghiep.chn',
        ]

        print("📰 Scraping CafeBiz...")

        for url in urls_to_scrape:
            try:
                response = self.session.get(url, timeout=15)
                response.encoding = 'utf-8'

                if response.status_code != 200:
                    print(f"   ⚠️ Failed to fetch {url}: {response.status_code}")
                    continue

                soup = BeautifulSoup(response.text, 'lxml')

                # Find news articles
                articles = soup.find_all('h3')

                for article in articles[:10]:
                    try:
                        link = article.find('a')
                        if not link:
                            continue

                        title = link.get_text(strip=True)
                        href = link.get('href', '')

                        if not title or len(title) < 20:
                            continue

                        # Build full URL
                        if href.startswith('/'):
                            full_url = f"https://cafebiz.vn{href}"
                        elif href.startswith('http'):
                            full_url = href
                        else:
                            continue

                        tickers = self.extract_tickers(title)
                        category = self.categorize_news(title, full_url)

                        news_item = NewsItem(
                            id=len(news_items) + 1,
                            title=title,
                            category=category,
                            tickers=tickers,
                            date=datetime.now(),
                            source="CafeBiz",
                            url=full_url
                        )
                        news_items.append(news_item)

                        if len(news_items) >= limit:
                            break

                    except Exception as e:
                        continue

                time.sleep(0.5)

            except Exception as e:
                print(f"   ❌ Error scraping CafeBiz: {e}")

        print(f"   ✅ Got {len(news_items)} news from CafeBiz")
        return news_items[:limit]

    def scrape_all_sources(self, total_limit: int = 100) -> List[NewsItem]:
        """
        Scrape news from all available sources
        Returns combined list of real news items
        """
        all_news = []

        print("\n🌐 Starting to scrape REAL news from Vietnamese financial websites...\n")

        # Calculate how many to get from each source
        per_source = total_limit // 4 + 5  # Get a bit more, then trim

        # Scrape from each source
        try:
            cafef_news = self.scrape_cafef(per_source)
            all_news.extend(cafef_news)
        except Exception as e:
            print(f"❌ CafeF scraping failed: {e}")

        try:
            vietstock_news = self.scrape_vietstock(per_source)
            all_news.extend(vietstock_news)
        except Exception as e:
            print(f"❌ VietStock scraping failed: {e}")

        try:
            vneconomy_news = self.scrape_vneconomy(per_source)
            all_news.extend(vneconomy_news)
        except Exception as e:
            print(f"❌ VnEconomy scraping failed: {e}")

        try:
            cafebiz_news = self.scrape_cafebiz(per_source)
            all_news.extend(cafebiz_news)
        except Exception as e:
            print(f"❌ CafeBiz scraping failed: {e}")

        # Remove duplicates based on title similarity
        unique_news = []
        seen_titles = set()

        for news in all_news:
            # Create a simplified version of title for comparison
            simple_title = news.title.lower()[:50]
            if simple_title not in seen_titles:
                seen_titles.add(simple_title)
                unique_news.append(news)

        # Re-number the news items
        for i, news in enumerate(unique_news, 1):
            news.id = i

        # Trim to requested limit
        final_news = unique_news[:total_limit]

        print(f"\n✅ Total: {len(final_news)} REAL news items collected from multiple sources!")
        print(f"   Sources: CafeF, VietStock, VnEconomy, CafeBiz\n")

        return final_news


def collect_real_news(count: int = 100) -> List[NewsItem]:
    """
    Main function to collect real news from Vietnamese financial websites

    Args:
        count: Number of news items to collect (default 100)

    Returns:
        List of real NewsItem objects with actual headlines and URLs
    """
    scraper = RealNewsScraper()
    return scraper.scrape_all_sources(count)


if __name__ == "__main__":
    # Test the scraper
    news = collect_real_news(100)
    print(f"\nCollected {len(news)} real news items:")
    for item in news[:10]:
        print(f"\n{item.id}) {item.title}")
        print(f"   Source: {item.source} | URL: {item.url}")
