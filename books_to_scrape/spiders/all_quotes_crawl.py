import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllQuotesCrawlSpider(CrawlSpider):
    name = "all_quotes_crawl"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = {}
            item["text"] = quote.xpath('.//span[@class="text"]/text()').get()
            item["author"] = quote.xpath('.//small[@class="author"]/text()').get()
            item["tags"] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            yield item


