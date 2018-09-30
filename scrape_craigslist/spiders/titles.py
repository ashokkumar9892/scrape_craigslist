from .base import BaseSpider


class TitlesSpider(BaseSpider):

    def __init__(self, *args, name='titles', **kwargs):
        super().__init__(self, *args, name=name, **kwargs)

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        for title in titles:
            yield {
                'title': title
                }
