"""
Sample data generator for demonstration purposes
"""
from datetime import datetime, timedelta
import random
from models import NewsItem, NewsCategory


class SampleNewsGenerator:
    """Generates sample Vietnam stock market news for testing"""

    # Sample Vietnamese stock tickers
    TICKERS = [
        "VNM", "VIC", "VHM", "HPG", "TCB", "VCB", "BID", "CTG", "MWG", "FPT",
        "VPB", "GAS", "MSN", "SAB", "VRE", "POW", "PLX", "SSI", "NVL", "VNM",
        "HDB", "MBB", "ACB", "STB", "TPB", "DIG", "GVR", "VJC", "DXG", "NLG",
        "FLC", "HAG", "PVD", "BSR", "PVT", "AGG", "GIL", "DRH", "SCD", "PTL",
        "CCA", "FMC", "EVF", "BCM", "SNZ", "TAL", "CTR", "X20"
    ]

    # Sample news templates by category
    ENTERPRISE_TEMPLATES = [
        "{ticker}: Công ty công bố kế hoạch tăng vốn điều lệ lên {value} tỷ đồng",
        "{ticker}: Báo cáo lợi nhuận quý {quarter} tăng trưởng {percent}%",
        "{ticker}: Ký hợp đồng cung cấp sản phẩm trị giá {value} triệu USD",
        "{ticker}: Khai trương {number} chi nhánh mới tại khu vực miền {region}",
        "{ticker}: Hoàn thành dự án đầu tư nhà máy mới công suất {value} tấn/năm",
        "{ticker}: Doanh thu tháng {month} đạt {value} tỷ đồng, tăng {percent}%",
        "{ticker}: Công bố chiến lược mở rộng thị trường {market} trong năm 2025",
        "{ticker}: Đạt hợp đồng xuất khẩu {value} triệu USD sang thị trường {market}",
    ]

    TRADING_TEMPLATES = [
        "{ticker}: Chuẩn bị chào bán {value} triệu cổ phiếu giá {price} đồng",
        "{ticker}: Chủ tịch muốn bán {value} triệu cổ phiếu",
        "{ticker}: Huy động {value} tỷ đồng trái phiếu trong {days} ngày",
        "{ticker}: Thay đổi điều khoản lô trái phiếu ngàn tỷ",
        "{ticker}: Chào bán riêng lẻ {value} triệu cổ phiếu cho cổ đông",
    ]

    DIVIDEND_TEMPLATES = [
        "{ticker}: Chốt quyền trả cổ tức bằng tiền tỷ lệ {percent}%",
        "{ticker}: Dành gần {value} tỷ đồng trả cổ tức",
        "{ticker}: Chốt ngày chia cổ tức, tỷ lệ {percent}% tiền mặt",
        "{ticker}: Hoàn tất phát hành {value} triệu cổ phiếu thưởng cho cổ đông",
    ]

    MARKET_TEMPLATES = [
        "VN-Index tăng mạnh {percent} điểm, thanh khoản đạt {value} tỷ đồng",
        "Khối ngoại mua ròng {value} tỷ đồng, tập trung vào cổ phiếu {ticker}",
        "Cổ phiếu {ticker} tăng trần, khối ngoại gom hàng mạnh",
        "Tự doanh CTCK mua ròng {value} tỷ đồng trên HOSE",
    ]

    SECURITIES_TEMPLATES = [
        "Ngân hàng {ticker} báo lợi nhuận {period} tăng {percent}%",
        "Chính phủ yêu cầu đẩy nhanh tăng vốn điều lệ cho {ticker}",
        "Nhóm cổ phiếu ngân hàng hưởng lợi khi xóa room tín dụng",
    ]

    VIETNAM_TEMPLATES = [
        "Thủ tướng: Cả nước đã có gần {value}km đường cao tốc",
        "Vốn ngoại đổ vào khu công nghiệp, tăng {percent}%",
        "VASEP dự báo giá cá tra xuất khẩu tăng từ tháng {month}",
        "Siêu nút giao 3 tầng kết nối 2 tuyến cao tốc trị giá {value} tỷ sắp hoàn thành",
    ]

    # Popular Vietnamese financial news websites
    NEWS_SOURCES = [
        {"name": "CafeF", "domain": "cafef.vn"},
        {"name": "VietStock", "domain": "vietstock.vn"},
        {"name": "CafeBiz", "domain": "cafebiz.vn"},
        {"name": "Nhịp Đầu Tư", "domain": "ndh.vn"},
        {"name": "Báo Đầu Tư", "domain": "baodautu.vn"},
        {"name": "VnEconomy", "domain": "vneconomy.vn"},
        {"name": "Thời Báo Kinh Tế", "domain": "tbktvn.com"},
        {"name": "Đầu Tư Chứng Khoán", "domain": "stockbiz.vn"},
        {"name": "Doanh Nghiệp", "domain": "doanhnghiep.vn"},
        {"name": "Tài Chính Online", "domain": "taichinh.vn"},
    ]

    @staticmethod
    def generate_news_item(category: NewsCategory, news_id: int) -> NewsItem:
        """Generate a single random news item"""

        if category == NewsCategory.ENTERPRISE:
            templates = SampleNewsGenerator.ENTERPRISE_TEMPLATES
        elif category == NewsCategory.TRADING:
            templates = SampleNewsGenerator.TRADING_TEMPLATES
        elif category == NewsCategory.DIVIDEND:
            templates = SampleNewsGenerator.DIVIDEND_TEMPLATES
        elif category == NewsCategory.MARKET_MOVEMENT:
            templates = SampleNewsGenerator.MARKET_TEMPLATES
        elif category == NewsCategory.SECURITIES_FINANCE:
            templates = SampleNewsGenerator.SECURITIES_TEMPLATES
        elif category == NewsCategory.VIETNAM_ECONOMY:
            templates = SampleNewsGenerator.VIETNAM_TEMPLATES
        else:
            templates = SampleNewsGenerator.ENTERPRISE_TEMPLATES

        template = random.choice(templates)
        ticker = random.choice(SampleNewsGenerator.TICKERS)

        # Fill in template variables
        title = template.format(
            ticker=ticker,
            value=random.randint(100, 50000),
            percent=random.randint(5, 150),
            quarter=random.choice(["1", "2", "3", "4"]),
            number=random.randint(5, 50),
            region=random.choice(["Bắc", "Trung", "Nam"]),
            month=random.randint(1, 12),
            market=random.choice(["Mỹ", "EU", "Châu Á", "Trung Quốc"]),
            price=random.randint(10000, 50000),
            days=random.randint(3, 30),
            period=random.choice(["quý 1", "quý 2", "quý 3", "quý 4", "6 tháng đầu năm"])
        )

        # Determine tickers
        tickers = [ticker] if "{ticker}" in template else []

        # Generate realistic URL
        source = random.choice(SampleNewsGenerator.NEWS_SOURCES)
        article_id = random.randint(100000, 999999)
        year = datetime.now().year
        month = datetime.now().month

        # Generate URL based on common Vietnamese news site patterns
        url_patterns = [
            f"https://{source['domain']}/{ticker.lower()}-{article_id}.html",
            f"https://{source['domain']}/{year}/{month:02d}/{ticker.lower()}-{article_id}.chn",
            f"https://{source['domain']}/chung-khoan/{ticker.lower()}-{article_id}",
            f"https://{source['domain']}/doanh-nghiep/{ticker.lower()}-tin-{article_id}.html",
        ]

        url = random.choice(url_patterns)

        return NewsItem(
            id=news_id,
            title=title,
            category=category,
            tickers=tickers,
            date=datetime.now() - timedelta(days=random.randint(0, 7)),
            source=source['name'],
            url=url,
            importance=random.randint(1, 5)
        )

    @staticmethod
    def generate_sample_news(count: int = 100) -> list:
        """Generate multiple sample news items"""
        news_items = []

        # Distribution of news across categories
        distribution = {
            NewsCategory.ENTERPRISE: 0.40,  # 40% enterprise news
            NewsCategory.TRADING: 0.15,
            NewsCategory.DIVIDEND: 0.10,
            NewsCategory.MARKET_MOVEMENT: 0.15,
            NewsCategory.SECURITIES_FINANCE: 0.10,
            NewsCategory.VIETNAM_ECONOMY: 0.10,
        }

        for i in range(1, count + 1):
            # Select category based on distribution
            rand = random.random()
            cumulative = 0
            selected_category = NewsCategory.ENTERPRISE

            for category, prob in distribution.items():
                cumulative += prob
                if rand <= cumulative:
                    selected_category = category
                    break

            news_item = SampleNewsGenerator.generate_news_item(selected_category, i)
            news_items.append(news_item)

        return news_items
