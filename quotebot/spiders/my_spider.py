import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ["http://quotes.toscrape.com/"]
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield{
                'text' :quote.css("span.text::text").extract_first(),
                'authors' :quote.css("small.author::text").extract_first(),
                'tags' :quote.css("div.tags>a.tags::text").extract_first(),
            }
