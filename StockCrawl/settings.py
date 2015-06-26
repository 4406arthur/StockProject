# Scrapy settings for StockCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'StockCrawl'

SPIDER_MODULES = ['StockCrawl.spiders']
NEWSPIDER_MODULE = 'StockCrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'StockCrawl (+http://www.yourdomain.com)'
