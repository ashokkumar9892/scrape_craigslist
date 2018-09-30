from scrapy import Request
from .titles import CraigslistSpider


class JobsSpider(CraigslistSpider):
    name = 'allcontent'

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')

        for job in jobs:
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            title = job.xpath('a/text()').extract_first()
            sqft = job.xpath('span[@class="result-meta"]/span[@class="result-housing"]/text()').extract_first("")[2:-1]
            address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]

            yield Request(absolute_url, callback=self.parse_page, meta={
                'url': absolute_url, 'title': title, 'address': address, 'sqft': sqft})

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = self.absolute_next_url + relative_next_url
        yield Request(absolute_next_url, callback=self.parse)

    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')

        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract()).strip()

        compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//p[@class="attrgroup"]/span[2]/b/text()').extract_first()

        yield {
            'url': url,
            'title': title,
            'address': address,
            'description': description,
            'dollars': compensation,
            'kind': employment_type,
            'body': response.body
            }
