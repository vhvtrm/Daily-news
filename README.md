# Vietnam Stock Market News Collector

A Python application for collecting, organizing, and managing news about the Vietnam stock market, including company news, market movements, and macroeconomic updates.

## Features

- Collect and store up to 100+ news items about Vietnam stock market
- Automatic categorization into 6 main categories:
  - **DOANH NGHIỆP** (Enterprises/Companies)
  - **MUA BÁN/PHÁT HÀNH** (Trading/Issuance)
  - **CỔ TỨC** (Dividends)
  - **CHUYỂN ĐỘNG THỊ TRƯỜNG** (Market Movements)
  - **CHỨNG KHOÁN/TÀI CHÍNH** (Securities/Finance)
  - **VIỆT NAM** (Vietnam Economy)
- Extract and track stock ticker symbols (POW, MWG, TCB, etc.)
- SQLite database for persistent storage
- Beautiful formatted output similar to Vietnamese financial news digests
- Search functionality by ticker or category
- Export to text files

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Daily-news
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Generate 100 Sample News Items

```bash
python main.py --generate 100
```

### Display All News

```bash
python main.py --show
```

### Display Limited Number of News

```bash
python main.py --show --limit 50
```

### Export to File

```bash
python main.py --export daily_news.txt
```

## Usage Examples

### Generate Sample Data
Generate 100 sample Vietnam stock market news items:
```bash
python main.py --generate 100
```

### View News
Show all news in formatted output:
```bash
python main.py --show
```

Show only 30 most recent news:
```bash
python main.py --show --limit 30
```

### Search by Stock Ticker
Find all news related to a specific stock:
```bash
python main.py --ticker VNM
python main.py --ticker HPG
```

### Filter by Category
Show news from a specific category:
```bash
python main.py --category "DOANH NGHIỆP"
python main.py --category "CỔ TỨC"
```

### Database Statistics
View statistics about collected news:
```bash
python main.py --stats
```

### Export News
Export news to a text file:
```bash
python main.py --export news_report.txt
```

Export only 100 most recent items:
```bash
python main.py --export news_report.txt --limit 100
```

### Import from Text File
Parse and import news from a formatted text file:
```bash
python main.py --import news_input.txt
```

The text file should follow this format:
```
=> DOANH NGHIỆP

1) POW: Gã khổng lồ 35.000 tỷ của ngành điện lần đầu muốn tăng vốn thêm 7.000 tỷ

2) MWG: Bách Hóa Xanh tăng tốc tìm mặt bằng để Bắc tiến

=> CỔ TỨC

3) CTR: Lãi kỷ lục, chốt quyền trả cổ tức bằng tiền tỷ lệ 21%
```

### Clear Database
Remove all news items:
```bash
python main.py --clear
```

## Project Structure

```
Daily-news/
├── main.py              # Main application entry point
├── models.py            # Data models (NewsItem, NewsCategory, DailyNewsDigest)
├── database.py          # SQLite database operations
├── news_collector.py    # News collection and parsing logic
├── news_formatter.py    # Output formatting
├── sample_data.py       # Sample data generator
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── vietnam_news.db     # SQLite database (created on first run)
```

## Data Model

### NewsItem
Each news item contains:
- **id**: Unique identifier
- **title**: News headline
- **category**: One of 6 predefined categories
- **tickers**: List of stock ticker symbols (e.g., ["VNM", "HPG"])
- **date**: Publication date
- **source**: News source (optional)
- **url**: Source URL (optional)
- **importance**: Importance rating (0-5)

### Categories
1. **DOANH NGHIỆP**: Company news (earnings, expansions, contracts)
2. **MUA BÁN/PHÁT HÀNH**: Stock offerings, issuances, insider trading
3. **CỔ TỨC**: Dividend announcements
4. **CHUYỂN ĐỘNG THỊ TRƯỜNG**: Market movements, index changes, trading activity
5. **CHỨNG KHOÁN/TÀI CHÍNH**: Banking and finance sector news
6. **VIỆT NAM**: Macroeconomic news, government policies

## Output Format

The app generates beautifully formatted news digests:

```
TIN NHANH CHỨNG KHOÁN 26/10

=> DOANH NGHIỆP

1) POW: Gã khổng lồ 35.000 tỷ của ngành điện lần đầu muốn tăng vốn thêm 7.000 tỷ
2) MWG: Bách Hóa Xanh tăng tốc tìm mặt bằng để Bắc tiến
3) TCB: Techcombank tính chuyện chế tác vàng miếng thương hiệu Techcombank

_

=> CỔ TỨC

21) CTR: Lãi kỷ lục, chốt quyền trả cổ tức bằng tiền tỷ lệ 21%
22) PVD: Lãi tăng mạnh, dành gần 280 tỷ đồng trả cổ tức

_
```

## Extending the Application

### Adding Real News Sources

To add real web scraping capabilities:

1. Edit `news_collector.py`
2. Add methods to scrape from your preferred news sources
3. Use BeautifulSoup for HTML parsing

Example:
```python
def scrape_vietstock(self, url):
    # Your scraping logic here
    pass
```

### Custom Categories

Edit `models.py` to add new categories to the `NewsCategory` enum.

### API Integration

The modular design makes it easy to add API integrations for automated news collection.

## Database

The app uses SQLite for storage. The database file (`vietnam_news.db`) is created automatically on first run.

To use a different database file:
```bash
python main.py --db my_custom_db.db --generate 100
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- python-dotenv
- lxml

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Future Enhancements

- [ ] Web scraping from popular Vietnamese financial news sites (CafeF, VietStock, etc.)
- [ ] Real-time news collection via RSS feeds
- [ ] Web interface using Flask/Django
- [ ] Sentiment analysis of news
- [ ] Email digest notifications
- [ ] Integration with trading APIs
- [ ] Machine learning for news importance scoring
- [ ] Multi-language support (Vietnamese/English)

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

Made with ❤️ for Vietnam Stock Market enthusiasts
