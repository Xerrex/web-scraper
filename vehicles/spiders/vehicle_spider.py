import scrapy


class VehicleSpider(scrapy.Spider):
    name = 'vehicle'
    allowed_domains = ['https://www.edmunds.com/cars-for-sale-by-owner/']
    start_urls = ['http://https://www.edmunds.com/cars-for-sale-by-owner//']

    def parse(self, response):
        pass
