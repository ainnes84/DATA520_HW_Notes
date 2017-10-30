import scrapy

class QuotesSpider(scrapy.Spider):
    name = "install"
    start_urls = [
        'https://media.readthedocs.org/pdf/scrapy/master/scrapy.pdf',
    ]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            
