from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', ''])
execute(['scrapy','crawl', 'book_spider', '-o', 'data2.csv'])