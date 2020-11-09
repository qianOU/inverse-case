from scrapy.cmdline import execute
execute(['scrapy','crawl','all_books','-o','data.json'])