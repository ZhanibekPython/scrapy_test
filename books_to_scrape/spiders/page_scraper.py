import scrapy


class PageScraperSpider(scrapy.Spider):
    name = "page_scraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath("//ol[@class='row']/li")
        print(len(books))
        for book in books:
            yield {
                'image': 'https://books.toscrape.com/' + books.xpath(".//div[@class='image_container']/a/img/@src").get(),
                'title': book.xpath(".//h3/a/@title").get(),
                'price': book.xpath(".//p[@class='price_color']/text()").get()
            }

