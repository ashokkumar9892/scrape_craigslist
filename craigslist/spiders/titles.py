import scrapy


class CraigslistSpider(scrapy.Spider):
    city = 'sandiego'
    region = 'nsd'
    category = 'apartment'[:3]
    name = "craigslist"
    absolute_next_url = "https://{}.craigslist.org".format(city)
    start_urls = ["{}/search/{}/{}".format(absolute_next_url, region, category)]
    allowed_domains = ["craigslist.org"]

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class TitlesSpider(CraigslistSpider):
    name = "titles"

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        for title in titles:
            yield {'Title': title}
