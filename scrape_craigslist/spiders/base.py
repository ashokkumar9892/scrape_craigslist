import scrapy


class BaseSpider(scrapy.Spider):
    city = 'sandiego'
    region = 'nsd'
    category = 'apartment'[:3]
    allowed_domains = ["craigslist.org"]

    def __init__(self, *args, name='base', **kwargs):
        defaults = {
            'city': self.city,
            'region': self.region,
            'category': self.category
            }
        defaults.update(kwargs)
        for k, v in defaults.items():
            print(k, v)
            setattr(self, k, v)
        self.absolute_next_url = "https://{}.craigslist.org".format(self.city)
        self.start_urls = (
            '/'.join(x for x in (
                self.absolute_next_url,
                'search',
                self.region,
                self.category) if x),
            )
        super().__init__(self, *args, **defaults)
