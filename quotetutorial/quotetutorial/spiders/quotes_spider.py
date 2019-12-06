import scrapy

class QuoteSpider(scrapy.Spider):
    name="quotes"
    start_urls = ["https://github.com/somenath1435"]

    def parse(self, response):
        title = response.css(".d-block.overflow-hidden::text").extract()
        yield {"titletext": title}