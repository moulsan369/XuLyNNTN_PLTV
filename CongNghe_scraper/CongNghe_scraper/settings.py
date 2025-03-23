# Scrapy settings for CongNghe_scraper project

BOT_NAME = "CongNghe_scraper"

SPIDER_MODULES = ["CongNghe_scraper.spiders"]
NEWSPIDER_MODULE = "CongNghe_scraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # Tắt để crawl không bị chặn bởi robots.txt

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1  # Giảm từ 5 xuống 1 để crawl nhanh hơn, vẫn an toàn

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32  # Giữ nguyên, đủ để xử lý nhanh

# Giới hạn độ sâu phân trang
DEPTH_LIMIT = 50  # Giảm từ 100 xuống 50, đủ để lấy 1000 URL

# Cấu hình lưu file JSON
FEEDS = {
    'congnghe_urls.json': {  # Đổi tên file cho phù hợp với chủ đề "Công nghệ"
        'format': 'json',
        'overwrite': False,  # Không ghi đè, thêm dữ liệu vào file hiện có
        'fields': ['url'],   # Chỉ lưu trường 'url'
        'encoding': 'utf-8', # Đảm bảo mã hóa UTF-8
    }
}

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    "CongNghe_scraper.middlewares.CongngheScraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
#    "CongNghe_scraper.middlewares.CongngheScraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
#ITEM_PIPELINES = {
#    "CongNghe_scraper.pipelines.CongngheScraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"